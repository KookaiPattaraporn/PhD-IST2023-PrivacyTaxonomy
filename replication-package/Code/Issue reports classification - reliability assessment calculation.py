import numpy as np
import pandas as pd
import nltk
from nltk.metrics import agreement
from nltk.metrics.agreement import AnnotationTask
from nltk.metrics import masi_distance
import csv

def calculate_alpha(filepath):
    task_data = []
    f = open(filepath, 'r')
    with f:
        reader = csv.reader(f)
        rowcount = 0
        for row in reader:
            if rowcount > 0:
              coder = row[0]
              issue = row[1]
              columncount = 0
              labels = []
              for e in row:
                if columncount > 1:
                  if int(e) == 1:
                    labels.append('R' + str(columncount-1))

                columncount +=1
              thistuple = tuple((coder, issue, frozenset(labels)))
              task_data.append(thistuple)

            rowcount +=1

    #print(task_data)
    task = AnnotationTask(distance = masi_distance)

    task.load_array(task_data)

    return task.alpha()
    

Chrome_A1A2 = calculate_alpha('replication-package/Data/Chrome-A1A2-task.csv')
print ("Chrome A1-A2: ", Chrome_A1A2)

Chrome_A1A3 = calculate_alpha('replication-package/Data/Chrome-A1A3-task.csv')
print ("Chrome A1-A3: ", Chrome_A1A3)

Moodle_A1A2= calculate_alpha('replication-package/Data/Moodle-A1A2-task.csv')
print ("Moodle A1-A2: ", Moodle_A1A2)

Moodle_A1A3= calculate_alpha('replication-package/Data/Moodle-A1A3-task.csv')
print ("Moodle A1-A2: ", Moodle_A1A3)

Chrome_A1A3_2 = calculate_alpha('/Users/KOOKAI/Dropbox/replication-package copy/Data/Chrome-A1A3-task2.csv')
print ("Chrome A1-A3 task2: ", Chrome_A1A3_2)

