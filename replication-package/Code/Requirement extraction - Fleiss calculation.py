import numpy as np
import pandas as pd
import sklearn as sk
import statsmodels.stats.inter_rater

def calculate_fleiss(filepath,n_cat):
    data = pd.read_csv(filepath)
    data = statsmodels.stats.inter_rater.aggregate_raters(data, n_cat)
    fleiss = statsmodels.stats.inter_rater.fleiss_kappa(data[0], method='fleiss')
    return fleiss


#Calculate fleiss kappa of requirements extraction process
fleiss_reqext_gdpr = calculate_fleiss('replication-package/Data/Coding results - requirements extraction - GDPR.csv',2)
fleiss_reqext_iso = calculate_fleiss('replication-package/Data/Coding results - requirements extraction - ISO.csv',2)

print("Fleiss value of GDPR requirements extraction:", fleiss_reqext_gdpr)
print("Fleiss value of ISO requirements extraction:", fleiss_reqext_iso)


#Calculate fleiss kappa of requirements classification process
fleiss_reqclass = calculate_fleiss('replication-package/Data/Coding results - requirements classification.csv',7)

print("Fleiss value of requirements classification:", fleiss_reqclass)
