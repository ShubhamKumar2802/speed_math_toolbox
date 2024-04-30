import streamlit as st
from utils.toolkit import MultiplicationToolkit
import utils.toolkit as tlk

def render_sidebar():
    range = st.sidebar.slider(
        label='Range', 
        min_value=1, 
        max_value=150, 
        value=(50, 100), 
        key='multiply_range_slider'
    )

    distance_options = ['Consecutive', 'Even-Spaced', 'Random']
    ques_type = st.sidebar.radio(label='Distance', options=distance_options, key='mulitply_distance_radio')
    
    regen_button = st.sidebar.button(
        'Regenerate',
        type='secondary', 
        on_click=start_session(range, ques_type), 
        key='multiply_start_button'   
    )

def start_session(range, ques_type):
    toolkit = tlk.MultiplicationToolkit()
    print(f'range: ({range[0]}, {range[1]})')
    session_without_timer(toolkit, range[0], range[1], ques_type)


def session_without_timer(toolkit: MultiplicationToolkit, lower_limit, upper_limit, ques_type):
    print('session_without_timer: started')
    rnd_nums = get_numbers(toolkit, lower_limit, upper_limit, ques_type)
    if len(rnd_nums) > 0:
        ans = toolkit.ans(rnd_nums[0], rnd_nums[1])
        display_multi_ques(rnd_nums[0], rnd_nums[1], ans)

@st.cache_data
def get_numbers(_toolkit, lower_limit, upper_limit, ques_type):
    rnd_nums = []
    match ques_type:
        case 'Consecutive':
            rnd_nums = _toolkit.fetch_consecutive_numbers(lower_limit, upper_limit)
        case 'Random':
            rnd_nums = _toolkit.fetch_random_numbers(lower_limit, upper_limit)
        case 'Even-Spaced':
            rnd_nums = _toolkit.fetch_even_spaced_numbers(lower_limit, upper_limit, 4)

    print('session_without_timer: fetched random numbers')
    print(rnd_nums)
    return rnd_nums


def display_multi_ques(num_a, num_b, ans):
    exp = f'$ {num_a} \\times {num_b}$'
    st.subheader(exp)
    checkbox_col, ans_col = st.columns([1, 2])
    with checkbox_col:
        reveal_ans = st.checkbox('Reveal Answer', value=False, key='multiply_revealans_checkbox')
    
    with ans_col:
        if reveal_ans:
            st.write(ans)   


st.sidebar.header(':keycap_star: Multipy')
st.header(':keycap_star: Multipy')
render_sidebar()
