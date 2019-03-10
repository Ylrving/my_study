#coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel('data.xls',header=None)
data1 = data.iloc[:,[15]]
print(data)

print("hello")