# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 18:08:15 2020

@author: avinash.tiwari
"""

def model_input():
    inputs = tf.placeholder(tf.int32,[None, None], name='input')
    targets = tf.placeholder(tf.int32,[None, None], name='target')
    lr = tf.placeholder(tf.float32, name='learning_rate')
    keep_prob = tf.placeholder(tf.float32, name='keep_prob')
    return inputs,targets, lr,keep_prob