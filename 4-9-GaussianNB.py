
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import jieba
from sklearn.naive_bayes import GaussianNB


# In[2]:


df_train = pd.read_csv('data/simplifyweibo_4_moods.csv')


# In[3]:


print(df_train.shape)
df_train.describe()


# In[4]:


df_train.head(10)


# In[5]:


list(jieba.cut(df_train.iloc[2, :]['review']))[:10]


# In[8]:


#获取词典
def getVocabList(data, rmSignal = ['.', '?', '!', ':', '-', '+', '/', '"', ',', '，', '？', '！', ' ', '…']):
    vocabList = set()
    for rec in data['review']:
        vocabList |= set(list(map(lambda x:x.strip().lower() if len(x.strip().lower()) > 0 else None, jieba.cut(rec))))
    
    #删除空串
    vocabList.remove(None)
    #删除指定字符
    vocabList -= set(rmSignal)
    #删除数字
    vocabList = filter(lambda x:not x.isdigit(), vocabList)
    
    return vocabList

#计算词典的词频
def getVocabCnt(data, vocabList):
    vocabCnt = [0] * len(vocabList)
    for rec in data['review']:
        sentences = list(map(lambda x:x.strip().lower() if len(x.strip().lower()) > 0 else None, jieba.cut(rec)))
        for wd in sentences:
            if wd in vocabList:
                vocabCnt[vocabList.index(wd)] += 1
    return vocabCnt

rmSignal = ['.', '?', '!', ':', '-', '+', '/', '"', ',', '，', '？', '！', ' ', '…', '；', '：', '”', '“', '、','~', '。']
rmChinese = ['的', '地', '得', '了', '吧']

#为增加测试速度，只处理部分数据集
select_idx = list(range(1000)) + [x for x in range(251210, 251210+1000)]
test_select_idx = np.random.choice(select_idx, size=(1,300)).tolist()[0]

select_idx = list(filter(lambda x: x not in test_select_idx, select_idx))

vocabList = list(getVocabList(df_train.iloc[select_idx], rmSignal+rmChinese))
vocabCnt = getVocabCnt(df_train.iloc[select_idx], vocabList)


# In[9]:


print(vocabList[:10], vocabCnt[:10])
print(np.sum(vocabCnt))


# In[10]:


def plotTopFrequeceWord(vocabCnt, vocabList, topK=10):
    chVocab = sorted(vocabList, key=lambda x:vocabCnt[vocabList.index(x)])[-topK:]
    cntAllVocab = np.sum(vocabCnt)
    vocabCnt = [vocabCnt[vocabList.index(x)] for x in chVocab]
    print(chVocab, vocabCnt)
    
    plt.bar(list(range(topK)), vocabCnt , align = 'center',color='steelblue', alpha = 0.8)
    plt.ylabel('词频')
    plt.xlabel('词语')
    plt.title('出现最多的前%s个词'%(topK))
    
    # 为每个条形图添加数值标签
    for x,y in enumerate(vocabCnt):
        plt.text(x, y, '%.2f ' %(round(y*100 / cntAllVocab, 2)), ha='center')


# 中文乱码的处理
plt.rcParams['font.sans-serif'] =['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plotTopFrequeceWord(vocabCnt, vocabList, 20)


# In[11]:


def word2Vect(rec, vocabList):
    sentences = list(map(lambda x:x.strip().lower() if len(x.strip().lower()) > 0 else None, jieba.cut(rec)))
    vec = [0] * len(vocabList)
    for wd in sentences:
        if wd in vocabList:
            vec[vocabList.index(wd)] += 1
    
    return vec

def makeDataMat(data, vocabList):
    data_mat = []
    for idx, rec in enumerate(data['review']):
        try:
            tmp = word2Vect(rec, vocabList)
            data_mat.append(tmp)
        except Exception as e:
            print(rec)
            print(data.iloc[idx])
            print()
            print(e)
            break
    return np.mat(data_mat)

train_x = makeDataMat(df_train.iloc[select_idx], vocabList)
train_y = np.mat(df_train.iloc[select_idx]['label'].tolist()).reshape((-1, 1))

test_x = makeDataMat(df_train.iloc[test_select_idx], vocabList)
test_y = np.mat(df_train.iloc[test_select_idx]['label'].tolist()).reshape((-1, 1))


# In[12]:


train_x.shape, train_y.shape


# In[13]:


model = GaussianNB()
model.fit(train_x, train_y)


# In[14]:


model.class_prior_


# In[15]:


sum(train_y)


# In[16]:


model.predict(np.array(word2Vect('这个真的好可爱啊！我超喜欢这里的', vocabList)).reshape(1, -1))


# In[32]:


model.predict(np.array(word2Vect('其实姐只是一个你永远无法超越的传说。', vocabList)).reshape(1, -1))


# In[17]:


set(df_train.iloc[select_idx]['label'].tolist())


# In[23]:


cnt_2 = sum(df_train.iloc[select_idx]['label'].tolist())/2
cnt_1 = len(df_train.iloc[select_idx]['label'].tolist()) - cnt_2
cnt_1, cnt_2


# In[18]:


model.theta_.shape


# In[19]:


model.score(train_x, train_y)


# In[21]:


model.score(test_x, test_y)

