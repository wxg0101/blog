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
title: "Who owns the copyright for an AI generated creative work?"
date: {datetime.now().strftime('%Y-%m-%d')}             # 时间
img: posts/20210420/post8-rembrandt.jpg
tags: [copyright, creativity, neural networks, machine learning, artificial intelligence]
mathjax: yes
category: opinion
author: Armando Maynez
description: "As neural networks are used more and more in the creative process, text, images and even music are now created by AI, but who owns the copyright for those works?"
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