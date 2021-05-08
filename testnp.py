#!/usr/bin/env python3

from np import *
import pytest
import pandas as pd
import sys
import numpy as np

def test_start():
  k=5
  string = 'ATTGA'
  actual_result = start(string)
  expected_result  = [['A', 'T', 'T', 'G', 'A'], ['AT', 'TT', 'TG', 'GA'], ['ATT', 'TTG', 'TGA'], ['ATTG', 'TTGA'], ['ATTGA']]
  assert actual_result == expected_result

def test_get_obs():
  k = 5
  get_list = pd.array([['A', 'T', 'G'], ['AT', 'TT', 'TG', 'GA'], ['ATT', 'TTG', 'TGA'], ['ATTG', 'TTGA'], ['ATTGA' ]])  
  actual_result = get_obs('list')
  expected_result = [1,1,1,1]
  assert actual_result == expected_result

def test_get_pos():
  
  seq = "ATTGA"
  actual_result = get_pos('string')
  expected_result = [4,5,4,3,2,1]
  assert actual_result == expected_result
