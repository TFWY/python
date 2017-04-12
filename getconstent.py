#! /usr/bin/env python
# coding=utf-8


import urllib.request
import re
#import importlib

#importlib.reload(sys)
#sys.setdefaultencoding('utf-8')

_page = 3  # 抓取页数


def get_page_html(page):  # 读取指定某页源代码
    html_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&jl=%E9%80%89%E6%8B%A9%E5%9C%B0%E5%8C%BA&isadv=0&sg=6d6d21666daf43f19e6fed6699a25265&p='+str(page)
    html = urllib.request.urlopen(html_url).read()
    return html


def get_url(html):  # 从源代码中解析出url
    pattern_start = re.compile('par="ssidkey=y&amp;ss=409&amp;ff=03" href="')  # url开始标记
    pattern_end = re.compile('" target="_blank"')  # url结束标记
    split1 = pattern_start.split(html.decode('utf-8'))
    global url_save  # 用于存储解析出的url
    url_save = []
    for link in split1[1:-1]:  # 跳过第一段split
        url_get = pattern_end.split(link)
        if re.search('http://jobs.zhaopin.com/', url_get[0]):  # 再次验证结果:
            url_save.append(url_get[0])
    # 无须return，因为url_save已经被global
    return 0


def read_url(url, cnt1, cnt2):  # 读取url内容，写入get_constent.txt
    try:
        constent_all = urllib.request.urlopen(url).read()  # 获取页面源代码
    except:
        constent_all = ''
    finally:
        # 获取信息流
        pattern_strat = re.compile('<ul class="terminal-ul clearfix">')
        #pattern_end = re.compile('</ul>\n <div class="terminalpage-main clearfix">')
        #pattern_strat = re.compile('<!-- SWSStringCutStart -->')
        pattern_end = re.compile('<!-- SWSStringCutEnd -->')
        constent_get = pattern_strat.split(constent_all.decode('utf-8'))
        constent_get = pattern_end.split(constent_get[-1])

        # 将信息流转化为独立的句子,并写入文本

        fw = open('get_constent.txt', 'a')
        fu = open('save_url.txt', 'a')

        if re.search(re.compile('style'), constent_get[0]):
            cnt2 += 1
        else:
            split_pattern = re.compile('<P>|</P>|<p>|</p>|<BR>|<br/>|<br />|<br>')  # 格式化获得的信息
            # 此命令处理句子间格式，或许可以和下文处理句内字符同时进行。此处出于逻辑清晰之虑，分两步进行

            con_0 = re.split(split_pattern, constent_get[0])

            fu.write(url + '\n')
            for line in con_0:
                write_constent = line.replace('&nbsp;', '').replace('\n', '').replace('\r', '').replace('\t','').replace(' ','')
                if len(write_constent):
                    fw.write(write_constent)
            cnt1 += 1
            fw.write('\n')
    return cnt1, cnt2


##-------------------------程序由此开始-------------------------


# 读取url_save，解析其中招聘信息，存储在get_constent.txt中

fc = open('get_constent.txt', 'w')  # 新建get_constent.txt,存储得到的信息。
fc.close()
fu = open('save_url.txt', 'w')
fu.close()

global count1  # 统计解析数据
global count2  # 统计未解析数据
count1 = 0
count2 = 0

for p in range(_page):
    html = get_page_html(p)
    re1 = get_url(html)
    for url in url_save:
        count1, count2 = read_url(url, count1, count2)  # 解析某一url内容

count_text = '共解析 ' + str(count1) + ' 条数据'
count_text2 = '未解析 ' + str(count2) + ' 条有格式数据'
print(count_text)
print(count_text2)
