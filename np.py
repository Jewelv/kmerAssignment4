#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import argparse

def unique(ary):
  linr = []
  i=0
  x= np.array(ary)
  for i in range(len(x[i])):
   linr.append(np.unique(x[i]))
  return linr

def window(string):
  j = []
  k = 0
  l = 0
  while k < len(string) + 1:
    d = [string[i:i+k] for i in range(len(string)-l+1)]
    j.append(d)
    k+=1
    l+=1
  return j

def get_obs(linr):
  get_linr = []
  for x_linr in linr:
    print(x_linr)
    counter = len(x_linr)
    get_linr.append(counter)
  return get_linr

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

def get_df(string,get_linr,pos):
  kmer = []
  for i in range(1,len(string)+1):
    kmer.append(i)
  df = pd.DataFrame(linr(zip(kmer,get_linr,pos)), columns = ['k','Obs', 'Pos'])
  df.at['total','Obs'] = df['Obs'].sum()
  df.at['total','Pos'] = df['Pos'].sum()
  return df

def get_lc(df):
  lc = df['Obs'].sum()/df['Pos'].sum()
  return lc

def main():
  fn = open("dna.txt","r+")
  file = [seq.strip() for seq in fn]
  for seq in file:
    ary = window(seq)
    ary.pop(0)
    linr =unique(ary)
    get_linr = get_obs(linr)
    pos = get_pos(seq)
    df1 = get_df(seq,get_linr,pos)
    df2 = df1['Obs'].sum()/df1['Pos'].sum()
    print(df1)
    print(df2)
    f= open("kmerAssignmentOutput.txt", 'a')
    f.write(str(df1)+ str(df2)+' ')
    f.close()
  fn.close()
main()
