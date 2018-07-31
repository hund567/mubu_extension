# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import codecs


#这个函数是为了将幕布的文件标准化输出
#思路如下：
    #1.逐行读取数据，并使用正则来区分字段级别
    #2.按照anki_mindnode.html的字段描述来创建字段值，(node_id,parent_id,value)这种形式也可以做成字典{node_id：,parent_id:,value: }这样的形式
    #但是考虑到javascripts数组不是很合适，只能用对象的形式，我们不如创建一个个的对象，三条属性：node_id,parent_id,value
    #这样在anki的输入字段，我们就可以直接输入json格式的字符串就行，anki会做自动解析
def trans():
    infile = 'D:/test.txt'
    f = open(infile,'r')
    sourceline = f.readlines()
    array=[]

    sub1_flag = 0
    sub2_flag = 1
    sub3_flag = 1
    sub4_flag = 1
    sub5_flag = 1
    sub6_flag = 1
    sub7_flag = 1
    sub8_flag = 1
    sub9_flag = 1
    sub10_flag = 1
    sub11_flag = 1

    for each_line in sourceline:
        dict1 = {"id": "", "parentid": "", "topic": ""}
        each_line_list = each_line.split("-",1)
        sub_level_flag = len(each_line_list[0])

        if sub_level_flag == 0:
            dict1["id"]  = "root"
            dict1["parentid"]  = "aa"
            dict1["topic"]  = each_line_list[1].encode("UTF-8")
            sub1_flag = sub1_flag +1

        elif sub_level_flag == 2:
            dict1["id"] = "sub"+ str(sub2_flag)
            dict1["parentid"] = "root"
            dict1["topic"] = each_line_list[1].encode("UTF-8")
            sub2_flag = sub2_flag + 1
        elif sub_level_flag == 4:
            dict1["id"] = "sub"+ str(sub2_flag-1) + str(sub3_flag)
            dict1["parentid"] = "sub"+ str(sub2_flag-1)
            dict1["topic"] = each_line_list[1].encode("UTF-8")
            sub3_flag = sub3_flag + 1
        elif sub_level_flag == 6:
            dict1["id"] = "sub"+ str(sub2_flag-1) + str(sub3_flag-1)+str(sub4_flag)
            dict1["parentid"] = "sub"+ str(sub2_flag-1)+ str(sub3_flag-1)
            dict1["topic"] = each_line_list[1].encode("UTF-8")
            sub4_flag = sub4_flag + 1

        elif sub_level_flag == 8:
            dict1["id"] = "sub"+ str(sub2_flag-1) + str(sub3_flag-1)+str(sub4_flag-1)+str(sub5_flag)
            dict1["parentid"] = "sub"+ str(sub2_flag-1)+ str(sub3_flag-1)+str(sub4_flag-1)
            dict1["topic"] = each_line_list[1].encode("UTF-8")
            sub5_flag = sub5_flag + 1

        elif sub_level_flag == 10:
            dict1["id"] = "sub" + str(sub2_flag - 1) + str(sub3_flag - 1) + str(sub4_flag - 1) + str(sub5_flag-1) + str(sub6_flag)
            dict1["parentid"] = "sub" + str(sub2_flag - 1) + str(sub3_flag - 1) + str(sub4_flag - 1) + str(sub5_flag-1)
            dict1["topic"] = each_line_list[1].encode("UTF-8")
            sub6_flag = sub6_flag + 1


        elif sub_level_flag == 12:
            dict1["id"] = "sub" + str(sub2_flag - 1) + str(sub3_flag - 1) + str(sub4_flag - 1) + str(
                sub5_flag - 1) + str(sub6_flag-1)+ str(sub7_flag)
            dict1["parentid"] = "sub" + str(sub2_flag - 1) + str(sub3_flag - 1) + str(sub4_flag - 1) + str(sub5_flag - 1)+ str(sub6_flag - 1)
            dict1["topic"] = each_line_list[1].encode("UTF-8")
            sub7_flag = sub7_flag + 1


        elif sub_level_flag == 14:
            dict1["id"] = "sub" + str(sub2_flag - 1) + str(sub3_flag - 1) + str(sub4_flag - 1) + str(
                sub5_flag - 1) + str(sub6_flag - 1) + str(sub7_flag-1)+ str(sub8_flag)
            dict1["parentid"] = "sub" + str(sub2_flag - 1) + str(sub3_flag - 1) + str(sub4_flag - 1) + str(
                sub5_flag - 1) + str(sub6_flag - 1)+ str(sub7_flag-1)
            dict1["topic"] = each_line_list[1].encode("UTF-8")
            sub8_flag = sub8_flag + 1

        elif sub_level_flag == 16:
            dict1["id"] = "sub" + str(sub2_flag - 1) + str(sub3_flag - 1) + str(sub4_flag - 1) + str(
                sub5_flag - 1) + str(sub6_flag - 1) + str(sub7_flag-1)+ str(sub8_flag-1)+ str(sub9_flag)
            dict1["parentid"] = "sub" + str(sub2_flag - 1) + str(sub3_flag - 1) + str(sub4_flag - 1) + str(
                sub5_flag - 1) + str(sub6_flag - 1)+ str(sub7_flag-1)+ str(sub8_flag-1)
            dict1["topic"] = each_line_list[1].encode("UTF-8")
            sub9_flag = sub9_flag + 1


        elif sub_level_flag == 16:
            dict1["id"] = "sub" + str(sub2_flag - 1) + str(sub3_flag - 1) + str(sub4_flag - 1) + str(
                sub5_flag - 1) + str(sub6_flag - 1) + str(sub7_flag - 1) + str(sub8_flag - 1) + str(sub9_flag-1)+str(sub10_flag)
            dict1["parentid"] = "sub" + str(sub2_flag - 1) + str(sub3_flag - 1) + str(sub4_flag - 1) + str(
                sub5_flag - 1) + str(sub6_flag - 1) + str(sub7_flag - 1) + str(sub8_flag - 1)+str(sub9_flag-1)
            dict1["topic"] = each_line_list[1].encode("UTF-8")
            sub10_flag = sub10_flag + 1


        elif sub_level_flag == 16:
            dict1["id"] = "sub" + str(sub2_flag - 1) + str(sub3_flag - 1) + str(sub4_flag - 1) + str(
                sub5_flag - 1) + str(sub6_flag - 1) + str(sub7_flag - 1) + str(sub8_flag - 1) + str(
                sub9_flag - 1) + str(sub10_flag-1) + str(sub11_flag)
            dict1["parentid"] = "sub" + str(sub2_flag - 1) + str(sub3_flag - 1) + str(sub4_flag - 1) + str(
                sub5_flag - 1) + str(sub6_flag - 1) + str(sub7_flag - 1) + str(sub8_flag - 1) + str(sub9_flag - 1)+str(sub10_flag-1)
            dict1["topic"] = each_line_list[1].encode("UTF-8")
            sub11_flag = sub11_flag + 1
        array.append(dict1)

    f1 = codecs.open('D:/test2.txt', 'w', 'utf-8')
    json_str = json.dumps(array,ensure_ascii=False)
    print json_str
    f1.write(json_str)
if __name__ == '__main__':
    trans()
