import csv
import plotly.express as px

with open("data5.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="date",y="cases")
    fig.show()