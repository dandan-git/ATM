

"""
接口层
"""

from db import db_handler
from lib import common


# 注册接口
def register_interface(user, pwd, balance=1500):
    user_dict = db_handler.select(user)
    if user_dict:
        return False, "用户已存在"
    else:
        # 做注册业务逻辑的处理
        user_info = {
            'user': user,
            'pwd': common.get_md5(user, pwd),
            'flow_list': [],
            'balance': balance,
            'shop_car': {},
            'locked': False  # True
        }

        # 让数据层保存用户信息
        db_handler.save(user_info)
        return True, "注册成功！"


# 登录接口
def login_interface(user, pwd):
    user_dict = db_handler.select(user)
    if not user_dict:
        return False, '用户不存在'
    else:
        if user_dict.get('pwd') == common.get_md5(user, pwd):
            return True, '登录成功'
        # 密码错误
        else:
            return False, '密码错误'


# 查看余额接口
def check_bal_interface(user):
    user_dict = db_handler.select(user)
    return user_dict.get('balance')
