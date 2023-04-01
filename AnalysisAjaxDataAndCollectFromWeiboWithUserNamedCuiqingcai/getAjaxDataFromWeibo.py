"""
# File       : getAjaxDataFromWeibo.py
# Time       : 3:19 PM
# Author     : vincent
# version    : python 3.8
# Description:
"""
from urllib.parse import urlencode
import requests
import pymongo

client = pymongo.MongoClient("mongodb+srv://vincent:ZTXic3344"
                             "@tempcluster.kslgvab.mongodb.net/?retryWrites=true&w=majority")
db = client['test']

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def get_page(page_num):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page_num
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json_data):
    if json_data:
        items = json_data.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            if item.get('text') != "转发微博":
                weibo = {'id': item.get('id'), 'text': item.get('text'), 'attitudes': item.get('attitudes_count'),
                         'comments': item.get('comments_count'), 'reposts': item.get('reposts_count')}
                yield weibo
            else:
                weibo = {'id': item.get('id'), 'text': item.get('retweeted_status').get('text'),
                         'attitudes': item.get('attitudes_count'), 'comments': item.get('comments_count'),
                         'reposts': item.get('reposts_count')}
                yield weibo


def save_to_mongo(result):
    if db['weibo'].insert_many(result):
        print('Saved to Mongo', result)
        return True
    return False