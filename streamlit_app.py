import streamlit as st
import pandas

st.title("TEST SNOWPARK DEPLOY")

st.header("I am playing around")

st.title("MENU FROM LABS")
st.header('Breakfast Menu')
st.text(' 🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text("🥑🍞 Avacado toast")

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

st.dataframe(my_fruit_list)
