import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#Data Loading

data = pd.read_csv("data/benin-malanville.csv")

data.head()  #displays the first few rows of the dataset
data.shape   #number of rows and columns
data.describe()  #summary statistics for the dataset