import requests
import re
import urllib

def getHtml(url):
    html = requests.get(url)
    html.content
    return html.content

def getImg(html):
    reg=r'src="(.+?\.jpg)"'
    imgreg=re.compile(reg)
    imglist=imgreg.findall(html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve('http:'+imgurl, '/Users/liwenwen/Desktop/pic/%s.jpg' % x)
        x += 1

if __name__=='__main__':
    html = getHtml('http://jandan.net/pic')
    reg=r'span class="current-comment-page">\[(\d+)\]<'
    pagereg=re.compile(reg)
    page=pagereg.findall(html)[0]
    for i in range(502,int(page)+1):
        print 'http://jandan.net/pic/page-%s' % i
        html2 = getHtml('http://jandan.net/pic/page-%s' % i)
        getImg(html2)


