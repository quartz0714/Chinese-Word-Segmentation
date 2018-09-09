#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 15:48:16 2018

@author: mazheng
"""

#使用正向最大匹配算法实现中文分词
words_dic = []

def init():
    '''

    读取词典文件
    载入词典
    '''
    
    with open('dic/dic.txt','r',encoding='utf8') as dic_input:
        for word in dic_input:
            words_dic.append(word.strip())         
#实现正向最大匹配算法中的切词方法

def cut_words(raw_sentence,words_dic):
    
    #统计词典中最长的词
    
    max_length = max(len(word) for word in words_dic)
    sentence = raw_sentence.strip()
    
    #统计序列长度
    words_length = len(sentence)
    
    #存储且分好的词语
    cut_word_list = []
    while words_length>0:
        
        max_cut_length = min(max_length,words_length)
        subSentence = sentence[0 : max_cut_length]
        while max_cut_length > 0:
            if subSentence in words_dic:
                cut_word_list.append(subSentence)
                break
            elif max_cut_length ==1:
                cut_word_list.append(subSentence)
                break
            else:
                max_cut_length -= 1
                subSentence = subSentence[0:max_cut_length]
        sentence = sentence[max_cut_length:]
        words_length -= max_cut_length
    words = "/".join(cut_word_list)
    
    return words

def main():
    '''
    与用户交互接口
    :return
    '''
    init()
    while True:
        print('请输入您要分词的序列:')
        input_str = input()
        if not input_str:
            break
        result = cut_words(input_str,words_dic)
        print('分词结果：')
        print(result)
        
        
if __name__ == "__main__":
    main()        
        
        
