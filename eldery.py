import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
xls= "http://www.biostatisticien.eu/springeR/nutrition_eldery.xls"
file1 = open("nutrition_elderly.xls", "r")
nutri = pd.read_excel("nutrition_elderly.xls")

width = 0.35 # the width of the bars
situation_counts= nutri['situation'].value_counts()
x = range(len(situation_counts))

plt.bar(x, situation_counts, width, edgecolor = 'black')
plt.xticks(x, situation_counts.index, rotation=20)
plt.ylabel("Number of people")
plt.title("Living situation of eldery")
plt.show()