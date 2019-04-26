import threading
import requests
import shutil
from lxml import etree
import time
import os
URL = "https://captcha.delorean.codes/u/rickyhan/challenge"
lock = threading.Lock()


def download_file(url, fname):
    with requests.Session() as c:
        url_1 = "http://www.urbtix.hk"
        url_2 = "https://ticket.urbtix.hk/internet/zh_TW/secure/shoppingCart"

        page = c.get(url_1)
        js_version = page.text.split(
            "/internet/css/normalize.min.css?version=")[1][0:13]
        page = c.get(url_2)

    # print(page.raw)
    ##
    # if page.status_code == 200:
    # with open("img.png", 'wb') as f:
    ####            page.raw.decode_content = True
    ####            shutil.copyfileobj(page.raw, f)
    ##
    # print(page.content)
        tree = etree.HTML(page.content)
    ##
    # f = open("a.txt",'wb')
    # f.write(page.raw)
    ##
    # print(page.content)
    ##
        element = tree.xpath("""//*[@id="captchaImage"]""")
        content = etree.tostring(element[0]).decode()
    ##
        content = content.split('"')[3]
    ##
    ##
        src = "https://ticket.urbtix.hk"+content
    # print(src)
    ##
        page = c.get(src, stream=True)
    # with open("my.jpeg",'wb') as f:
    ##        page.raw.decode_content = True
    ##        shutil.copyfileobj(page.raw, f)

        get_10_captcha_json_url = "https://ticket.urbtix.hk/internet/captchaImage/" + \
            str(js_version)+"/inputKey.json"
        page = c.get(get_10_captcha_json_url)
    # array=[]
    ##
    # for i in range(2):
    # array.append([])
    # for j in range(5):
    # array[i].append(0)
    ##
    ##
    # for i in range(2):
    # for j in range(5):
    # array[i][j]=page.text.split('"')[i*5*2+j*2+3]

        key1_1 = (page.text.split('"')[3])
        for i in range(10000):
            get_10_captcha_url = "https://ticket.urbtix.hk/internet/captchaImage/" + \
                str(js_version)+"/"+key1_1+".jpeg"
            page = c.get(get_10_captcha_url, stream=True)
            name = fname+str(i)+".jpeg"
            with open(name, 'wb') as f:
                for chunk in page.iter_content(chunk_size=1024):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                    # f.flush() commented by recommendation from J.F.Sebastian
            with lock:
                pass
        # print fname

    ##    key1_2 = (page.text.split('"')[5])
    ##    key1_3 = (page.text.split('"')[7])
    ##    key1_4 = (page.text.split('"')[9])
    ##    key1_5 = (page.text.split('"')[11])
    ##    key2_1 = (page.text.split('"')[13])
    ##    key2_2 = (page.text.split('"')[15])
    ##    key2_3 = (page.text.split('"')[17])
    ##    key2_4 = (page.text.split('"')[19])
    ##    key2_5 = (page.text.split('"')[21])

    # for i in range(10000):
    ##            captcha_dir = "./1/"+str(i)+".jpeg"
    # get_10_captcha_url="https://ticket.urbtix.hk/internet/captchaImage/"+str(js_version)+"/"+key1_1+".jpeg"
    ##            page = c.get(get_10_captcha_url, stream=True)
    # with open(captcha_dir,'wb') as f:
    ##                page.raw.decode_content = True
    ##                shutil.copyfileobj(page.raw, f)

    # print(key1_1)
    # print(key1_2)
    # print(key1_3)
    # print(key1_4)
    # print(key1_5)
    # print(key2_1)
    # print(key2_2)
    # print(key2_3)
    # print(key2_4)
    # print(key2_5)

            # print(page.headers)
ts = []
for i in range(16):
    fname = "1/"+str(i)+"/"
    if not os.path.exists(fname):
        os.makedirs(fname)
    t = threading.Thread(target=download_file, args=(URL, fname))
    ts.append(t)
    t.start()
    time.sleep(0.5)
for t in ts:
    t.join()
print("Done")
