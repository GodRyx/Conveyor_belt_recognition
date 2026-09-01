# -*- coding: utf-8 -*-
"""
练习2-A：用户登录系统
------------------------
题目要求：
    设计一个登录系统，用户名和密码都是预设好的（写死在代码里）。
    用户输入用户名和密码，如果都对就提示"登录成功"并结束；
    如果不对就提示错误，并允许用户继续尝试，最多尝试 N 次（N 自己定）。
    超过 N 次还没成功，就提示"尝试次数过多，账号已锁定"，程序结束。

对应 Java 概念：这个题就是 Java 里经典的 "for + break" 或 "while + 计数" 登录重试。
Python 里我们用 while 循环 + 一个计数器来实现。
"""

# ---------- 1. 预设的"数据库"（写死的账号密码） ----------
# 这里模拟数据库里的正确账号。答辩时可以讲：真实项目这里会换成查询数据库。
USERNAME = "admin"      # 正确的用户名
PASSWORD = "123456"     # 正确的密码
MAX_TRIES = 3           # 最多允许尝试几次（N）

print("===== 欢迎使用登录系统 =====")
print(f"（最多可尝试 {MAX_TRIES} 次，每次输入错误会提示剩余次数）")
print()

# ---------- 2. 循环尝试登录 ----------
tries = 0               # 计数器：已经试了几次

while tries < MAX_TRIES:                     # 条件：还没超过最大次数就继续
    # 每次循环都让用户重新输入
    username = input("请输入用户名：")
    password = input("请输入密码：")

    # 判断用户名和密码是否都正确（and 表示"并且"，两个都对才成立）
    if username == USERNAME and password == PASSWORD:
        print("登录成功！欢迎回来，admin。")
        break                                # break：立刻退出整个 while 循环
    else:
        tries += 1                           # 试错一次，计数器 +1
        remain = MAX_TRIES - tries           # 还剩几次机会
        if remain > 0:
            print(f"用户名或密码错误，还剩 {remain} 次机会。")
            print("-" * 30)
        else:
            # remain 已经是 0，说明这是最后一次还错了
            print("尝试次数过多，账号已锁定！")

print()
print("程序结束。")
