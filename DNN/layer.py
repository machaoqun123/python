# -*- coding: utf-8 -*-
"""
 在该模块内定义了神经网络的layer,包括数据层/加权层/全连接层/激活函数层/损失函数层;
 具体可以见说明文档

作者: 马超群
时间:2018年3月12日
联系:757706439@qq.com
"""

from __future__ import division
import numpy as np
import random
import update_method
import function_for_layer as ffl

# 一些重要的全局变量的参数:
update_function = update_method.batch_gradient_descent

#下面这两个变量可以在net定义的时候改变它.
weights_decay = 0.01
batch_size = 64 

#定义数据层的类:
class data:
	def __init__(self):
		self.data_sample = 0
		self.data_label = 0
		self.output_sample = 0
		self.output_label = 0
		self.point = 0           #用于记住下一次pull数据的地方;

	def get_data(self, sample, label):   # sample 每一行表示一个样本数据, label的每一行表示一个样本的标签.
		self.data_sample = sample
		self.data_label = label

	def shuffle(self):    # 用于打乱顺序;
		random_sequence = random.sample(np.arange(self.data_sample.shape[0]), self.data_sample.shape[0])
		self.data_sample = self.data_sample[random_sequence]
		self.data_label = self.data_label[random_sequence]

	def pull_data(self):     #把数据推向输出
		start = self.point
		end = start + batch_size
		output_index = np.arange(start, end)
		if end > self.data_sample.shape[0]:
			end = end - self.data_sample.shape[0] 
			output_index = np.append(np.arange(start, self.data_sample.shape[0]), np.arange(0, end))
		self.output_sample = self.data_sample[output_index]
		self.output_label = self.data_label[output_index]
		self.point = end % self.data_sample.shape[0]


#定义全连接层的类

class fully_connected_layer:
	def __init__(self, num_neuron_inputs, num_neuron_outputs):
		self.num_neuron_inputs = num_neuron_inputs
		self.num_neuron_outputs = num_neuron_outputs
		self.inputs = np.zeros((batch_size, num_neuron_inputs))
		self.outputs = np.zeros((batch_size, num_neuron_outputs))
		self.weights = np.zeros((num_neuron_inputs, num_neuron_outputs))
		self.bias = np.zeros(num_neuron_outputs)
		self.weights_previous_direction = np.zeros((num_neuron_inputs, num_neuron_outputs))
		self.bias_previous_direction = np.zeros(num_neuron_outputs)
		self.grad_weights = np.zeros((batch_size, num_neuron_inputs, num_neuron_outputs))
		self.grad_bias = np.zeros((batch_size, num_neuron_outputs))
		self.grad_inputs = np.zeros((batch_size, num_neuron_inputs))
		self.grad_outputs = np.zeros((batch_size,num_neuron_outputs)) 

	def initialize_weights(self):
		self.weights = ffl.xavier(self.num_neuron_inputs, self.num_neuron_outputs)

	# 在正向传播过程中,用于获取输入;
	def get_inputs_for_forward(self, inputs):
		self.inputs = inputs


	def forward(self):
		self.outputs = self.inputs .dot(self.weights) + np.tile(self.bias, (batch_size, 1))

	# 在反向传播过程中,用于获取输入;
	def get_inputs_for_backward(self, grad_outputs):
		self.grad_outputs = grad_outputs 

	def backward(self):
		#求权值的梯度,求得的结果是一个三维的数组,因为有多个样本;
		for i in np.arange(batch_size):
			self.grad_weights[i,:] = np.tile(self.inputs[i,:], (1, 1)).T \
			                         .dot(np.tile(self.grad_outputs[i, :], (1, 1))) + \
									 self.weights * weights_decay
		#求求偏置的梯度;
		self.grad_bias = self.grad_outputs
		#求 输入的梯度;
		self.grad_inputs = self.grad_outputs .dot(self.weights.T)

	def update(self):
		#权值与偏置的更新;
		grad_weights_average = np.mean(self.grad_weights, 0)
		grad_bias_average = np.mean(self.grad_bias, 0)
		(self.weights, self.weights_previous_direction) = update_function(self.weights,
																		grad_weights_average, 
																		self.weights_previous_direction)
		(self.bias, self.bias_previous_direction) = update_function(self.bias,
																		grad_bias_average, 
																		self.bias_previous_direction)

class activation_layer:
	def __init__(self, activation_function_name):
		if activation_function_name == 'sigmoid':
			self.activation_function = ffl.sigmoid
			self.der_activation_function = ffl.der_sigmoid
		elif activation_function_name == 'tanh':
			self.activation_function = ffl.tanh
			self.der_activation_function = ffl.der_tanh
		elif activation_function_name == 'relu':
			self.activation_function = ffl.relu
			self.der_activation_function = ffl.der_relu
		else:
			print '输入的激活函数不对啊'
		self.inputs = 0
		self.outputs = 0
		self.grad_inputs = 0
		self.grad_outputs = 0

	def get_inputs_for_forward(self, inputs):
		self.inputs = inputs

	def forward(self):
		#需要激活函数
		self.outputs = self.activation_function(self.inputs)

	def get_inputs_for_backward(self, grad_outputs):
		self.grad_outputs = grad_outputs 

	def backward(self):
		#需要激活函数的导数
		self.grad_inputs = self.grad_outputs * self.der_activation_function(self.inputs)

class loss_layer:
	def __init__(self, loss_function_name):
		self.inputs = 0
		self.loss = 0
		self.accuracy = 0
		self.label = 0
		self.grad_inputs = 0
		if loss_function_name == 'SoftmaxWithLoss':
			self.loss_function =ffl.softmaxwithloss
			self.der_loss_function =ffl.der_softmaxwithloss
		elif loss_function_name == 'LeastSquareError':
			self.loss_function =ffl.least_square_error
			self.der_loss_function =ffl.der_least_square_error
		else:
			print '输入的损失函数不对吧,别继续了,重新输入吧'
		
	def get_label_for_loss(self, label):
		self.label = label

	def get_inputs_for_loss(self, inputs):
		self.inputs = inputs

	def compute_loss_and_accuracy(self):
		#计算正确率
		if_equal = np.argmax(self.inputs, 1) == np.argmax(self.label, 1)
		self.accuracy = np.sum(if_equal) / batch_size 
		#计算训练误差
		self.loss = self.loss_function(self.inputs, self.label)

	def compute_gradient(self):
		self.grad_inputs = self.der_loss_function(self.inputs, self.label)

