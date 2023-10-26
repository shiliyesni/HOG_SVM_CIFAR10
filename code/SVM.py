import pickle
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import time
accuracys = []
timeer = []
timeer2 = []
# 加载本地CIFAR-10数据集
def load_cifar10_data(data_dir, num_samples):
    train_images = []
    train_labels = []
    test_images = []
    test_labels = []

    for batch in range(1, 6):
        with open(f'{data_dir}/data_batch_{batch}', 'rb') as file:
            batch_data = pickle.load(file, encoding='bytes')
            if num_samples > 0:
                train_images.extend(batch_data[b'data'][:num_samples])
                train_labels.extend(batch_data[b'labels'][:num_samples])
            else:
                train_images.extend(batch_data[b'data'])
                train_labels.extend(batch_data[b'labels'])

    with open(f'{data_dir}/test_batch', 'rb') as file:
        test_data = pickle.load(file, encoding='bytes')
        if num_samples > 0:
            test_images = test_data[b'data'][:num_samples]
            test_labels = test_data[b'labels'][:num_samples]
        else:
            test_images = test_data[b'data']
            test_labels = test_data[b'labels']

    return np.vstack(train_images), np.array(train_labels), test_images, np.array(test_labels)

print(time.time())
data_dir = '../cifar-10-batches-py'  # 指定CIFAR-10数据集的本地目录
for i in range(100, 10001, 100):
    start_time = time.time()
    print(i)
    num_samples = i  # 选择要使用的样本数量
    train_images, train_labels, test_images, test_labels = load_cifar10_data(data_dir, num_samples)

    # 数据预处理和标准化
    scaler = StandardScaler()
    train_images = scaler.fit_transform(train_images)
    test_images = scaler.transform(test_images)

    # PCA降维
    pca = PCA(n_components=64)
    train_images = pca.fit_transform(train_images)
    test_images = pca.transform(test_images)

    # 创建一个SVM分类器
    svm_classifier = SVC()

    # 在训练集上训练SVM分类器
    svm_classifier.fit(train_images, train_labels)

    # 在测试集上进行预测
    test_predictions = svm_classifier.predict(test_images)

    # 计算分类准确度
    accuracys.append(accuracy_score(test_labels, test_predictions))
    end_time = time.time()
    timeer.append(end_time - start_time)
    timeer2.append(end_time)

file1_name = "../data/svm.txt"
file2_name = "../data/svm_time.txt"
file3_name = "../data/svm_time2.txt"
# 打开文件以写入模式
with open(file1_name, "w") as file:
    # 使用循环将浮点数列表的每个元素写入文件
    for number in accuracys:
        file.write(str(number) + "\n")


with open(file2_name, "w") as file:
    # 使用循环将浮点数列表的每个元素写入文件
    for number in timeer:
        file.write(str(number) + "\n")

with open(file3_name, "w") as file:
    # 使用循环将浮点数列表的每个元素写入文件
    for number in timeer2:
        file.write(str(number) + "\n")

print(end_time)
