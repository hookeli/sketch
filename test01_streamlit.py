import streamlit as st
from streamlit_option_menu import option_menu

st.title('welcome to the world of Nanitalk')

with st.sidebar:
    choose = option_menu('Nanitalk', ['虎克', '纳尼说', '呆鸟日记'], icons = ['house', 'cloud-upload', 'list-task'], menu_icon="cast")
    if choose == '虎克':
        st.image('https://cdn.jsdelivr.net/gh/hookeli/sketch@main/images/WX20230701-174840%402x.png', caption='caption', use_column_width=True)
    elif choose == '纳尼说':
        st.image('https://cdn.jsdelivr.net/gh/hookeli/sketch@main/images/WX20230701-174938%402x.png', caption='caption', use_column_width=True)
    else:
        st.image('https://cdn.jsdelivr.net/gh/hookeli/sketch@main/images/WX20230701-174954%402x.png', caption='caption', use_column_width=True)
