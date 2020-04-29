

"""
接口层
"""

from db import db_handler

# 注册接口


def register_interface(user, pwd, balance=1500):
    user_dict = db_handler.select(user)
    if user_dict:
        return False, "用户已存在"
    else:
        # 做注册业务逻辑的处理
        user_info = {
            'user': user,
            'pwd': pwd,
            'flow_list': [],
            'balance': balance,
            'shop_car': {},
            'locked': False  # True
        }

        # 让数据层保存用户信息
        db_handler.save(user_info)
        return True, "注册成功！"
