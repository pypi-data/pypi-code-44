# sqlx 是一种扩展 sql 的语言
# 目标是打造 "易读易写 方便维护" 的 sql 脚本
# 语法参考 test.sqlx

import os
import sys
import re
import pprint
import sqlformat



# 构建后添加的头部文字
HEADER = '-- ======== Generated By Sqlx ========\n-- https://github.com/taojy123/sqlx'

# sqlx 语法注释标记
COMMENT_PREFIX = '-- !'

# 目前支持的关系运算符
OPERATORS = ['>', '<', '>=', '<=', '==', '!=']


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def remove_space_line(sql):
    # 移除空行
    new_lines = []
    for line in sql.splitlines():
        if line.strip():
            new_lines.append(line)
    return '\n'.join(new_lines)


def get_indent(s):
    # 获取字符串前有多少个空格
    return len(s) - len(s.lstrip())



def render(content, define_map, block_map, local_map=None):
    # render sqlt content to sql

    key_map = {}
    key_map.update(define_map)
    if local_map:
        key_map.update(local_map) 

    # 处理 for 循环，暂时不支持嵌套
    for_blocks = re.findall(r'(\{\s*%\s*for\s+(.+?)\s+in\s+(.+?)\s*%\s*\}(.*?)\{\s*%\s*endfor\s*%\s*\})', content, re.S)
    for full_block, for_names, for_values, for_content in for_blocks:
        for_names = for_names.split('|')
        for_values = for_values.split(',')
        for_values = [t.split('|') for t in for_values]
        # {% for n|m in 1|a,2|b,3|c %} ... {% endfor %}
        # => 
        # for_names = ['n', 'm']
        # for_values = [['1', 'a'], ['2', 'b'], ['3', 'c']]
        rendered_blocks = []
        for values in for_values:
            local_map = {}
            local_map.update(key_map)
            for for_name, for_value in zip(for_names, values):
                local_map[for_name] = for_value
            # local_map => {n: 1, m: a}
            rendered_block = render(for_content, define_map, block_map, local_map)
            rendered_block = remove_space_line(rendered_block)
            rendered_blocks.append(rendered_block)

        rendered_blocks = '\n'.join(rendered_blocks)
        content = content.replace(full_block, rendered_blocks)

    # 处理 if 判断，暂时不支持嵌套
    if_blocks = re.findall(r'(\{\s*%\s*if(.+?)%\s*\}(.*?)\{\s*%\s*endif\s*%\s*\})', content, re.S)
    for full_block, condition, if_content in if_blocks:
        # {% if a > b %} ... {% else %} ... {% endif %}
        if_content = re.sub(r'\{\s*%\s*else\s*%\s*\}', r'{% else %}', if_content)
        ts = if_content.split(r'{% else %}')
        assert len(ts) in [1, 2], f'{full_block} 内容编写错误!'
        if_content = ts[0]
        if len(ts) == 2:
            else_content = ts[1]
        else:
            else_content = ''

        a1 = a2 = None
        for op in OPERATORS:
            if op in condition:
                assert condition.count(op) == 1, f'{condition} 判定条件编写错误!'
                a1, a2 = condition.split(op)
                a1 = a1.strip()
                a2 = a2.strip()
                break
        assert a1 and a2, f'{condition} 未找到合法的关系运算符!'

        # 判断项默认以字符串类型比较，如果正好是变量名称则转为变量值，如果外加单引号或双引号则强制为原字符串
        r1 = re.findall(r'''^['"](.+)['"]$''', a1)
        if r1:
            a1 = r1[0]
        elif a1 in key_map:
            a1 = key_map[a1]

        r2 = re.findall(r'''^['"](.+)['"]$''', a2)
        if r2:
            a2 = r2[0]
        elif a2 in key_map:
            a2 = key_map[a2]

        # 比较前会先尝试将两个变量转为数字类型
        try:
            a1 = float(a1)
        except ValueError as e:
            pass
        try:
            a2 = float(a2)
        except ValueError as e:
            pass

        a1 = repr(a1)
        a2 = repr(a2)
        result = eval(f'{a1} {op} {a2}')

        assert result in (True, False)

        if result:
            rendering_content = if_content
        else:
            rendering_content = else_content

        rendered_block = render(rendering_content, define_map, block_map, key_map)
        rendered_block = remove_space_line(rendered_block)
        content = content.replace(full_block, rendered_block)

    # 处理 define 替换和 block 替换
    tags = re.findall(r'\{.+?\}', content)
    tags = set(tags)
    rendered_map = {}
    for tag in tags:
        key = tag.strip('{}').strip()
        if '(' not in key:
            assert key in key_map, f'`{tag}` define 引用未找到!'
            value = key_map[key]
            # 对于简单的变量替换，直接 replace 就行了
            content = content.replace(tag, value)
        else:
            rs = re.findall(r'(.+?)\((.*?)\)', key)
            assert len(rs) == 1, f'`{tag}` block 引用语法不正确!'
            block_name, params = rs[0]
            assert block_name in block_map, f'`{tag}` block 引用未找到!'
            block_content = block_map[block_name]['content']
            param_names = block_map[block_name]['params']
            params = params.split(',')
            params = [param.strip() for param in params if param.strip()]
            assert len(param_names) == len(params), f'{tag} block 参数数量不正确!'
            local_map = {}
            for name, value in zip(param_names, params):
                local_map[name] = value
            rendered_block = render(block_content, define_map, block_map, local_map)
            # 对于块替换，为了更好的视觉体验，先将渲染后的块内容保存下来，接下来用到
            rendered_map[tag] = rendered_block

    lines = content.splitlines()
    new_lines = []
    for line in lines:
        for tag in rendered_map.keys():
            if tag in line:
                # 遍历每一行，替换行中的块内容，并加上合适的缩进
                # 例如 `select * from {myblock} where 1=1` 渲染后得到:
                # select * from 
                #     (
                #         SELECT
                #             id, name
                #         FROM
                #             mytable
                #     ) AS myblock
                # where 1=1
                n = get_indent(line)
                rendered_block = rendered_map[tag]
                rendered_block = rendered_block.replace('\n', '\n' + ' ' * n)
                rendered_block = '\n' + ' ' * n + rendered_block + '\n' + ' ' * n
                # 先尝试替换 tag 两边有空格的情况
                line = line.replace(f' {tag} ' , rendered_block)
                line = line.replace(tag, rendered_block)
        new_lines.append(line)
    content = '\n'.join(new_lines)

    return content


def build(content, pretty=False):
    # build sqlx content to sql

    define_map = {}
    block_map = {}


    # 处理 define 和 sqlx 注释
    lines = content.splitlines()
    # 确保第一行是空行
    new_lines = [''] 
    for line in lines:

        if line.startswith(COMMENT_PREFIX):
            continue

        if COMMENT_PREFIX in line:
            i = line.find(COMMENT_PREFIX)
            line = line[:i]

        if line.lower().startswith('define '):
            line = line.replace('=', ' ')
            items = line.split()
            assert len(items) == 3, f'`{line}` define 语法不正确!'
            define, key, value = items
            define_map[key] = value
            continue

        new_lines.append(line)
    # pprint.pprint(define_map)

    sqlx_content = '\n'.join(new_lines)
    # print(sqlx_content)

    # 处理 block
    block_pattern = r'\nblock\s+(.+?)\((.*?)\)[:\s]*\n(.*?)\nendblock'
    blocks = re.findall(block_pattern, sqlx_content, re.S)
    sqlx_content = re.sub(block_pattern, '', sqlx_content, flags=re.S)
    for block in blocks:
        block_name, params, content = block
        params = params.split(',')
        params = [param.strip() for param in params if param.strip()]
        block_map[block_name] = {
            'params': params,
            'content': content,
        }
    # pprint.pprint(block_map)


    sql = render(sqlx_content, define_map, block_map)
    sql = sql.strip()
    # sql = remove_space_line(sql)
    sql = f'{HEADER}\n\n{sql}\n'

    # print(sql)

    if pretty:
        sql = sqlformat.sqlformat(sql)

    return sql


def auto(path='.', pretty=False):
    # pip intall sqlx
    # sqlx [path/to/sqlxfiles]

    args = sys.argv
    if len(args) > 1:
        path = args[1]

    if 'pretty' in args:
        pretty = True

    if os.path.isdir(path):
        files = os.listdir(path)
        files = [file for file in files if file.endswith('.sqlx')]
    elif os.path.isfile(path) and path.endswith('.sqlx'):
        files = [path]
    else:
        print('Usage: sqlx path/to/sqlxfiles')
        return 1

    for file in files:
        # build xx.sqlx to dist/xx.sql

        dirname, filename = os.path.split(file)
        dirname = os.path.join(dirname, 'dist')
        filename = os.path.join(dirname, filename[:-1])

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        for encoding in ['utf8', 'gbk']:
            try:
                sqlx_content = open(file, encoding=encoding).read()
                break
            except Exception as e:
                encoding = None
                
        if not encoding:
            print(file, 'read failed!')

        sql_content = build(sqlx_content, pretty)
        open(filename, 'w', encoding=encoding).write(sql_content)
        print(f'{filename} built')

    print('Finish!')


if __name__ == '__main__':
    print(build(open('demo.sqlx', encoding='utf8').read(), True))

