#building chatbot deep Nlp

import numpy as np
import tensorflow as tf
import re 
import time

lines = open('movie_lines.txt', encoding='utf-8', errors='ignore').read().split("\n")
conversations = open('movie_conversations.txt', encoding='utf-8', errors='ignore').read().split("\n")

id2line = {}
for line in lines:
    _line =  line.split(' +++$+++ ')
    if len(_line) == 5:
        id2line[_line[0]] = _line[4]

conversations_id = []
for conversation in conversations[:-1]:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
    conversations_id.append(_conversation.split(","))
    
    
