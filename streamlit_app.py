
import streamlit
import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


streamlit.title("My Parents New Healthy Diner")

streamlit.header('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.header('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.header('🐔 Hard-Boiled Free-Range Egg')
streamlit.header('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits_selected = streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index), ['Strawberries', 'Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
