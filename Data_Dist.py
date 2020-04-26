from nltk.metrics import edit_distance
import numpy as np 

def ReadFile(arr,length):    #读取文件，arr是需要返回的数组，length是需要读取的长度
    for i in range(length):
        arr[i]=open("./实验一作业/data/{}.txt".format(i+1))

def Split_Word(filetext,arr,length):  
    for i in range(length):
        arr[i] = "{}".format(fileText[i].readline()).split()

def GetDistance(str_arr,pos1,pos2):
    Dist = 0                   
    for i in str_arr[pos1]:    #i，j均是列表中的某个单词
        for j in str_arr[pos2]:
            Dist+=edit_distance(i,j)/(len(str_arr[pos1])*len(str_arr[pos2]))
    return Dist

def get_Matrx_or_Dist(arr,len1,len2):
    matrix = np.empty((len1,len2))
    for i in range(len1):
        for j in range(len2):
            matrix[i][j]=GetDistance(arr,i,j)
    return matrix

fileText = {}
arr = {}
ReadFile(fileText,10)
Split_Word(fileText,arr,10)
mat = get_Matrx_or_Dist(arr,10,10)

print(mat)