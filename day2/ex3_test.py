# -*- coding: utf-8 -*-
"""
练习3-B：用 unittest 给 max_depth 写单元测试
--------------------------------------------
题目要求：用 unittest 写出至少 5 个测试用例，并执行。

unittest 是 Python 自带的一个"测试框架"（不用装，import 就能用）。
概念上对标 Java 的 JUnit：
    Java  JUnit：  @Test 注解 的方法，一个一个测
    Python unittest： 以 test_ 开头的类方法，一个方法一个用例

三个核心东西：
    1. 测试类要继承 unittest.TestCase
    2. 每个测试方法名必须以 test_ 开头（否则不会被当成测试执行）
    3. 用 self.assertEqual(实际值, 期望值) 来"断言"：两个相等就通过，不等就报错

运行方式（在项目文件夹下开 cmd）：
    D:\Anaconda3\envs\labelme\python.exe -m unittest ex3_test -v
    （-v 表示显示每个用例的详细结果）
"""

import unittest                      # 导入测试框架
import os                            # 处理文件路径
import sys                           # 操作 Python 的模块搜索路径

# —— 关键修复：让 Python 一定能找到同文件夹里的 ex3_max_depth.py ——
# 因为 PyCharm 右键运行时，搜索路径可能只包含项目根 D:\env_test，
# 而 ex3_max_depth.py 在 day2 子文件夹里，所以直接 import 会报 ModuleNotFoundError。
# 解决办法：手动把"本文件所在文件夹"（day2）加到 Python 的搜索路径最前面。
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ex3_max_depth import max_depth  # 导入要测试的函数（现在一定能找到了）

class TestMaxDepth(unittest.TestCase):
    """测试 max_depth 函数的用例组"""

    def test_flat_list(self):
        """用例1：完全扁平的列表，深度应该是 1"""
        self.assertEqual(max_depth([1, 2, 3]), 1)

    def test_nested_example(self):
        """用例2：题目给的标准例子 [[1], [2,[3]]]，深度是 3"""
        self.assertEqual(max_depth([[1], [2, [3]]]), 3)

    def test_empty_list(self):
        """用例3：空列表，深度是 1（本身占一层）"""
        self.assertEqual(max_depth([]), 1)

    def test_single_nested(self):
        """用例4：[[1]]，只套了一层，深度是 2"""
        self.assertEqual(max_depth([[1]]), 2)

    def test_deep_chain(self):
        """用例5：[[[[]]]]，连续套了 4 层，深度是 4"""
        self.assertEqual(max_depth([[[[]]]]), 4)

    def test_very_deep(self):
        """用例6：更深的嵌套，验证递归能一直往下走"""
        self.assertEqual(max_depth([[[]], [1, [2, [3, [4]]]]]), 5)


if __name__ == "__main__":
    # 这句让脚本可以被直接运行：python ex3_test.py
    unittest.main()
