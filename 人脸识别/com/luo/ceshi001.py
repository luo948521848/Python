import time#用于给每次迭代计时

from PIL import Image #用于读取、resize图片数据

import numpy as np  #数据处理库

from keras import backend  #s深度学习
from keras.models import Model
from keras.applications.vgg16 import VGG16

from scipy.optimize import fmin_l_bfgs_b #求最优值

from scipy.misc import imsave  #用于存储数据图片的数据

#对数据进行预处理
#只能对正方形的图片进行处理

#内容图
height = 512
width = 512

content_image_path = "C:/Users/luo/Desktop/img/3.jpg"
content_image = Image.open(content_image_path)
content_image = content_image.resize(height,width)

#风格图

content_image_path1 = "C:/Users/luo/Desktop/img/5.jpg"
content_image1 = Image.open(content_image_path)
content_image1 = content_image1.resize(height,width)
#将图片拓展到4维  第四维是batch 用于VGG
#内容图
content_array = np.asarray(content_image, dtype='float')
#在坐标一（0）添加维度
content_array = np.extend_dins(content_array, axis=0)


#风格图
style_array = np.asarray(content_image1, dtype='float')
#在坐标一（0）添加维度
style_array = np.extend_dins(style_array, axis=0)


#满足数据输入格式对数据进行转换
content_array[:, :, :, 0] -= 103.939 #减去红的平均值
content_array[:, :, :, 0] -= 116.779 #减去绿的平均值
content_array[:, :, :, 0] -= 123.68  #减去蓝的平均值
content_array = content_array[:, :, :, ::-1] #将数组的倒序排列

style_array[:, :, :, 0] -= 103.939 #减去红的平均值
style_array[:, :, :, 0] -= 116.779 #减去绿的平均值
style_array[:, :, :, 0] -= 123.68  #减去蓝的平均值
style_array = style_array[:, :, :, ::-1] #将数组的倒序排列

#定义一个方向方法 方便对处理完的图形数据进行展示
def deprocess_image(x):
    x = x.reshape((height,width,3))  #对图像进行降维
    x =x[:, :, ::-1]  #再一次倒序
    x[:, :, 0] += 103.939
    x[:, :, 1] += 116.779
    x[:, :, 2] += 123.68
    x = np.clip(x, 0, 255).astype('uint8')
    return x

    #创建3个图像容器   并将三者级联
content_image = backend.variable(content_array)
content_image1 = backend.variable(style_array)
#预留给输出图像
combination_image = backend.placeholder((1, height, width, 3))

input_tensor = backend.concatenate([content_image, content_image1, combination_image], axis=0)



#建立模型
#参数一：输入集 参数二：输入集的方式  参数三：是否进行图像分类
model =VGG16(input_tensor, weigths='imagenet', include_top=False)
#获取模型的每一层
layers = dict([(layer.name, layer.output) for layer in Model.layers])


#定义损失函数
#初始化一些变量
content_weight = 0.025 #内容图占的比例
style_weight = 5.0 #风格图占的比例
total_variation_weight = 1.0#总变异损失的权重
#损失函数的初始化
loss = backend.variable(0.)

#定义内容损失函数   内容图与结果图进行比较
def content_loss(content, combination):
    return backend.sum(backend.square(combination-content))# 求2者的欧式距离  差的平方和

layer_features = layers['block2_conv2'] #选择这种内容特征等级 比较美观
content_image_features = layer_features[0, :, :, :]#0表示样本一 即内容图
conbination_features = layer_features[2, :, :, :]#2表示样本三  即结果图
#内容所占的比例
loss +=content_weight * content_loss(content_image_features, conbination_features)


#定义风格损失函数
#Gram matrix矩阵：通过这个矩阵与相应的特征集合的协方差成比例 ，获取其风格特征
def gram_matrix(x):
    features = backend.batch_flatten(backend.permute_dimensions(x,(2, 0, 1)))
    gram = backend.dot(features, backend.transpose(features))
    return gram
#求matrix的欧式距离
def style_loss(style,combination):
    S = gram_matrix(style)
    C = gram_matrix(combination)
    channels = 3#RGB三通道
    size=height*width
    return backend.sum(backend.square(S-C)/(4.*(channels**2))*(size**2))


    #选择风格特征标准 三个标准苹果都加上
feature_layers = ['block3_conv3', 'block4_conv3', 'block5_conv3']
for layer_name in feature_layers:
    layer_features = layers[layer_name]
    style_features = layer_features[1, :, :, :]#1表示样本二 即风格图
    conbination_features = layer_features[2, :, :, :]#2表示样本三  即结果图
    s1 = style_loss(style_features, conbination_features)
    loss += (style_weight/len(feature_layers))*s1

#为了使结果图更平滑 定义总变异损失
def total_variation_loss(x):
    a = backend.square(x[:, :height-1, :width-1, :]-x[:, 1:, :width-1, :])
    b = backend.square(x[:, :height-1, :width-1, :]-x[:, :height-1, 1:, :])
    return backend.sum(backend.pow(a+b, 1.25))


    #加上总变异损失
loss +=total_variation_weight*total_variation_loss(combination_image)


#利用梯度函数迭代求出最优值 （即输出结果）
#让loss最小
#当梯度趋于0 Y:loss最小  X:是结果图片
grads =backend.gradients(loss,combination_image)
#outputs {[loss, grads]}
outputs = [loss]
outputs += grads

#输入是combination_image 输出是{[loss, grads]}
f_outputs = backend.function([combination_image],outputs)

#用x得到 loss和grads
def eval_loss_and_grads(x):
    x=x.reshape((1, height, width, 3))#转化成4维
    outs = f_outputs([x]) #输出是{[loss, grads]}
    loss_values = outs[0]
    grad_values = outs[1]
    return loss_values, grad_values
#定义一个类一次性获得loss和grade
class Evaluator(object):
    def _init_(self):
        self.loss_value=None
        self.grad_values =None
    #同时得到loss、grad 但只返回loss
    def loss(self, x):
        assert self.loss_value is None
        loss_value, grad_values = eval_loss_and_grads(x)
        return self.loss_value
    #删除loss、grads 返回原来的grads
    def grads(self, x):
        assert self.loss_value is not None
        grad_values = np.copy(self.grad_values) #暂存在本地变量中
        #清空值
        self.loss_value = None
        self.grad_values = None
        return grad_values

evaluator = Evaluator()


#使用优化器获得最优值
x =np.random.uniform(0,255,(1, height, width, 3)) - 128
#迭代十次
interations = 10
for i in range(interations):
    print('开始迭代',i)
    start_time = time.time()
    x, min_val, info =fmin_l_bfgs_b(evaluator.loss, x.flatten(),
                                    fprime=evaluator.grads, maxfun=20)
    print('当前的损失值',min_val)
    img = deprocess_image(x.copy())
    result ='../images/'
    fname=result + 'di%d.png' % i
    imsave(fname, img)
    end_time =time.time()