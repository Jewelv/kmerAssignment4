#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import argparse

def unique(ary):
  list = []
  i=0
  x= np.array(ary)
  for i in range(len(x[i])):
   list.append(np.unique(x[i]))
  return list

def window(string):
  j = []
  k = 0
  l = 1
  while k < len(string) + 1:
    d = [string[i:i+k] for i in range(len(string)-l+1)]
    j.append(d)
    k+=1
    l+=1
  return j

def get_obs(list):
  get_list = []
  for x_list in list:
    print(x_list)
    counter = len(x_list)
    get_list.append(counter)
  return get_list

def get_pos(string):
  j= []
  k=1
  n=0
  l=0
  x = len(string)
  while k < x+1:
   n= x - k +1
   l= 4**k
   if n < l:
    j.append(n)
   elif n==l:
    j.append(n)
   else:
    j.append(l)
   n=0
   l=0
   k+=1
  return j

def get_df(string,get_list,pos):
  kmer = []
  for i in range(1,len(string)+1):
    kmer.append(i)
  df = pd.DataFrame(list(zip(kmer,get_list,pos)), columns = ['k','Obs', 'Pos'])
  df.at['total','Obs'] = df['Obs'].sum()
  df.at['total','Pos'] = df['Pos'].sum()
  return df

def get_lc(df):
  lc = df['Obs'].sum()/df['Pos'].sum()
  return lc
  



def main(args):
  fn = open("dna.txt","r+")
  file = [seq.strip() for seq in fn]
  for seq in file:
    ary = window(seq)
    ary.pop(0)
    list =unique(ary)
    get_list = get_obs(list)
    pos = get_pos(seq)
    df1 = get_df(seq,get_list,pos)
    df2 = df1['Obs'].sum()/df1['Pos'].sum()
    #lc = get_lc(df)
    print(df1)
    print(df2)
    f= open("kmerAssignmentOutput.txt", 'a')
    f.write(str(df1)+ str(df2)+' ')
    f.close()
  fn.close()


if __name__ == '__main__': 
  parser = argparse.ArgumentParser()
  parser.add_argument('dna', type=argparse.FileType('r'))
  #parser.add_argument('kmer', type = int)
  args = parser.parse_args()
  main(args)

