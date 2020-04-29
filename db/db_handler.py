"""
数据层
读取数据
保存数据
"""
from conf import settings
import os
import json


def select(user):
    # 拼接用户文件路径
    user_path = os.path.join(settings.db_path, '{}.json'.format(user))
    # 判断文件是否存在
    if os.path.exists(user_path):
        with open(user_path, 'r', encoding='utf-8') as f:
            user_dic = json.load(f)
        return user_dic
    else:
        return None


def save(user_info):
    # 拼接用户文件路径
    user_path = os.path.join(settings.db_path, '{}.json'.format(user_info.get('user')))
    # 判断文件是否存在
    with open(user_path, 'w', encoding='utf-8') as f:
        json.dump(user_info, f)
        f.flush()



