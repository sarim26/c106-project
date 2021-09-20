import plotly.express as px
import csv 

with open('data.csv')as f:

    df = csv.DictReader(f)
    fig = px.scatter(df, x = "Days Present", y = "Marks In Percentage" )

    fig.show()