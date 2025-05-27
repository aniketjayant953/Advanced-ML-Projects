import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import random

data = pd.DataFrame(columns=['a','b','c'])



data['a']=np.random.randn(100)
data['b']=np.random.randn(100)
data['c']=np.random.randn(100)


#st.line_chart(data)

#st.area_chart(data,width=100,height=100)
#st.bar_chart(data,width=100,height=100)

#plt.scatter(data['a'],data['b'])
#plt.title('scatter')
#st.pyplot()

st.graphviz_chart("""
digraph{
watch -> like
like -> share
share -> subscribe ->
share-> watch

} """)

#st.plotly_chart

city= pd.DataFrame({
    'cites':['Chicago','Minneapolis','Louisville','Topeka'],
    'lat':[41.868171,44.979840,38.257972,39.030575],
    'lon': [-87.667458,-93.272474,-85.765187,-95.702548]


})
st.map(city)

#st.image('location')
#st.audio('location')
#st.video('location')
