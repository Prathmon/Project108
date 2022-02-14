import plotly.figure_factory as ff
import pandas as pd
import csv

file1 = pd.read_csv("data.csv",encoding='utf-8')
figure = ff.create_distplot([file1["Avg Rating"].tolist()], ["Mobile Brand"], show_hist = False)
figure.show()