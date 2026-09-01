# -*- coding: utf-8 -*-
"""
练习4：User 类 + Admin 继承类
------------------------------
题目要求：
    1. 创建一个 User 类，属性：first_name、last_name；方法：
       - describe_user()：打印用户信息
       - greet_user()：打印问候语
    2. 管理员是一种特殊用户，创建 Admin 类，让它继承 User 类。
       添加属性 privileges（一个存字符串的列表，如 "can add post" 等）。
       添加方法 show_privileges()，显示管理员的权限。
    3. 创建 Admin 实例，调用它的所有方法。

对应 Java 概念：
    - class User  → Java 的 class User
    - def __init__(self, ...) → Java 的构造函数 public User(...)
    - 继承 class Admin(User): → Java 的 class Admin extends User
    - super().__init__(...) → Java 的 super(...) 调用父类构造
    - self 就是 Java 的 this（指向当前对象）
"""

# ---------- 1. 父类 User ----------
class User:
    """普通用户：有姓、有名，能自我介绍和问好"""

    def __init__(self, first_name, last_name):
        """
        构造方法：创建对象时自动调用，用来给属性赋初值。
        self.first_name 表示"这个对象的 first_name 属性"。
        """
        self.first_name = first_name      # 保存名字
        self.last_name = last_name        # 保存姓

    def describe_user(self):
        """打印这个用户的信息"""
        print(f"用户信息：{self.first_name} {self.last_name}")

    def greet_user(self):
        """打印一句问候语"""
        print(f"你好，{self.first_name}！欢迎回来。")


# ---------- 2. 子类 Admin（继承 User） ----------
class Admin(User):
    """管理员：User 的一种特殊类型，额外带权限列表"""

    def __init__(self, first_name, last_name):
        """
        构造方法。子类要先调 super().__init__(...) 初始化父类的属性
        （也就是把 first_name / last_name 设置好），再加自己的属性。
        """
        super().__init__(first_name, last_name)   # 调用父类的构造方法（等价 Java 的 super(...)）
        # 自己的新属性：权限列表
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """打印管理员的权限列表"""
        print(f"管理员 {self.first_name} {self.last_name} 的权限：")
        for p in self.privileges:          # 遍历权限列表，一个个打印
            print(f"  {p}")


# ---------- 3. 主程序：创建实例并调用所有方法 ----------
if __name__ == "__main__":
    # 创建"普通用户"实例并调用它的方法
    u1 = User("小明", "张")
    u1.describe_user()                     # 来自父类
    u1.greet_user()                        # 来自父类
    print()

    # 创建"管理员"实例
    admin = Admin("张三", "李")
    admin.describe_user()                  # 继承来的父类方法
    admin.greet_user()                     # 继承来的父类方法
    admin.show_privileges()                # Admin 自己的方法
