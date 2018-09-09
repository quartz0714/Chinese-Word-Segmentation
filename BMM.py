



#使用逆向最大匹配算法实现中文分词

words_dic = []

def init():
    """
    读取词典文件
    获取词典
    :return:
    """
    with open("dic/dic.txt","r",encoding="utf-8") as dic_input:
        for word in dic_input:
            words_dic.append(word.strip())


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

    words = "/".join(cut_word_list)
    return words

def main():
    """
    用户交互接口
    :return:
    """
    init()
    while True:
        print("请输入您要分词的序列：")
        input_str = input()
        if not input_str:
            break
        else:
            result = cut_words(input_str,words_dic)

        print("分词结果")
        print(result)


if __name__  == "__main__":
    main()
