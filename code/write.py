# 创建一个浮点数列表
float_list = [0.1, 0.2, 0.3, 0.4, 0.5]

# 指定要保存的文件名
file_name = "float_list.txt"

# 打开文件以写入模式
with open(file_name, "w") as file:
    # 使用循环将浮点数列表的每个元素写入文件
    for number in float_list:
        file.write(str(number) + "\n")
