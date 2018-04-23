# -*- coding: utf-8 -*-
import json
import pickle
import csv
import string


def main(filename):
   t=open(filename)
   lines=t.readlines()
   all_words = []
   for line in lines:
     words=line.split()
     for ele in words:
       ele = ele.strip(string.punctuation) 
       if ele!='':
         all_words.append(ele)
   counter = {}
   for ele in all_words:
     if ele in counter:
       counter[ele]=counter[ele]+1
     if ele not in counter:
       counter.update({ele:1})
   counters=sorted(counter.items(), key=lambda x: x[1],reverse=True)
   counters=dict(counters)
   with open('wordcount.csv', 'w', newline='') as csv_file:
     writer = csv.writer(csv_file,delimiter=",")
     writer.writerow(['word']+['count'])
     for ele in counters:
       writer.writerow([ele]+[counters[ele]])
   with open("wordcount.json",'w') as json_file:
     json.dump(counters,json_file)
   with open("wordcount.pkl","wb") as pkl_file:
     pickle.dump(counters, pkl_file)

main("i_have_a_dream.txt")

if __name__ == '__main__':
   main("i_have_a_dream.txt")

