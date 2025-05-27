import pandas as pd
import numpy as np
import streamlit as st

a = [1, 2, 3, 4, 5, 6, 7, 8]
n = np.array(a)
nd = n.reshape((2, 4))

dic = {
    "name": ['aniket', 'gupta'],
    'language': ["python", 'java'],
    'city': ['streamlit', 'delhi']

}

# st.dataframe(n)
st.dataframe(dic,width=1000,height=100)
# st.table(a)
# st.json(dic)
# st.write(dic)
