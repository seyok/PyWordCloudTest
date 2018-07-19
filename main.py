# -*- coding: utf-8 -*-

import jieba
import jieba.analyse
import pandas as pd
from wordcloud import WordCloud


files = ["红楼梦.txt", "哈利波特.txt", "水浒传.txt", "西游记.txt", "三国演义.txt"]


def fenci(file_name):
    f = open(file_name, 'r+', encoding='utf-8')
    file_list = f.read()
    f.close()

    seg_list = list(jieba.cut(file_list, cut_all=True))
    tf = {}
    for seg in seg_list:
        seg = ''.join(seg.split())
        if seg != "\n\n" and len(seg) > 1:
            if seg in tf:
                tf[seg] += 1
            else:
                tf[seg] = 1

    df = pd.DataFrame(list(tf.items()), columns=['word', 'counts'])
    df = df[df.counts > 100]
    df = df.sort_values(by='counts', ascending=False)
    # print(df)

    list_word = df['word'].tolist()
    # print(list_word)
    return list_word


def gen_word_cloud(num, word_list):
    word_cloud = WordCloud(font_path="SourceHanSerifCN-Regular.otf",
                           background_color="black", width=1920,
                           height=1080, max_words=1500, min_font_size=4).generate(' '.join(word_list))
    word_cloud.to_file(str(num) + '.png')


def gen_word_cloud_file(num, file_name):
    word_list = fenci(file_name)
    gen_word_cloud(num, word_list)


if __name__ == '__main__':
    index = 1
    for item in files:
        gen_word_cloud_file(index, item)
        index += 1
    words = ["Row", "Column", "Index", "delete", "copy", "check", "list", "cell", "next", "all", "fill", "null"]
    gen_word_cloud(index, words)
    print("OK")

