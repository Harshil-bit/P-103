import pandas as pd
import plotly.express as px

df=pd.readcsv("Covid Details.csv")

fig=px.scatter(df,x="date",y="cases",)
fig.show()