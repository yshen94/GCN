

import jieba
import jieba.analyse
import jieba.posseg as pseg

sentence = '一个超过5000万人关注的大项目，您参加了吗'央视新闻

# 获取分词
seg_list = jieba.cut(sentence, cut_all = False)
print(seg_list)
print(' '.join(seg_list))

"""
"""

words= pseg.cut(sentence)

for word, flag in words:
    print('%s, %s' % (word, flag))

