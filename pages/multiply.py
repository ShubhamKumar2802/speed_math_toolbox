import streamlit as st
from utils.toolkit import MultiplicationToolkit

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
    
    space = 0
    if ques_type is 'Even-Spaced':
        spacing = st.sidebar.slider(
        label='Spacing', 
        min_value=2, 
        max_value=20,
        step=2, 
        value=4, 
        key='multiply_spacing_slider'
        )
        space = spacing   
        
    st.sidebar.button(
        'Regenerate',
        type='secondary', 
        on_click=start_session(range, ques_type, space), 
        key='multiply_start_button'   
    )

def start_session(range, ques_type, spacing):
    toolkit = MultiplicationToolkit()
    print(f'range: ({range[0]}, {range[1]})')
    session_without_timer(toolkit, range[0], range[1], ques_type, spacing)


def session_without_timer(toolkit: MultiplicationToolkit, lower_limit, upper_limit, ques_type, spacing):
    print('session_without_timer: started')
    rnd_nums = get_numbers(toolkit, lower_limit, upper_limit, ques_type, spacing)
    if rnd_nums is not None:
        ans = toolkit.ans(rnd_nums[0], rnd_nums[1])
        display_multi_ques(rnd_nums[0], rnd_nums[1], ans)

@st.cache_data
def get_numbers(_toolkit: MultiplicationToolkit, lower_limit, upper_limit, ques_type, spacing):
    rnd_nums = []
    match ques_type:
        case 'Consecutive':
            rnd_nums = _toolkit.fetch_consecutive_numbers(lower_limit, upper_limit)
        case 'Random':
            rnd_nums = _toolkit.fetch_random_numbers(lower_limit, upper_limit)
        case 'Even-Spaced':
            if spacing is not None:
                rnd_nums = _toolkit.fetch_even_spaced_numbers(lower_limit, upper_limit, spacing)

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
