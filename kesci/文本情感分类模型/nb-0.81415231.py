
# coding: utf-8

# In[1]:


import jieba
import pandas as pd
import numpy as np
import sklearn
from matplotlib import pyplot as plt


# In[2]:


train_data = pd.read_csv('train.csv', lineterminator='\n')
test_data = pd.read_csv('test.csv', lineterminator='\n')


# In[3]:


train_data.head(10)


# In[4]:


test_data.head(10)


# In[5]:


train_data['label'] = train_data['label'].map({'Negative':0, 'Positive':1})
test_data['label'] = 0
#a = jieba.cut(train_data['review'][:2].tolist(), )
train_data.head()


# In[8]:


def getBagsOfWord(data):
    vocabSet = set()
    for rec in data['review']:
        vocabSet |= set(list(map(lambda x:x.strip().lower() if len(x.strip().lower()) > 0 else None, jieba.cut(rec))))
    vocabSet.remove(None)
    vocabSet -= set(rmSignal)
    vocabSet = filter(lambda x:not x.isdigit(), vocabSet)
    return vocabSet

def word2Vec(vocabList, ip):
    recVec = [0] * len(vocabList)
    ip = jieba.cut(ip)
    for word in ip:
        word = word.strip().lower()
        if len(word) == 0 or word in rmSignal or word not in vocabList:
            continue

        if word in vocabList:
            recVec[vocabList.index(word)] = 1
        else:
            print("{0} is not in vocabList!".format(word))
    return recVec

def makeDataMat(data, vocabList):
    data_mat = []
    for rec, label in zip(data['review'], data['label']):
        data_mat.append(word2Vec(vocabList, rec) + [label])

    return np.mat(data_mat, dtype=np.double)
        
rmSignal = ['.', '?', '!', ':', '-', '+', '/', '"', ',']    
vocabList = list(getBagsOfWord(train_data))#list(getBagsOfWord(train_data) | getBagsOfWord(test_data))
print(len(vocabList), vocabList[:10])


# In[9]:


#analyse train data
def getCountWords(data, vocabList):
    cntWords = [0] * len(vocabList)
    for rec in data['review']:
        sentence = list(map(lambda x:x.strip().lower() if len(x.strip().lower()) > 0 else None, jieba.cut(rec)))
        for wd in sentence:
            if wd in vocabList:
                cntWords[vocabList.index(wd)] += 1
    cntWords = [(cntWords[i], vocabList[i]) for i in range(len(vocabList))]
    return cntWords

    
cntWords = getCountWords(train_data, vocabList)
cntWords = sorted(cntWords, key=lambda x:x[0])


# In[10]:


def plotTopFrequeceWord(cntWords, topK=10):
    cntWords = sorted(cntWords, key=lambda x:x[0])[-topK:]
    print(cntWords)
    
    plt.bar(list(range(topK)), [x[0] for x in cntWords], align = 'center',color='steelblue', alpha = 0.8)
    plt.ylabel('词频')
    plt.xlabel('词语')
    plt.title('出现最多的前%s个词'%(topK))
    plt.xticks(list(range(topK)), [x[1] for x in cntWords])
    
    # 为每个条形图添加数值标签
    for x,y in enumerate(cntWords):
        plt.text(x, y[0], '%s' %(y[0]), ha='center')


# 中文乱码的处理
plt.rcParams['font.sans-serif'] =['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plotTopFrequeceWord(cntWords, 20)


# In[11]:


testVocabList = list(getBagsOfWord(test_data))
testCntWords = getCountWords(test_data, testVocabList)
plotTopFrequeceWord(testCntWords, 20)


# In[12]:


cntWords = sorted(cntWords, key=lambda x:x[0])
cntWords[:20]


# In[11]:


train_mat = makeDataMat(train_data, vocabList)
cnt = 0
test_mat = makeDataMat(test_data, vocabList)


# In[14]:


test_mat[0, 2343]


# In[15]:


print(train_mat.shape, test_mat.shape)
print("sparsity of train_mat is {0}%\n".format(100. - np.sum(train_mat[:100, :] / train_mat.shape[1])))
print("sparsity of train_mat is {0}%\n".format(100. - np.sum(test_mat[:10, :] / test_mat.shape[1])))


# In[18]:


#use sklearn bayes
'''
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(train_mat[:, :-1], train_mat[:, -1])
y_test = model.predict_proba(test_mat[:, :-1])

print(model.class_prior_)

'''

# In[19]:


y_test[:10, :]


# In[30]:

'''
output = pd.DataFrame(data={"ID":test_data["ID"].tolist(), "Pred":y_test[:, 0]})
output.to_csv('output.csv', index = False, quoting = 3)
'''

# In[16]:


def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = trainMatrix.shape[1]
    pAbusive = sum(trainCategory) / numTrainDocs
    p0Num = np.ones(numWords).reshape(1, -1)
    p1Num = np.ones(numWords).reshape(1, -1)
    p0Denom = 2.
    p1Denom = 2.
    print(trainMatrix.shape, trainCategory.shape, p0Num.shape, numWords)
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num / p1Denom
    p0Vect = p0Num / p0Denom
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = np.sum(np.log(vec2Classify) * p1Vec) + np.log(pClass1)
    p0 = np.sum(np.log(vec2Classify) * p0Vec) + np.log(1-pClass1)
    return 1 if p1 > p0 else 0

def predictNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = np.sum(vec2Classify * p1Vec) + np.log(pClass1)
    p0 = np.sum(vec2Classify * p0Vec) + np.log(1-pClass1)


    return p1 / (p1 + p0) if p1 > 0 else 1-p1 / (p1 + p0)

p0Vect, p1Vect, pAbusive = trainNB0(train_mat[:, :-1], train_mat[:, -1])


# In[17]:


def predictTest():
    for i in range(len(test_mat)):
        test_mat[i][-1] = predictNB(test_mat[i, :-1], p0Vect.transpose(), p1Vect.transpose(), pAbusive)

cnt = 0
test_mat.dtype = np.double
print(p0Vect.shape, p0Vect[:10], pAbusive)
predictTest()


# In[19]:


test_mat[:20, -1], train_mat[:2, -1]


# In[20]:


test_mat[:, -1].reshape(1, -1).tolist()[0]


# In[18]:


output = pd.DataFrame(data={"ID":test_data["ID"].tolist(), "Pred":test_mat[:, -1].reshape(-1).tolist()[0]})
output.to_csv('output.csv', index = False, quoting = 3)
