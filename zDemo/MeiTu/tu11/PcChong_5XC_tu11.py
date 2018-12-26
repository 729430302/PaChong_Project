from bs4 import BeautifulSoup
import requests,threading
import re
import time

IP = '211.20.200.38:3128'
UA = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1'
header = {'User-Agent': UA}
              # 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
# url = 'http://www.tu11.com/qingchunmeinvxiezhen/list_4_1.html'
# url1 = 'http://www.tu11.com/qingchunmeinvxiezhen/2018/14220.html'
proxies = {'http': IP}
# 获取也没html内容
def get_response(url):
    res = requests.get(url=url, verify=False,
                       # headers=header,
                       # proxies=proxies
                       )
    response = res.content
    return response

# 解析首页HMTL内容，并获取所有二级html地址
def get_htmls(response):
    soup = BeautifulSoup(response, 'html.parser', from_encoding='gbk')
    # html1 = soup.find_all('a', href=re.compile(r'/qingchunmeinvxiezhen/\d+/\d+\.html'))  # 获取所有的html
    htmls = soup.find_all('a', class_='leibie')  # 获取所有的html
    return htmls

# 解析二级页面HMTL内容，并获取所有图片地址
def get_imgs(html):
    soup = BeautifulSoup(html, 'html.parser', from_encoding='gbk')
    imgs = soup.find_all('img', src=re.compile(r'/picture/\d+/\w+/\d\.jpg'))  # 获取所有的img
    # imgs = soup.find_all('a', class_='nry')
    return imgs

# 解析二级页面HMTL内容，并获取所有html地址
def get_html(html, url):
    soup = BeautifulSoup(html, 'html.parser', from_encoding='gbk')
    # http://www.tu11.com/qingchunmeinvxiezhen/2018/
    str_num1 = url[46:-5]  # 拿到14220
    # print(str_num)
    str_num2 = url[:-10]  # 拿到http://www.tu11.com/qingchunmeinvxiezhen/2018/

    try:
        html = soup.find_all('a', href=re.compile(str_num1 + r'_\d\.html'))  # 获取所有的img

    except:
        html = ''
    return html, str_num2


def for_list_01(htmls):
    for html in htmls:
        html_url = 'http://www.tu11.com' + html['href']
        html = get_response(html_url)
        imgs = get_imgs(html)
        for_list_02(imgs)

def for_list_02(imgs):
    for img in imgs:
        img_url = img['src']
        img = get_response(img_url)
        name = img_url.replace('\\', '')  # 取消字符串中所有的反斜杠\
        name = name.replace('/', '')
        name = name.replace(':', '')
        save_img(img, name)

def save_img(img, name):
    with open('G:\PaChong\A11\ %s.jpg' % name, 'wb') as f:
        f.write(img)

def main(num1, num2):
    for i in range(num1, num2):
        url = 'http://www.tu11.com/qingchunmeinvxiezhen/list_4_' + str(i) + '.html'
        response = get_response(url)
        htmls = get_htmls(response)
        for_list_01(htmls)
        # try:
        #     for_list_01(htmls)
        # except:
        #     print('没有获取到元素')


if __name__ == '__main__':
    mthread1 = threading.Thread(target=main, args=(1, 8))
    mthread2 = threading.Thread(target=main, args=(9, 16))
    mthread3 = threading.Thread(target=main, args=(17, 24))
    mthread4 = threading.Thread(target=main, args=(25, 32))
    mthread5 = threading.Thread(target=main, args=(33, 37))
    # 启动刚刚创建的线程
    mthread1.start()
    mthread2.start()
    mthread3.start()
    mthread4.start()
    mthread5.start()



#获取地址
#获取图片
#下载图片
#判读地址是否有
    # 获取图片
    #下载图片
