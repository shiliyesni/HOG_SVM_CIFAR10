from matplotlib import pyplot as plt
x = range(100,10001,100)

file_name = "data/svm.txt"

# 创建一个空列表以存储读取的浮点数
float_list = []

# 打开文件以读取模式
with open(file_name, "r") as file:
    # 逐行读取文件，并将每行的内容（浮点数）转换为浮点数类型后添加到列表
    for line in file:
        number = float(line.strip())  # 将每行的内容转换为浮点数并去除换行符
        float_list.append(number)

# 现在，float_list 包含了从文件中读取的浮点数列表
# print(float_list)

#绘图
plt.plot(x,float_list)
#展示图形
plt.show()