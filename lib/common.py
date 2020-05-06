"""
公共方法
"""

# MD5 加密方法

import hashlib
from core import src

# 将密码加密处理
def get_md5(user, pwd):
    md5_object = hashlib.md5()
    md5_object.update(pwd.encode('utf-8'))
    md5_object.update(user.encode('utf-8'))
    md5_str = md5_object.hexdigest()
    print(md5_str)
    return md5_str

# 登录认证装饰器


def login_auth(func):
    from core import src

    def inner(*args, **kwargs):
        if src.user_key.get('token'):
            res = func(*args, **kwargs)
            return res
        else:
            print("请先登录！")
            src.login()

    return inner
