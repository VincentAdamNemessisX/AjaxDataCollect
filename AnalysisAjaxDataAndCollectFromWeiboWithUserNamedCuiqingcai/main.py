"""
# File       : main.py
# Time       : 4:13 PM
# Author     : vincent
# version    : python 3.8
# Description:
"""
from getAjaxDataFromWeibo import get_page, parse_page, save_to_mongo

if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json)
        save_to_mongo(results)
# Path: AnalysisAjaxDataAndCollectFromWeiboWithUserNamedCuiqingcai/getAjaxDataFromWeibo.py