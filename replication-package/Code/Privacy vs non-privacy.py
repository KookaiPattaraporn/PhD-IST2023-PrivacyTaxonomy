#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import sklearn
import scipy
import pingouin as pg
from scipy.stats import ranksums
from scipy.stats import mannwhitneyu
from scipy.stats import ttest_ind
from scipy.stats import wilcoxon
from sklearn import preprocessing

def read_input(filepath):
    data = pd.read_csv(filepath)
    return data

def cal_ranksums(data1, data2):
    result = ranksums(data1, data2)
    return result

def cal_pg_ranksums(data1, data2, tail):
    result = pg.mwu(data1, data2, tail)
    return result

data_moodle_nonp = read_input('replication-package/Data/Moodle-sample-nonprivacy.csv')
data_moodle_pri = read_input('replication-package/Data/Moodle-sample-privacy.csv')

data_chrome_nonp = read_input('replication-package/Data/Chrome-sample-nonprivacy.csv')
data_chrome_pri = read_input('replication-package/Data/Chrome-sample-privacy.csv')

'''Calculate the Wilxocon rank-sum test (pengouin lib) to get effect size (CLES) - one-sided'''
res_moodle_fixing_1side = pg.mwu(data_moodle_nonp['DateDiff(Days)'], data_moodle_pri['DateDiff (days)'],tail='one-sided')
res_chrome_fixing_1side = pg.mwu(data_chrome_nonp['DateDiff (days)'], data_chrome_pri['DateDiff (days)'],tail='one-sided')

res_moodle_comments_1side = pg.mwu(data_moodle_nonp['#Comments'], data_moodle_pri['#Comments'],tail='one-sided')
res_chrome_comments_1side = pg.mwu(data_chrome_nonp['#Comments'], data_chrome_pri['#Comments'],tail='one-sided')

print("\n The result of pq ranksums test - moodle - fixing time - one-sided: \n", res_moodle_fixing_1side)
print("\n The result of pq ranksums test - chrome - fixing time - one-sided: \n", res_chrome_fixing_1side)

print("\n The result of pq ranksums test - moodle - comments - one-sided: \n", res_moodle_comments_1side)
print("\n The result of pq ranksums test - chrome - comments - one-sided: \n", res_chrome_comments_1side)
