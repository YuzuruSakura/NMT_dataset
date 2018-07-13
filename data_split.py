import numpy as np

DEV_SIZE = 3000
TEST_SIZE = 3000
X_SIZE = 638789

#X:含label的数据集：分割成训练集和测试集
#test_size:测试集占整个数据集的比例
def DataSplit(X_num=X_SIZE,test_num=TEST_SIZE,dev_num=DEV_SIZE):
    # X_num=X.shape[0]
    # train_index=range(X_num)
    train_index=[]
    for i in range(X_num):
        train_index.append(i)
    test_index=[]
    for i in range(test_num):
        randomIndex=int(np.random.uniform(0,len(train_index)))
        test_index.append(train_index[randomIndex])
        del train_index[randomIndex]
    dev_index=[]
    for i in range(dev_num):
        randomIndex=int(np.random.uniform(0,len(train_index)))
        dev_index.append(train_index[randomIndex])
        del train_index[randomIndex]
    #train,test,dev的index是抽取的数据集X的序号
    # train=X.ix[train_index] 
    # test=X.ix[test_index]
    # dev=X.ix[dev_index]
    return train_index,test_index,dev_index


if __name__ == '__main__':
    
    
    data_src_file = 'europarl-v8.lv-en.lv'
    train_src_file = 'train.src'
    test_src_file = 'test.src'
    dev_src_file = 'dev.src'
    
    f01 = open(data_src_file, 'r', encoding='utf-8').readlines()
    train, test, dev = DataSplit()
    
    f1 = open(train_src_file, 'w',encoding='utf-8')
    for item in train:
        f1.write(f01[item])
    f1.close()

    f2 = open(test_src_file, 'w',encoding='utf-8')
    for item in test:
        f2.write(f01[item])
    f2.close()

    f3 = open(dev_src_file, 'w',encoding='utf-8')
    for item in dev:
        f3.write(f01[item])
    f3.close()


    data_trg_file = 'europarl-v8.lv-en.en'
    train_trg_file = 'train.trg'
    test_trg_file = 'test.trg'
    dev_trg_file = 'dev.trg'

    f02 = open(data_trg_file, 'r', encoding='utf-8').readlines()

    f4 = open(train_trg_file, 'w', encoding='utf-8')
    for item in train:
        f4.write(f02[item])
    f4.close()

    f5 = open(test_trg_file, 'w', encoding='utf-8')
    for item in test:
        f5.write(f02[item])
    f5.close()

    f6 = open(dev_trg_file, 'w', encoding='utf-8')
    for item in dev:
        f6.write(f02[item])
    f6.close()






    