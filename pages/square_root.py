import streamlit as st
import utils.toolkit as tlk
import math

st.header(':seedling: Square Root')
st.sidebar.header(':seedling: Square Root')

num_range = st.sidebar.slider(
    label='Range', 
    min_value=1, 
    max_value=10000, 
    value=5000,
    key='square_root_range_slider'
)

# print(num_range)

def get_num(): 
    pass

def get_toolkit_reference():
    toolkit = tlk.SquareRootToolkit()
    return toolkit

def display_ques(num, ans): 
    exp = f'$ \sqrt{num} = $'
    st.subheader(exp)
    
    checkbox_col, ans_col = st.columns([1, 2])

    with checkbox_col:
        reveal_ans = st.checkbox('Reveal Answer', value=False, key='multiply_revealans_checkbox')
    
    with ans_col:
        if reveal_ans:
            st.write(ans)   

@st.cache_data
def get_number(_toolkit, upper_limit):
    return _toolkit.fetch_random_num(1, num_range)



toolkit = get_toolkit_reference()
num = get_number(toolkit, num_range)
display_ques(num, toolkit.ans(num))