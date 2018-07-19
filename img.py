# -*- coding: utf-8 -*-
from wordcloud import WordCloud
filename = "红楼梦.txt"

def read_text(file_name):
    a = []
    f = open(file_name,'r+',encoding='utf-8')
    for item in f.readlines():
        w = item.replace("\n", "")
        a.append(w)
    return a


wordcloud = WordCloud(font_path="FZYTK.TTF",
                          background_color="black", width=1280,
                          height=720, max_words=50,min_font_size=8).generate(' '.join(read_text(filename)))
image = wordcloud.to_image()
wordcloud.to_file(r'1.jpg')
image.show()