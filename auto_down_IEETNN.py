import urllib.request
import requests
import os
from bs4 import BeautifulSoup
import threading
from get_list0 import *
import time

def getIEETNNPapers(lines,despath,si,ei):
    ff = open(despath+'error.txt', 'a')
    i = si
    llen = len(lines)
    for s in lines[si-1:ei]:
        out_fname = despath+'%04d.pdf' % i
        if os.path.exists(out_fname):
            print(out_fname,'paper exists!')
            i = i+1
            continue
        s = s[:-1]
        res = requests.get(url=s)
        url0 = res.url[:-1]
        urlpath = url0.replace("document/", "stamp/stamp.jsp?tp=&arnumber=")
        if not getUrlPdf(urlpath, i, llen,out_fname,despath):
            ff.write(str(s)+'\n')
        time.sleep(5)
        i = i+1
        # break
    print('all finished!')
    ff.close()

def getUrlPdf(urlpath,i,llen,out_fname,despath):
    try:
        res = requests.get(urlpath)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        news = soup.select('iframe')
        pdf = news[0]['src']
        print(i,'/',llen,':',pdf,' downloading……')
        r = requests.get(pdf)
    except Exception as err:
        print(urlpath, ' error :', err)
        time.sleep(5)
        return False
    with open(out_fname, 'wb') as f2:
        f2.write(r.content)
    print(out_fname,'finish!')
    return True


if __name__ == '__main__':
    ptype = 'IEE-TNN'
    year = '2018'
    name = 'tnn29'
    localDir = createPath('./' + ptype + year + '/')
    lines = open('list_%s.txt' % name).readlines()
    total = len(lines)
    ths = 1
    si = 1
    di = total//ths + 1
    for i in range(ths):
        t = threading.Thread(target=getIEETNNPapers, args=(lines,localDir, si,si+di))
        t.start()
        si = si+di
