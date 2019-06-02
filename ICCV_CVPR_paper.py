# coding:utf-8
import re
import requests
import urllib
import os
import threading
import pdb
import os

def getIJCAIPapers(minnum,maxnum):
    url = 'https://www.ijcai.org/proceedings/2018/%04d.pdf'
    # maxnum = 870
    ctype = 'IJCAI'
    year = '2018'
    localDir = 'E:\\' + ctype + year + '\\'
    for i in range(minnum,maxnum+1):
        urlpath = url % (i)
        file_path = localDir+'%04d.pdf'% (i)
        if not os.path.exists(file_path):
        	os.makedirs(file_path)
        print('[' + str(i) + '/' + str(maxnum) + "]  Downloading -> " + file_path)
        try:
            urllib.request.urlretrieve(urlpath, file_path)
        except Exception as err:
            print(urlpath,' error :',err)
            continue
    print("all download finished")

def get_CVPR_ICCV_Papers():
    ctype = 'ICCV'
    year = '2017'
    # get web context
    r = requests.get('http://openaccess.thecvf.com/'+ctype+year+'.py')
    data = r.text
    # find all pdf links
    link_list = re.findall(r"(?<=href=\").+?pdf(?=\">pdf)|(?<=href=\').+?pdf(?=\">pdf)" ,data)
    name_list = re.findall(r"(?<=href=\").+?'+year+'_paper.html\">.+?</a>" ,data)
    cnt = 0
    num = len(link_list)
    # your local path to download pdf files
    localDir = 'D:\\'+ctype+year+'\\'
    if not os.path.exists(localDir):
        os.makedirs(localDir)
    while cnt < num:
        url = link_list[cnt]
        # seperate file name from url links
        file_name = link_list[cnt].split('/')[-1]
        # to avoid some illegal punctuation in file name
        # file_name = file_name.replace(':','_')
        # file_name = file_name.replace('\"','_')
        # file_name = file_name.replace('?','_')
        # file_name = file_name.replace('/','_')
        file_path = localDir + file_name + '.pdf'
        # download pdf files
        print('['+str(cnt)+'/'+str(num)+"]  Downloading -> "+file_path)
        try:
            urllib.request.urlretrieve('http://openaccess.thecvf.com/'+url,file_path)
        except Exception as err:
            print(err)
            continue
        cnt = cnt + 1
    print("all download finished")

if __name__ == '__main__':
    threads = []
    t1 = threading.Thread(target=getIJCAIPapers, args=(1,400,))
    threads.append(t1)
    t2 = threading.Thread(target=getIJCAIPapers, args=(401,870,))
    threads.append(t2)
    for t in threads:
        t.start()