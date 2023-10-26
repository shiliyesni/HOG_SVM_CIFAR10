import matplotlib.pyplot as plt
# 指定保存浮点数的文件名
file_name1 = "../data/svm.txt"
file_name2 = "../data/HOGsvm.txt"
x = [i for i in range(100, 10001, 100)]
# 创建一个空列表以存储读取的浮点数
accuracys1 = []
accuracys2 = []
# 打开文件以读取模式
with open(file_name1, "r") as file:
    # 逐行读取文件，并将每行的内容（浮点数）转换为浮点数类型后添加到列表
    for line in file:
        number = float(line.strip())  # 将每行的内容转换为浮点数并去除换行符
        accuracys1.append(number)

with open(file_name2, "r") as file:
    # 逐行读取文件，并将每行的内容（浮点数）转换为浮点数类型后添加到列表
    for line in file:
        number = float(line.strip())  # 将每行的内容转换为浮点数并去除换行符
        accuracys2.append(number)


print(accuracys1)
print(accuracys2)

plt.rcParams["font.family"] = ["sans-serif"]
plt.rcParams["font.sans-serif"] = ['SimHei']

plt.plot(x, accuracys1, label="SVM", linestyle = '--')
plt.plot(x, accuracys2, label="SVM+HOG")
plt.legend()
plt.xlabel("num_samples")
plt.ylabel("accuracy")
plt.title("不同数量样本值训练准确率",fontproperties="SimHei")
plt.savefig('../accuracys.png')
plt.show()
