"""This maps all stations onto google maps"""


import plotly.express as px
geo_df = []
px.set_mapbox_access_token(open(".mapbox_token").read())
fig = px.scatter_geo()
fig.show()