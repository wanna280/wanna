from nltk.metrics import edit_distance
import numpy as np 

def ReadFile(length):    #读取文件,length是需要读取的长度
    files = {}
    for i in range(length):
        files[i]=open("./实验一作业/data/{}.txt".format(i+1))
    return files

def Split_Word(files,arr,length):  
    #files是读取到文件的句柄，arr是将句柄对应的文件分词，length是长度（句柄的个数)
    for i in range(length):
        arr[i] = "{}".format(files[i].read()).split()

def getDistance(str_arr,pos1,pos2):  #str_arr是分词后的数组，pos1和pos2对应数组下标
    Dist = 0                   
    for i in str_arr[pos1]:          #i，j均是列表中的某个单词
        for j in str_arr[pos2]:
            Dist+=edit_distance(i,j)/(len(str_arr[pos1])*len(str_arr[pos2]))  #得到pos1和pos2文件的距离
    return Dist

def get_Matrx_of_Dist(arr,len1,len2):  
    #返回距离矩阵，arr是需要分词的数组，len1和len2是文件的个数（矩阵的行/列数）
    matrix = np.empty((len1,len2))
    for i in range(len1):
        for j in range(len2):
            matrix[i][j]=getDistance(arr,i,j)
    return matrix

files = ReadFile(10)       #读取10个文件
files_text = {}
Split_Word(files,files_text,10)  #把文件内的内容分词
matrix_dist = get_Matrx_of_Dist(files_text,10,10)  #返回距离矩阵
dist = getDistance(files_text,0,1)
print(dist)
# print(matrix_dist)