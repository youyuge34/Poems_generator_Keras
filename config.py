# *-* coding:utf-8 *-*
'''
@author: ioiogoo
@date: 2018/1/31 19:28
'''


class Config(object):
    poetry_file = 'dataset/poetry.txt'
    weight_file = 'poetry_model.h5'
    # 根据前六个字预测第七个字
    max_len = 6
    batch_size = 32
    learning_rate = 0.001
