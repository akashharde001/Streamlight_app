import streamlit
import pandas


streamlit.title('Healty chichen....')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



streamlit.header('🥣Breakfast Menu')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑Hard-Boiled Free-Range Egg')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page.
my_fruit_list = my_fruit_list.set_index('Fruit')

select * from pc_rivery_db.public.fruit_load_list
fruits_to_show = my_fruit_list.loc[fruits_selected]
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

