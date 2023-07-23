import streamlit
streamlit.title('My Parents new healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text ('🥣 Omega 3 & Blueberry Datmeal')
streamlit.text ('🥗 Kale, Spinach & Rocket smoothie')
streamlit.text ('🐔 Hard-boiled Free-Range Egg')
streamlit.text ('🥑🍞 Avacodo Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import Pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
