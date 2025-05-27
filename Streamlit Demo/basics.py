import streamlit as st
import pandas as pd
import time

################ Text Utility ###############
st.title('Startup Dashboard')
st.header('Iam learning steamlit')
st.subheader('And I am loving it')
st.write('This is the normal text')
st.markdown("""
### my favourite movies
- Race 3
- Hamshakal 
- HouseFull
""")

st.code("""
def foo(input):
    return foo**2
x = foo(2)
""")

st.latex('x^2 + y^2 + 2 = 0')

########### Display Elements ##############

df = pd.DataFrame({
    'name': ['Nitish', 'Ankit', 'Anupam'],
    'marks': [50, 60, 70],
    'package': [10, 22, 23]
})

st.dataframe(df)

st.metric('Revenue', 'Rs 3L', '-3%')

st.json({
    'name': ['Nitish', 'Ankit', 'Anupam'],
    'marks': [50, 60, 70],
    'package': [10, 22, 23]
})

############# Display Media ###############|


st.image('hd.jpeg')

# st.video('video.mp4')

############ Creating Layout ###################

st.sidebar.title('Sidebar ka title')

col1, col2, col3 = st.columns(3)

with col1:
    st.image('image.jpeg')
with col2:
    st.image('image.jpeg')
with col3:
    st.image('image.jpeg')

################ Showing Status ##############

st.error('Login Failed')

st.success('Login Successful')

st.warning('warning')

st.info('info')

bar = st.progress(0)

# for i in range(1, 101):
#     time.sleep((0.05))
#     bar.progress(i)
# st.write('Task Completed')

##################### Task User input ####################

email = st.text_input('Enter Email')

number = st.number_input('Enter Age')

date = st.date_input('Enter Date')


################### Buttons ###############################

email = st.text_input('Enter Email')
password = st.text_input('Enter password')
gender = st.selectbox('Select gender', ['Male', 'Female'])

btn = st.button('Login Karo')

if btn:
    if email == 'aniket@gmail.com' and password == '1234':
        st.balloons()
        st.success('Login Successful')
        st.write(gender)
    else:
        st.error('Login Failed')


###################### Browse file ###################

file = st.file_uploader('Upload a csv file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df)
