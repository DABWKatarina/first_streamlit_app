import streamlit

streamlit.title('My Parents New Healthy Dineer')

streamlit.header('Breakfast Favorutes')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale,  3 Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Ragne Egg')
streamlit.text(' 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
