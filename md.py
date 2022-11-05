import os
from datetime import datetime
import argparse
import time

datetime.now().strftime('%Y-%m-%d')
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name",type=str,required=True,help="文件名")
    args=parser.parse_args()
    return args

if __name__=="__main__":
    args=get_args()
    filename = datetime.now().strftime('%Y-%m-%d')+"-"+args.name+".md"
    filename = os.path.join('D:\\Desktop\\blog\\_posts', filename)
    f =  open(filename, "w",encoding='utf-8')
    f.write(
        f"""---
layout: post
read_time: true
show_date: true
title: "my title"
date: {datetime.now().strftime('%Y-%m-%d')}             # 时间
img: posts/20210420/post8-rembrandt.jpg
tags: [artificial intelligence]
mathjax: yes
category: opinion
author: Xingguang
description: "my doc"
---

## Hey
>这是我的第一篇博客。

进入你的博客主页，新的文章将会出现在你的主页上.

 <!--more-->
        """
        )
    f.close()
    time.sleep(3)
    os.system('D:\\programdata\\Typora\\Typora.exe {}'.format(
        filename))