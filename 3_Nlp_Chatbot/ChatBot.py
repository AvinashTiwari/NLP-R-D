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
    
    
questions = []
answers = []
for conversation in conversations_id:
    for i in range(len(conversation) - 1):
        questions.append(id2line[conversation[i]])
        answers.append(id2line[conversation[i + 1]])


def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "what is", text)         
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"\'ll", "will", text)
    text = re.sub(r"\'ve", "have", text)
    text = re.sub(r"\'re", "are", text)
    text = re.sub(r"\'d", "would", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot ", text)
    text = re.sub(r"[-()\"/@;:<>{}+=~|.?,]", "", text)
    return text


clean_questions =[]
for question in questions:
    clean_questions.append(clean_text(question))

clean_answers = []
for answer in answers:
    clean_answers.append(clean_text(answer))
    

word2count = {}
for question in clean_questions:
    for word in question.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1
            
for answer in clean_answers:
    for word in answer.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1

threshold = 20
questionwords2int = {}
word_number = 0
for word , count in word2count.items():
    if count >= threshold:
        questionwords2int[word]  = word_number
        word_number +=1
        
        
answerwords2int = {}
word_number = 0
for word , count in word2count.items():
    if count >= threshold:
        answerwords2int[word]  = word_number
        word_number +=1

        
    
tokens = ['<PAD>', 'EOS', '<OUT>', '<SOS>']
for token in tokens:
    questionwords2int[token] = len(questionwords2int) + 1
for token in tokens:
    answerwords2int[token] = len(answerwords2int) + 1
    
answersints2word  = {w_i: w for w,w_i in answerwords2int.items()}
