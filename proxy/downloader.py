
import os

url_set = set()

# 文件名前缀
PREFIX = 'file_'


def check_url(url):
    # 可以自己重新写判断逻辑
    return '.m4a' in url


def download(url):
    url = url.strip()
    if url not in url_set:
        url_set.add(url)
        filename = PREFIX + str(len(url_set)).zfill(3) + ".m4a"
        print("Download: {}".format(url))
        os.system("wget \"{}\" -O ../data/{} &".format(url, filename))
