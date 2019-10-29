import cx_Oracle
import uuid
import time
from sync.base import BaseSync
from config import ORACLE_SERVER
from utils.code import b64encode
from classcard_dataclient.models.course import CourseTableManager, Course
from classcard_dataclient.models.classroom import Classroom, RoomType
from classcard_dataclient.models.subject import Subject
from utils.loggerutils import logging

logger = logging.getLogger(__name__)


class CourseTableSync(BaseSync):
    def __init__(self):
        super(CourseTableSync, self).__init__()
        db = cx_Oracle.connect(ORACLE_SERVER, encoding="UTF-8", nencoding="UTF-8")  # 连接数据库
        print(db.version)
        self.offset = 300
        self.cur = db.cursor()
        self.xn = '2019-2020'
        self.yjs_xq = '第一学期'
        self.xq = '1'
        manager_name = "{}-{}".format(self.xn, self.xq)
        manager_number = b64encode(manager_name)
        self.manager = CourseTableManager(name=manager_name, number=manager_number)
        self.course_map = {}
        self.space_map = {}
        self.space_container = {}
        self.classroom_map = {}
        self.subject_map = {}
        self.subject_names = []
        self.subject_number_name = {}

    def analyse_building(self, classroom_name):
        building, floor = None, None
        if classroom_name:
            key_words = ["楼", "区"]
            for kw in key_words:
                if kw in classroom_name:
                    kw_index = classroom_name.index(kw)
                    building = classroom_name[:kw_index + 1]
                    try:
                        floor = str(int(classroom_name[-3]))
                        # if '区' in classroom_name:
                        #     floor = str(int(classroom_name[kw_index + 1]))
                        # elif '座' in classroom_name:
                        #     zuo_index = classroom_name.index('座')
                        #     floor = str(int(classroom_name[zuo_index + 1]))
                        # else:
                        #     floor = str(int(classroom_name[kw_index + 2]))
                    except (Exception,):
                        pass
                    break
        return building, floor

    def create_unique(self, container, obj, salt=None):
        unique_obj = obj
        if obj in container:
            if salt and (obj + salt) not in container:
                unique_obj = obj + salt
            else:
                index = 0
                while True:
                    if (obj + str(index)) not in container:
                        unique_obj = obj + str(index)
                        break
                    index += 1
        return unique_obj

    def analyse_position(self, jc, week):
        course_week = int(week)
        position = []
        jc_items = jc.split('-')
        if len(jc_items) == 1:
            position.append((int(jc_items[0]), course_week))
        elif len(jc_items) == 2:
            for item in range(int(jc_items[0]), int(jc_items[1]) + 1):
                position.append((item, course_week))
        return position

    def combine_course(self):
        new_course_map = {}
        for space_name, container in self.space_container.items():
            sorted_c = sorted(container, key=lambda c: c.name)
            choose_c = sorted_c[0]
            self.space_map[space_name] = choose_c
            if choose_c.name not in new_course_map:
                new_course_map[choose_c.name] = choose_c
        self.course_map = new_course_map

    def in_area(self, area):
        key = ['长清B区', '长清C区', '教学一', '教学二', '教学三', '教学四']
        for k in key:
            if k in area:
                return True
        return True

    def analyse_sksj(self, sksj):
        try:
            if "星期" not in sksj:
                return None
            week_map = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "日": 7}
            index_map = {"上午": 0, "下午": 4, "晚上": 8}
            sksj_split = sksj.split(":")
            week_range = sksj_split[0][1:-1].split("-")
            begin_week, end_week = int(week_range[0]), int(week_range[1])
            schedule_info = sksj_split[1]
            single = 0
            if "单周" in schedule_info:
                single = 1
            elif "双周" in schedule_info:
                single = 2
            position_info = schedule_info.split("  ")[-1].split(",")
            positions = []
            for info in position_info:
                r_info = info[1:] if info[0] == ' ' else info
                week = week_map.get(r_info[2], None)
                index = index_map.get(r_info[4:6], 0)
                try:
                    begin_num, end_num = index + int(r_info[6]), index + int(r_info[10])
                except (ValueError,):
                    index = index_map.get(r_info[5:7], 0)
                    begin_num, end_num = index + int(r_info[7]), index + int(r_info[7])
                for num in range(begin_num, end_num + 1):
                    positions.append((num, week))
            result = {'begin_week': begin_week, 'end_week': end_week, 'single': single, "positions": positions}
        except (Exception,) as e:
            print("{}\n".format(sksj))
            return None
        return result

    def get_yjs_course(self):
        course_map = {}
        sql = "SELECT KCMC, KCBH, ZGH, RKJSXM, DZ, SKSJ FROM V_YJSKB " \
              "WHERE TERMNAME='{}{}' ORDER BY KCBH".format(self.xn, self.yjs_xq)
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for row in rows:
            subject_name, subject_number = row[0], row[1]
            subject_info = self.process_subject_info(subject_number, subject_name)
            subject_name, subject_number = subject_info['name'], subject_info['number']
            teacher_number = row[2]
            classroom_name = row[4] or "{}nirvana场地".format(subject_name)
            time_info = row[5]
            if not self.in_area(classroom_name):
                continue
            if not (time_info and classroom_name):
                continue
            time_result = self.analyse_sksj(time_info)
            if not time_result:
                continue
            course_name = classroom_name + subject_number + teacher_number
            if course_name in course_map:
                course = course_map[course_name]
            else:
                course_number = str(uuid.uuid4())
                classroom_num = b64encode(classroom_name)[:63]
                if 'nirvana场地' not in classroom_name and classroom_num not in self.classroom_map:
                    building, floor = self.analyse_building(classroom_name)
                    self.classroom_map[classroom_num] = Classroom(number=classroom_num, name=classroom_name,
                                                                  building=building, floor=floor,
                                                                  category=RoomType.TYPE_PUBLIC)
                course = Course(number=course_number, name=course_name, teacher_number=teacher_number,
                                classroom_number=classroom_num, subject_number=subject_number,
                                begin_week=time_result['begin_week'], end_week=time_result['end_week'],
                                required_student=False)
                self.course_map[course_name] = course
            for position in time_result['positions']:
                course.add_position(position[0], position[1], time_result['single'])
        return course_map

    def get_bk_course(self):
        single_map = {"单": 1, "双": 2}
        count_sql = "SELECT COUNT(*) FROM V_BZKS_JSKB WHERE XN='{}' AND XQ='{}'".format(self.xn, self.xq)
        self.cur.execute(count_sql)
        try:
            total = self.cur.fetchall()[0][0]
        except (Exception,):
            total = 1
        total_page = total // self.offset if total % self.offset == 0 else total // self.offset + 1
        for index in range(total_page):
            print(">>> Get course in {}/{}".format(index + 1, total_page))
            si, ei = index * self.offset + 1, (index + 1) * self.offset
            sql = "SELECT k.KCDM, k.SKBJH, k.RKJSGH, k.ZC, k.XQJ, k.DSZ, k.JC, k.SKDD, k.r " \
                  "FROM (SELECT x.*, rownum r FROM V_BZKS_JSKB x " \
                  "WHERE XN='{}' AND XQ='{}' ORDER BY KCDM) " \
                  "k WHERE k.r BETWEEN {} and {} ".format(self.xn, self.xq, si, ei)
            self.cur.execute(sql)
            rows = self.cur.fetchall()
            for row in rows:
                subject_number = row[0]
                subject_info = self.process_subject_info(subject_number)
                subject_name, subject_number = subject_info['name'], subject_info['number']
                class_number = row[1]
                classroom_name = row[7] or "{}nirvana场地".format(subject_name)
                teacher_number = row[2]
                week_range = row[3]
                week, num = row[4], row[6]
                single = single_map.get(row[5], 0)
                begin_week, end_week = int(week_range.split("-")[0]), int(week_range.split("-")[-1])
                if not self.in_area(classroom_name):
                    continue
                try:
                    space_name = classroom_name + week_range + num + week + str(single)
                    course_name = classroom_name + subject_number + teacher_number + class_number
                except (Exception,) as e:
                    continue
                if course_name in self.course_map:
                    course = self.course_map[course_name]
                else:
                    course_number = str(uuid.uuid4())
                    classroom_num = b64encode(classroom_name)[:63]
                    if 'nirvana场地' not in classroom_name and classroom_num not in self.classroom_map:
                        building, floor = self.analyse_building(classroom_name)
                        self.classroom_map[classroom_num] = Classroom(number=classroom_num, name=classroom_name,
                                                                      building=building, floor=floor,
                                                                      category=RoomType.TYPE_PUBLIC)
                    if subject_number not in self.subject_map:
                        self.add_subject(subject_number, subject_number, subject_info['ori_num'])
                    course = Course(number=course_number, name=course_name, teacher_number=teacher_number,
                                    classroom_number=classroom_num, subject_number=subject_number,
                                    begin_week=begin_week, end_week=end_week, required_student=False)
                    self.course_map[course_name] = course

                positions = self.analyse_position(num, week)
                for position in positions:
                    course.add_position(position[0], position[1], single)
                if space_name not in self.space_container:
                    self.space_container[space_name] = []
                if course_name not in self.space_container[space_name]:
                    self.space_container[space_name].append(course)

    def get_subjects(self):
        sql1 = "SELECT DISTINCT KCBH, KCMC FROM V_YJSKB " \
               "WHERE TERMNAME='{}{}' ORDER BY KCBH".format(self.xn, self.yjs_xq)
        sql2 = "SELECT DISTINCT kcdm, KCMC FROM V_BZKS_XSKB" \
               " WHERE XN='{}' AND XQ='{}' ORDER BY KCDM".format(self.xn, self.xq)
        for sql in [sql1, sql2]:
            self.cur.execute(sql)
            rows = self.cur.fetchall()
            for row in rows:
                subject_number, subject_name = row[0], row[1]
                if not (subject_number and subject_name):
                    continue
                subject_info = self.process_subject_info(subject_number, subject_name)
                subject_name, subject_number = subject_info['name'], subject_info['number']
                if subject_number not in self.subject_map:
                    self.add_subject(subject_name, subject_number, subject_info['ori_num'])

    def process_subject_info(self, subject_number, subject_name=None):
        if subject_number in self.subject_number_name:
            info = self.subject_number_name[subject_number]
        else:
            if subject_name:
                info = {'name': subject_name, 'number': b64encode(subject_name)[:63], 'ori_num': subject_number}
            else:
                info = {'name': subject_number, 'number': subject_number, 'ori_num': subject_number}
            self.subject_number_name[subject_number] = info
        return info

    def add_subject(self, subject_name, subject_number, ori_number):
        f_subject_name = self.create_unique(self.subject_names, subject_name, ori_number[-2:])
        if ori_number in ["160660314", "160920244", "163000004", "Y008030", "s022005", "160500101", "221006002"]:
            f_subject_name = "{}.".format(f_subject_name)
        self.subject_map[subject_number] = Subject(number=subject_number, name=f_subject_name)
        self.subject_names.append(f_subject_name)

    def relate_student(self):
        single_map = {"单": 1, "双": 2}
        count_sql = "SELECT COUNT(*) FROM V_BZKS_XSKB WHERE XN='{}' AND XQ='{}'".format(self.xn, self.xq)
        self.cur.execute(count_sql)
        try:
            total = self.cur.fetchall()[0][0]
        except (Exception,):
            total = 1
        total_page = total // self.offset if total % self.offset == 0 else total // self.offset + 1
        for index in range(total_page):
            print(">>> Related student in {}/{}".format(index + 1, total_page))
            si, ei = index * self.offset + 1, (index + 1) * self.offset
            sql = "SELECT k.KCDM, k.SKBJ, k.RKJSGH, k.ZC, k.XQJ, k.DSZ, k.JC, k.SKDD, k.XH, k.KCMC, k.r " \
                  "FROM (SELECT x.*, rownum r FROM V_BZKS_XSKB x " \
                  "WHERE XN='{}' AND XQ='{}' ORDER BY KCDM) " \
                  "k WHERE k.r BETWEEN {} and {} ".format(self.xn, self.xq, si, ei)
            self.cur.execute(sql)
            rows = self.cur.fetchall()
            for row in rows:
                subject_number, subject_name = row[0], row[9]
                subject_info = self.process_subject_info(subject_number)
                subject_name, subject_number = subject_info['name'], subject_info['number']
                classroom_name = row[7] or "{}场地".format(subject_number)
                week_range = row[3]
                week, num = row[4], row[6]
                single = single_map.get(row[5], 0)
                student_number = row[8]
                if not self.in_area(classroom_name):
                    continue
                try:
                    space_name = classroom_name + week_range + num + week + str(single)
                except (Exception,):
                    print(row)
                    continue
                course = self.space_map.get(space_name, None)
                if course:
                    course.add_student(student_number)

    def sync(self):
        print(">>>Start course sync")
        t1 = time.time()
        self.get_subjects()
        self.get_bk_course()
        print(">>>Start upload subjects")
        subjects = list(self.subject_map.values())
        self.client.create_subjects(self.school_id, subjects)
        print(">>>Finish upload subject")
        self.combine_course()
        print(">>>Total have {} courses".format(len(self.course_map)))
        self.relate_student()

        yjs_course = self.get_yjs_course()
        self.course_map.update(yjs_course)

        for number, course in self.course_map.items():
            self.manager.add_course(course)
        t2 = time.time()
        print(">>>Finish data process, cost {}s".format(t2 - t1))
        print(">>>Start upload classroom")
        classrooms = list(self.classroom_map.values())
        self.client.create_classrooms(self.school_id, classrooms)
        t3 = time.time()
        print(">>>Finish upload classroom, cost {}s".format(t3 - t2))
        print(">>>Start upload course table")
        self.client.create_course_table(self.school_id, self.manager)
        t4 = time.time()
        print(">>>Finish upload course table, cost {}s".format(t4 - t3))
        print(">>>Total cost {}s".format(t4 - t1))
