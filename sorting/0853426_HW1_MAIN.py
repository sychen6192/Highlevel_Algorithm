from MergeSort import mergeSort
from QuickSort import quickSort
from HeapSort import heapSort
from InsertionSort import insertionSort
import time
import sys
import openpyxl
import math

sys.setrecursionlimit(992233720) #這裡設定大一些

sort_fun = input("please input sorting method (merge/quick/heap/insertion):")
n = int(input('please input length of data :'))
nk = str(n//1000)
dict_n = {10000: "B", 20000: "C", 40000: "D"}

for i in range(1, 13):
    pwd = './HW1/'+nk+'k/'+nk+'k'+"{:02d}".format(i)+'.txt'
    print('Reading '+nk+"k{:02d}".format(i)+'.txt'+'....', end='')
    with open(pwd, 'r') as fn:
        data = []
        for line in fn:
            data.append(int(line))
        if sort_fun == 'merge':
            start = time.time()
            mergeSort(data)
            total = time.time() - start
        elif sort_fun == 'quick':
            start = time.time()
            quickSort(data, 0, len(data)-1)
            total = time.time() - start
        elif sort_fun == 'heap':
            start = time.time()
            heapSort(data)
            total = time.time() - start
        elif sort_fun == 'insertion':
            start = time.time()
            insertionSort(data)
            total = time.time() - start
        else:
            print("please input correct method!!!")
        for k in range(0, n-1):
            if data[k] > data[k+1]:
                print("error!")
                break
        print("correct!")
        print("Sorting Time : %dms" % float(1000*total))
        # 開啟檔案
        wb = openpyxl.load_workbook(u'./HW1/學號_HW1_report.xlsx')
        # 設定目前工作的工作表
        ws = wb[sort_fun+' sort result']
        row = dict_n[n] + str(i + 1)
        ws[row] = str(math.floor(1000 * total)) + ' ms'
        wb.save('./HW1/學號_HW1_report.xlsx')