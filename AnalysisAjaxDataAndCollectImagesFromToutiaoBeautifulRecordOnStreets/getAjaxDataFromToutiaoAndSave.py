import requests
from urllib.parse import urlencode
import os

index = 1  # 初始化索引，用于图片名称的唯一标识


def get_page(page_num, offset):
    """
    获取某一页的数据

    :param page_num: 页码
    :param offset: 页面偏移量
    :return: 该页的数据（JSON 格式）
    """
    params = {
        'keyword': '街拍',
        'offset': offset,
        'count': 40,
        'from': 'gallery',
        'page_num': page_num,
        'cur-tab': 1,
        'pd': 'atlas',
        'timestamp': 1561704400000,
        'dvpf': 'pc',
        'source': 'input',
        'action_type': 'search_subtab_switch',
        'rawJSON': 'false',
        'cur_tab_title': 'gallery',
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    try:
        response = requests.get(url)  # 发送 GET 请求获取数据
        if response.status_code == 200:
            with open('test.json', 'w', encoding='utf-8') as f:  # 将数据写入到 test.json 文件中（方便调试）
                f.write(response.text)
            return response.json()  # 返回 JSON 格式的数据
    except requests.ConnectionError:
        return None


def get_images(json_data):
    """
    从 JSON 数据中提取图片链接

    :param json_data: JSON 数据
    :return: 图片链接列表
    """
    if json_data.get('data'):
        data = json_data.get('data')
        rsts = []
        if data and isinstance(data, list):
            for item in data:
                image = item.get('img_url')
                rsts.append(image)
        return rsts


def save_images(rsts):
    """
    保存图片

    :param rsts: 图片链接列表
    """
    global index  # 引入全局变量
    if rsts:
        if not os.path.exists('images'):  # 如果 images 目录不存在，则创建该目录
            os.mkdir('images')
        for result in rsts:
            extensions = ['jpg', 'png', 'gif', 'jpeg', 'JPG', 'JPEG', 'PNG', 'GIF']
            rs_extension = result.split('/')[-1].split('.')[-1]
            if rs_extension in extensions:  # 判断图片格式是否合法
                with open('images/' + 'beautifulGirl' + str(index) + '.' + rs_extension, 'wb') as f:  # 以二进制方式写入图片数据
                    f.write(requests.get(result).content)
                    f.close()
                index += 1
# Path: AnalysisAjaxDataAndCollectImagesFromToutiaoBeautifulRecordOnStreets/getAjaxDataFromToutiaoAndSave.py