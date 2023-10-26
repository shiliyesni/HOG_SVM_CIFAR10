import matplotlib.pyplot as plt

# 指定保存浮点数的文件名
file_name1 = "svm_time.txt"

# 创建一个空列表以存储读取的浮点数
accuracys1 = []

# 打开文件以读取模式
with open(file_name1, "r") as file:
    for line in file:
        numbers_str = line.strip().strip('[]').split(', ')  # 去除方括号并按逗号分割成字符串列表
        numbers = [float(num) for num in numbers_str]  # 转换为浮点数列表
        accuracys1.extend(numbers)  # 将浮点数添加到列表中

print(accuracys1)

# 指定要保存的文件名
file_name = "SVM_time.txt"

# 打开文件以写入模式
with open(file_name, "w") as file:
    # 使用循循环将浮点数列表的每个元素写入文件
    for number in accuracys1:
        file.write(str(number) + "\n")
