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

    # question_count = st.sidebar.slider(
    #     label='Number of Questions', 
    #     min_value=1, 
    #     max_value=20, 
    #     key='multiply_questions_slider'
    # )

    # timer_checkbox = st.sidebar.checkbox('Enable Timer', key='multiply_timer_checkbox')
    # if timer_checkbox:
    #     timer = st.sidebar.slider(
    #         label='Time (sec)', 
    #         min_value=60, 
    #         max_value=600,
    #         # format='time',
    #         key='multiply_time_slider'
    #     )

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
    rnd_nums = []

    match ques_type:
        case 'Consecutive':
            rnd_nums = toolkit.fetch_consecutive_numbers(lower_limit, upper_limit)
        case 'Random':
            rnd_nums = toolkit.fetch_random_numbers(lower_limit, upper_limit)
        case 'Even-Spaced':
            rnd_nums = toolkit.fetch_even_spaced_numbers(lower_limit, upper_limit, 4)

    print('session_without_timer: fetched random numbers')
    print(rnd_nums)
    if len(rnd_nums) > 0:
        # st.write(rnd_nums[0]*rnd_nums[1])
        display_multi_ques(rnd_nums[0], rnd_nums[1])


def session_with_timer(): 
    pass 

@st.cache_data
def display_multi_ques(num_a, num_b):
    ques_col, ans_inp_col = st.columns([1, 2])
    with ques_col:
        exp = f'$ {num_a} * {num_b} = $'
        st.subheader(exp)
    
    with ans_inp_col:
        ans = num_a * num_b
        response = st.number_input(
            label='Ans', 
            value=0, 
            key='mulitply_ans_numinput', 
            # on_change=reveal_ans(ans), 
            placeholder='???'
        )

        if response: 
            reveal_ans(ans)

def reveal_ans(ans):
    st.write(ans)

st.sidebar.header(':keycap_star: Multipy')
st.header(':keycap_star: Multipy')
render_sidebar()
