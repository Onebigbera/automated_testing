# -*-coding:utf-8 -*-
# File :simple_spider.py
# Author:George
# Date : 2019/10/10
# motto: Someone always give up while someone always try!
"""
    simple spider practice with regex
"""
import re
import urllib
import urllib.request


def load_html(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    return data


def download_images(html):
    regex = r'http://[\S]*jpg'
    pattern = re.compile(regex)
    get_images = re.findall(pattern, repr(html))
    print(get_images)

    num = 1
    for img in get_images:
        image = load_html(img)
        with open(".\photos\{}.jpg".format(num), 'wb') as fb:
            fb.write(image)
            num += 1
    print("Download finished! total {} pictures".format(num-1))


if __name__ == "__main__":
    url = "http://p.weather.com.cn/2017/06/2720826.shtml#p=1"
    data = load_html(url)
    download_images(data)

