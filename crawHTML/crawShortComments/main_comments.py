# -*- coding: utf-8 -*-
import os
import time

import sampleComment



#html资源文件夹
htmls_dir = './html/';
if not os.path.isdir(htmls_dir):
	os.mkdir(htmls_dir)

#要操作的id文件
id_file = './ShortCommentsId-2389939--3264139'
#id_file = './ShortCommentsId-1920713--2389554'

start_time = time.time()


count = 0

while 1:
    returnCode,crawlCount = sampleComment.CrawShortComments(htmls_dir,id_file)
    print 'returnCode is ' + str(returnCode)

    count += crawlCount
    print 'crawl %s, total cost %.2fmin' % (count, (time.time() - start_time) / 60.0)
    if returnCode == 0:
        break;

print 'GoodBye'
