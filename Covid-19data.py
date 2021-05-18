import plotly_express as px 
import pandas as pd 
df = pd.read_csv(r'C:\Users\naman\Desktop\df2\HWyay\Copy+of+data+-+data.csv')
fig = px.scatter(df,x='date',y='cases',color='country')
fig.show()