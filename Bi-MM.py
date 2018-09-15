import FMM
import BMM


# 使用双向最大匹配算法实现中文分词
words_dic = []


def init():
    '''

    读取词典文件
    载入词典
    '''

    with open('dic/dic.txt', 'r', encoding='utf8') as dic_input:
        for word in dic_input:
            words_dic.append(word.strip())
        # 实现正向最大匹配算法中的切词方法


def cut_words(raw_sentence, words_dic):
    bmm_word_list = BMM.cut_words(raw_sentence,words_dic)
    fmm_word_list = FMM.cut_words(raw_sentence,words_dic)
    bmm_word_list_size = len(bmm_word_list)
    fmm_word_list_size = len(fmm_word_list)
    if bmm_word_list_size != fmm_word_list_size:
        if bmm_word_list_size <= fmm_word_list_size:
            return bmm_word_list
        else:
            return fmm_word_list
    else:
        FSingle = 0
        BSingle = 0
        isSame = True
        for i in range(bmm_word_list_size):
            if fmm_word_list[i] not in bmm_word_list:
                isSame = False
            if len(fmm_word_list[i]) == 1:
                FSingle += 1
            if len(bmm_word_list[i]) == 1:
                BSingle += 1
        if isSame == True:
            return fmm_word_list
        else:
            if FSingle < BSingle:
                return fmm_word_list
            else:
                return bmm_word_list


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
        print()

        result1 = FMM.cut_words(input_str, words_dic)
        result1 = "/".join(result1)
        print('正向最大匹配分词结果：')
        print(result1)
        print()

        result2 = BMM.cut_words(input_str, words_dic)
        result2 = "/".join(result2)
        print('逆向最大匹配分词结果：')
        print(result2)
        print()

        result3 = cut_words(input_str, words_dic)
        result3 = "/".join(result3)
        print('双向最大匹配分词结果：')
        print(result3)

if __name__ == "__main__":
    main()
