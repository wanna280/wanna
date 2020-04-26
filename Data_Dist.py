from nltk.metrics import edit_distance
import numpy as np
import time 

def read_file(length):    #读取文件,length是需要读取的长度
    files = {}
    for i in range(length):
        files[i]=open("./实验一作业/data/{}.txt".format(i+1))
    return files

def split_word(files,arr):  
    #files是读取到文件的句柄，arr是将句柄对应的文件分词
    for i in range(len(files)):
        arr[i] = "{}".format(files[i].read()).split()

def get_distance(str_arr,pos1,pos2):  #str_arr是分词后的数组，pos1和pos2对应数组下标
    Dist = 0                   
    for i in str_arr[pos1]:          #i，j均是列表中的某个单词
        for j in str_arr[pos2]:
            Dist+=edit_distance(i,j)/(len(str_arr[pos1])*len(str_arr[pos2]))  #得到pos1和pos2文件的距离
    return Dist

def get_matrix_of_dist(arr,len1,len2):  
    #返回距离矩阵，arr是需要分词的数组，len1和len2是文件的个数（矩阵的行/列数）
    matrix = np.empty((len1,len2))
    for i in range(len1):
        for j in range(len2):
            matrix[i][j]=get_distance(arr,i,j)
    return matrix

start = time.process_time()
files = read_file(10)       #读取10个文件
files_text = {}
split_word(files,files_text)  #把文件内的内容分词

matrix_dist = get_matrix_of_dist(files_text,10,10)  #返回距离矩阵
print(matrix_dist)

end = time.process_time()
print("运行时间是{}s".format(end-start))