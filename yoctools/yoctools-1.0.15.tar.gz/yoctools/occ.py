import json
import yaml
import time
from requests_toolbelt import MultipartEncoder

try:
    raw_input = raw_input
except NameError:
    raw_input = input

try:
    from component import *
    from tools import *
except:
    from yoctools.component import *
    from yoctools.tools import *


def get_url(cmd, text):
    timestamp = time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time()))
    md5 = MD5(cmd + timestamp + text)
    return '%s?timestamp=%s&sign=%s' % (cmd, timestamp, md5)

authorization = ''
login_time = 0

class OCC:
    def __init__(self, host=None):

        if host:
            self.host = host
        else:
            self.host = 'occ.t-head.cn'
            self.host = 'pre.occ.t-head.cn'


    def logout(self):
        global authorization, login_time
        authorization = ''
        login_time = 0


    def login(self):
        global authorization, login_time

        if authorization and time.time() - login_time < 25 * 50:
            return
        user = ''
        password = ''
        config_file = os.path.expanduser('~/.yocrc')
        conf = yaml_load(config_file)
        if conf == None:
            conf = {}
        if 'username' in conf:
            username = conf['username']
        else:
            username= raw_input('Input occ login username: ')

        if 'password' in conf:
            password = conf['password']
        else:
            password = raw_input('Input user password: ')

        cmd = '/api/base/auth/login'
        body = {
            "name": str(username),
            "password": password
        }
        js, _ = self.request(cmd, body)
        if 'userToken' in js:
            authorization = js['userToken']
            login_time = time.time()


    def upload(self, version, type, filename):
        global authorization, login_time
        cmd = '/api/resource/component/upload'

        m = MultipartEncoder(
            fields = {
                'version': version,
                'type': type,
                'file': (os.path.basename(filename), open(filename, 'rb'))
            }
        )
        headers = {
            'Content-Type': m.content_type,
            'Authorization': authorization,
        }

        js, error = self.request(cmd, m, headers, sign = False)
        if error == -2:
            self.logout()
            self.login()
            js, error = self.request(cmd, m, headers, sign = False)


    def yocGetInfo(self, name):
        cmd = '/api/resource/component/getInfo'
        body = {}
        js, _ = self.request(cmd, body)


    def yocComponentList(self, chipId):
        cmd = '/api/resource/component/getList'
        body = {
            "type": "common",
            "name": "",
            "pageIndex": 1,
            "pageSize": 10,
        }

        js, _ = self.request(cmd, body)
        print(json.dumps(js, indent=4))

        if 'packages' in js:
            packs = ComponentGroup()
            for p in js['packages']:
                pack = Component()
                pack.loader_json(p)
                packs.add(pack)
            return packs


    def request(self, url, body, headers=None, sign=True):
        if sign:
            body = json.dumps(body)
            url = get_url(url, body)

        connection = http.HTTPSConnection(self.host)

        try:
            if not headers:
                headers = {"Content-type": "application/json"}
            connection.request('POST', url, body, headers)
            response = connection.getresponse()
            if response.status == 200:
                text = response.read()
                js = json.loads(text)

                if js['code'] != 0:
                    print(js['msg'])
                return js['result'], js['code']
        except Exception as e:
            print(str(e))

        return {}, -1


if __name__ == "__main__":
    occ = OCC()
    occ.login()



    occ.yocComponentList('')
    # occ.upload("master", 'common', 'netmgr.zip')
    # occ.upload('master', 'setup.py')