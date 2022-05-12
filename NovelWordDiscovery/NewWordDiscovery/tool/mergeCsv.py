# _*_ coding: utf-8 _*_
"""
Time:     2022/1/18 21:54
Author:   ChenXin
Version:  V 0.1
File:     mergeCsv.py
Describe:  Github link: https://github.com/Chen-X666
"""
# _*_ coding: utf-8 _*_
"""
Time:     2021/11/30 10:26
Author:   ChenXin
Version:  V 0.1
File:     mergeAllCsv.py
Describe:  Github link: https://github.com/Chen-X666
"""
import csv
import glob
import os

import pandas as pd

import datetime

#  当前文件路径 的上层路径
CWD = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

def mergeCsv(inputPath,outputPath):
    #inputfile = str(os.path.dirname(os.getcwd())) + "\\CandidateWordResult\\*.csv"
    print(inputPath)
    #outputfile = str(os.path.dirname(os.getcwd())) + "\\csvProcess\\trainingData4.csv"
    csv_list = glob.glob(inputPath)

    filepath = csv_list[0]
    df = pd.read_csv(filepath,encoding='GBK')
    df = df.to_csv(outputPath, index=False)

    for i in range(1, len(csv_list)):
        print(csv_list[i])
        filepath = csv_list[i]
        df = pd.read_csv(filepath,encoding='GBK',error_bad_lines=False)
        df = df.to_csv(outputPath, index=False, header=False, mode='a+')
    print('finished')

if __name__ == '__main__':
    inputPath = str(os.path.dirname(CWD)) + "\\CandidateWordResult\\*.csv"
    outputPath = str(os.path.dirname(CWD)) + "\\CandidateWord.csv"
    mergeCsv(inputPath,outputPath)