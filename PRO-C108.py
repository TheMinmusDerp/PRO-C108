import plotly.figure_factory as ff
import pandas as pd

df=pd.read_csv("projectdata.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist=False)
fig.show()