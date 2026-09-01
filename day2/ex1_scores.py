# -*- coding: utf-8 -*-
"""
Day2 练习1：用 列表 + 字典 表示一个班的期末考试成绩
求：单科第一名 / 总分第一名 / 挂科名单

运行方式：PyCharm 里打开本文件，右键 -> Run
知识点：列表、字典、for 循环、if 判断、len()、f-string
"""


students = [
    {"学号": "2026001", "姓名": "张三", "班级": "软件1班", "高数": 85, "英语": 72, "Java编程": 90},
    {"学号": "2026002", "姓名": "李四", "班级": "软件1班", "高数": 58, "英语": 66, "Java编程": 75},
    {"学号": "2026003", "姓名": "王五", "班级": "软件2班", "高数": 92, "英语": 88, "Java编程": 64},
    {"学号": "2026004", "姓名": "赵六", "班级": "软件2班", "高数": 45, "英语": 55, "Java编程": 59},
    {"学号": "2026005", "姓名": "钱七", "班级": "软件1班", "高数": 78, "英语": 95, "Java编程": 82},
]

subjects = ["高数", "英语", "Java编程"]   # 要统计的科目，也是一个列表
PASS_LINE = 60

print(f"全班共 {len(students)} 名学生，科目：{subjects}")   # len() 取列表长度


print("=" * 40)
print("【单科第一名】")
for subject in subjects:            # 外层：一门一门课来
    best = students[0]              # 先假设列表里第 0 个学生是第一名
    for stu in students:            # 内层：遍历每个学生（类似 Java 的增强 for）
        if stu[subject] > best[subject]:   # 字典用[键]取值，如 stu["高数"]
            best = stu                    # 分数更高 -> 更新第一名
    print(f"  {subject} 第一名：{best['姓名']}（{best[subject]} 分）")

# ========== 第 3 步：求总分第一名 ==========
print("=" * 40)
best_student = students[0]     # 记住总分最高的"人"
best_total = 0                 # 记住最高的总分

for stu in students:
    total = 0                  # 每个学生从 0 开始累加
    for subject in subjects:   # 三门课的分数一个个加起来
        total = total + stu[subject]
    if total > best_total:     # 比目前最高分还高 -> 换人
        best_total = total
        best_student = stu

print(f"【总分第一名】{best_student['姓名']}，{best_total} 分")

# ========== 第 4 步：挂科名单 ==========
print("=" * 40)
print("【挂科名单】")
found = False                       # 旗帜变量：有没有人挂科
for stu in students:
    failed = []                     # 存这个学生挂掉的科目名
    for subject in subjects:
        if stu[subject] < PASS_LINE:
            failed.append(subject)  # append() 往列表末尾添加元素
    if len(failed) > 0:             # 挂科科目数 > 0 就是有挂科
        found = True
        print(f"  {stu['姓名']}（{stu['学号']}）：挂了 {failed} 科目")

if not found:
    print("  好消息：没有人挂科！")
