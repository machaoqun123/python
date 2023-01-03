# -*- coding: utf-8 -*-
"""
用于训练网络,很简单,就几行代码.

作者:马超群
时间:2018年3月13日
邮箱:757706439@qq.com
"""

import scipy.io
import random
import net
import numpy as np
import matplotlib.pyplot as plt

# 导入数据;
data = scipy.io.loadmat('data.mat') 
train_label = data['train_label']
train_data = data['train_data']
test_label = data['test_label']
test_data = data['test_data']

#一些相关的重要参数
num_train = 800
lr = 0.1
weight_decay = 0.001
train_batch_size = 100
test_batch_size = 10000

# 创建网络并加载样本
solver = net.net(train_batch_size, lr, weight_decay)
solver.load_sample_and_label_train(train_data, train_label)
solver.load_sample_and_label_test(test_data, test_label)
# 初始化权值;
solver.initial()

# 用于存放训练误差
train_error = np.zeros(num_train)
# 训练
for i in range(num_train):
	print '第', i, '次迭代'
	net.layer.update_method.iteration  = i
	solver.forward_train()
	solver.backward_train()
	solver.update()
	train_error[i] = solver.loss.loss

plt.plot(train_error)
plt.show()
#测试
solver.turn_to_test(test_batch_size)
solver.forward_test()
print '测试样本的识别率为:', solver.loss.accuracy
