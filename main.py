# -*- coding: utf-8 -*-

import sys
import jieba
import jieba.analyse
import operator
import pandas as pd
from collections import Counter

#filename = r"C:\Users\ojdf\Downloads\红楼梦.txt"
filename = r"C:\Users\ojdf\Downloads\哈利波特.txt"

def fenci(file_name):
    f = open(file_name, 'r+',encoding='utf-8')
    file_list = f.read()
    f.close()

    seg_list = list(jieba.cut(file_list, cut_all=True))
    tf = {}
    for seg in seg_list:
        seg = ''.join(seg.split())
        if (seg != '' and seg != "\n" and seg != "\n\n"):
            if seg in tf:
                tf[seg] += 1
            else:
                tf[seg] = 1

    #tf = sorted(tf.items(), key = operator.itemgetter(1), reverse = True)

    arr = list(tf.items())
    df = pd.DataFrame(list(tf.items()), columns=['word', 'counts'])
    df = df[df.word.len()>1]
    df = df.sort_index(by='counts', ascending = False)
    print(df)

    f = open("result.txt", "w+")
    for item in tf:
        f.write(item + " " + str(tf[item]) + "\n")
    f.close()


fenci(filename)