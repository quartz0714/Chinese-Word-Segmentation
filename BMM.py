





#实现逆向最大匹配算法中的切词方法
def cut_words(raw_sentence,words_dic):

    #统计词典中词的最长长度
    max_length = max(len(word) for word in words_dic)
    sentence = raw_sentence.strip()

    #统计序列长度
    words_length = len(sentence)

    #切分出来的词语
    cut_word_list = []

    #判断是否需要切词
    while words_length >0:
        max_cut_length = min(words_length,max_length)
        subSentence = sentence[-max_cut_length:]

        while max_cut_length >0:
            if subSentence in words_dic:
                cut_word_list.append(subSentence)
                break
            elif max_cut_length == 1:
                cut_word_list.append(subSentence)
                break
            else:
                max_cut_length -= 1
                subSentence = subSentence[-max_cut_length:]

        sentence = sentence[0:-max_cut_length]
        words_length -= max_cut_length

    cut_word_list.reverse()

    return cut_word_list

