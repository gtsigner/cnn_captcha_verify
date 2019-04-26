# coding:utf-8

# 处理图片
import os
import uuid
import hashlib

fileDir = './sample/origin'
images = os.listdir(fileDir)


def fuck_md5(sr):
    return hashlib.md5(sr.encode(encoding="UTF-8")).hexdigest()


for img in images:
    imgDir = '%s/%s' % (fileDir, img)
    if not os.path.isdir(imgDir):
        continue
    tag_name = img.replace('_', '')
    # print(tag_name)
    files = os.listdir(imgDir)
    for fl in files:
        filename = '%s/%s' % (imgDir, fl)
        # hashname = hash(tag_name + fl)
        uidstr = fuck_md5(str(uuid.uuid1()) + filename)
        dstname = '%s/%s_%s.jpeg' % (fileDir, tag_name, uidstr)
        print(filename, dstname)
        os.rename(filename, dstname)
