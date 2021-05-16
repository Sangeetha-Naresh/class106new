import plotly.express as px
import csv
import pandas as pd

#use pandas instead of Dictreader

with open("./data/cups of coffee vs hours of sleep.csv") as csv_file:
      df = pd.read_csv(csv_file)
      fig = px.scatter(df,x="Coffee in ml", y="sleep in hours", color="week")
      fig.show()
