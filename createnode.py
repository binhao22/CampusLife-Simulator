
import os
import csv
from py2neo import Graph,Node,Relationship,NodeMatcher
#f = os.system("D:\\neo4j-windows\\neo4j-community-4.3.3-windows\\neo4j-community-4.3.3\\bin\\neo4j.bat console")

# Graph()中第一个为local host链接，auth为认证，包含 username 和 password
class CreateNode:
    def __init__(self, uri, user, password):
        self.g= Graph(uri, auth=(user, password))

        self.g.run("Match(n) optional match(n)-[r] -() Delete n,r")
        xunke_node = Node("Node", name="选课")
        self.matcher = NodeMatcher(self.g)
#创建选课数据库
        with open(r'.\resource\csv\xuanke.csv', 'r', encoding='GBK') as file:
            print("当前行数：当前内容：")
            reader = csv.reader(file)
            for item in reader:
                if reader.line_num == 0:
                    continue
                #        print("当前行数：", reader.line_num, "当前内容：", item)
                course_node = Node("Course", name=item[0], teacher=item[1])
                condition_node = Node("Condition", content=item[2])
                result_node = Node("Result", content=item[3])
                value_node = Node("Value", a=item[4], b=item[5], c=item[6], d=item[7], e=item[8])
                relation1 = Relationship(result_node, 'condition', condition_node)
                relation2 = Relationship(result_node, 'result', course_node)
                relation3 = Relationship(result_node, 'value', value_node)
                relation = Relationship(xunke_node, 'contains', course_node)
                self.g.create(relation1)
                # g.create(relation2)
                self.g.create(relation3)
                # g.create(relation)
                self.g.merge(course_node, "Course", "name")
                self.g.merge(relation, "Course", "name")
                # g.merge(relation1, "Course", "name")
                self.g.merge(relation2, "Course", "name")
                # g.merge(relation3, "Course", "name")
#创建随机课程事件库
        randomcourse = Node("Randomcourse", name='课程事件')
        with open(r'.\resource\csv\随机课程事件.csv', 'r', encoding='utf-8') as file:
            print("当前行数：当前内容：")
            reader = csv.reader(file)
            for item in reader:
                if reader.line_num == 0:
                    continue
                #        print("当前行数：", reader.line_num, "当前内容：", item)
                time_node = Node("Time", time=item[0])
                course_node = Node("Course", name=item[1])
                event_node = Node("Result", content=item[2])
                #        value_node = Node("Value", a=item[4], b=item[5], c=item[6], d=item[7], e=item[8])
                relation1 = Relationship(course_node, 'contains', time_node)
                relation2 = Relationship(course_node, 'result', event_node)
                #        relation3 = Relationship(course_node, 'value', value_node)
                relation = Relationship(randomcourse, 'contains', time_node)
                # g.create(relation1)
                self.g.create(relation2)
                #
                #        g.create(relation3)
                self.g.merge(time_node, "Time", "time")
                self.g.merge(relation1, "Time", "time")
                self.g.create(relation)
