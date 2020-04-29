# 用户视图层
# - 注册

from interface import user_interface


def register():
    while True:
        username = input("请输入用户名：").strip()
        password = input("请输入密码：").strip()
        re_password = input("请确认密码：").strip()
        # 判断密码与确认密码是否一致
        if password == re_password:
            # 密码一致时执行注册接口
            res = user_interface.register_interface(username, password)
            print(res)
            return res  # 两种结果1已存在，2注册成功
        else:
            print("两次密码不一致")


# 登录


def login():
    pass

# - 查看余额
# - 提现功能
# - 还款功能
# - 转账功能
# - 查看流水
# - 购物功能
# - 查看购物车

# 功能字典


func_dic = {
    '1': register,
    '2': login,
    '3': '查看余额',
    '4': '提现功能',
    '5': '还款功能',
    '6': '转账功能',
    '7': '查看流水',
    '8': '购物功能',
    '9': '查看购物车'
}


def user_view():
    while True:
        print("""
        1.注册
        2.登录
        3.查看余额
        4.提现功能
        5.还款功能
        6.转账功能
        7.查看流水
        8.购物功能
        9.查看购物车
        """)

        choice = input("请选择功能：").strip()

        if choice == 'q':
            break

        if choice not in func_dic:
            print("请输入正确编号")
            continue

        func_dic.get(choice)()
