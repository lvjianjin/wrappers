# -*- coding: utf-8 -*-
# @Time      : 2021/3/12 15:23
# @Author    : JianjinL
# @eMail     : jianjinlv@163.com
# @File      : __init__.py
# @Software  : PyCharm
# @Dscription: 代码加密装饰器，基于  MD5(CPU序列号 + 主板序列号 + 硬盘序列号)  方法加密。

import wmi
import hashlib
import functools


class Encryption:
    def __init__(self, func):
        self.func = func

    def __get_md5__(self):
        """
        基于CPU、主板、硬盘序列号信息生成硬件MD5码
        :return:
        """
        c = wmi.WMI()
        # 获取CPU序列号
        for cpu in c.Win32_Processor():
            cpu_id = cpu.ProcessorId.strip()
        # 获取主板序列号
        for board in c.Win32_BaseBoard():
            board_id = board.SerialNumber
        # 获取硬盘序列号
        for physical_disk in c.Win32_DiskDrive():
            disk_id = physical_disk.SerialNumber
        # 拼接硬件序列号
        id = cpu_id + board_id + disk_id
        # 硬件信息转MD5码
        m = hashlib.md5()
        m.update(id.encode())
        md5 = m.hexdigest()
        return md5

    def __check__(self, psword):
        """
        测试输入秘钥是否与本机硬件序列号一致。
        :param psword: 秘钥
        :return:
        """
        md5 = self.__get_md5__()
        if psword == md5:
            return True
        else:
            return False

    def __call__(self, *args, **kwargs):
        if
        return self.func(*args, **kwargs)

def check_cpu_board_disk():
    """
    检验CPU、主板、硬盘序列号信息
    :return:
    """
    c = wmi.WMI()
    # 获取CPU序列号
    for cpu in c.Win32_Processor():
        cpu_id = cpu.ProcessorId.strip()
    # 获取主板序列号
    for board in c.Win32_BaseBoard():
        board_id = board.SerialNumber
    # 获取硬盘序列号
    for physical_disk in c.Win32_DiskDrive():
        disk_id = physical_disk.SerialNumber
    # 拼接硬件序列号
    id = cpu_id + board_id + disk_id
    # 硬件信息转MD5码
    m = hashlib.md5()
    m.update(id.encode())
    md5 = m.hexdigest()
    return md5


# def authenticate(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         request = args[0]
#         if check_user_logged_in(request):  # 如果用户处于登录状态
#             return func(*args, **kwargs)  # 执行函数post_comment()
#         else:
#             raise Exception('Authentication failed')
#
#     return wrapper
#
#
# @authenticate
# def post_comment(request, ...)
#     ...


if __name__ == '__main__':
    print(check_cpu_board_disk())

