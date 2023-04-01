"""
# File       : main.py
# Time       : 5:30 PM
# Author     : vincent
# version    : python 3.8
# Description:
"""
from getAjaxDataFromToutiaoAndSave import get_page, get_images, save_images

if __name__ == '__main__':
    for i in range(0, 4):  # 爬取前四页的数据
        json = get_page(i, 10 * i)  # 获取第 i 页的数据
        results = get_images(json)  # 从数据中提取图片链接
        save_images(results)  # 保存图片到本地目录

# Path: AnalysisAjaxDataAndCollectImagesFromToutiaoBeautifulRecordOnStreets/getAjaxDataFromToutiaoAndSave.py