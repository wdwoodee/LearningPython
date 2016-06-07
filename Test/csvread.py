__author__ = 'dwang'
# -*- coding:utf-8 -*-

import csv

def get_attrbute(filename):
  csvfile = open(filename,'r')
  csvreader = csv.reader(csvfile)
  att_name=[]
  att_value = []
  print(csvreader)
  print(type(csvreader))
  for row in csvreader:
    print(row)
    att_name.append(row[0])
    att_value.append(row[1])
  print(att_name,att_value)
  return (att_name,att_value)

def get_line_attribut(filename):
    line = []
    csvfile = open(filename,"r")
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)
        print(type(row))
        name = row[0]
        value = row[1]
        stock = (name, value)
        line.append(stock)
    print(line)
    return line


file = r"D:\Github\python\test\dev.csv"
get_attrbute(file)
t = get_line_attribut(file)
print(t[0][1])