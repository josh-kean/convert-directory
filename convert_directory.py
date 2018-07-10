from os import *
import os
fileDirectory = input("where is this file located? ")
target = input("what part of every file name do you want to change? ")
result = input("what do you want the change to be? ")
#fileConvertTo = input("what do you want to convert the file to? ")

def fileConversion(directory, target, result):
    fileList = []
    newFileList = []
    for dirpath, dirnames, filenames in walk(directory):
        fileList = filenames
    for i in range(len(fileList)):
        newFileList.append(fileList[i].replace(target, result))
        os.rename(directory+"/"+fileList[i], directory+"/"+newFileList[i]) 
        

fileConversion(fileDirectory, target, result)

