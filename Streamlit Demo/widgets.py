import streamlit as st

st.title('WIDGETS')

if st.button('Subscribe'):
    st.write('Like this video and save this')

name = st.text_input('Enter Name:')
st.write(name)

address = st.text_area('Enter your address')
st.write(address)

st.date_input('Enter a Date')

st.time_input('Enter time')

if st.checkbox('Are you Female',value=False):
    st.write('Feminist is not allowed')

v1=st.radio('colors',('red','green','blue'),index=2)

v2=st.selectbox('colors',('red','green','blue'),index=2)


v3 = st.multiselect("Colours",["r","g","b"])
st.write(v1,v2,v3)

st.slider('age',min_value=18,max_value=80,value=30,step=2)

st.number_input('Age',min_value=18,max_value=80,value=30,step=2)

img=st.file_uploader('upload a file')
st.image(img)