import pyodbc
import streamlit as st

connection_string = r"DRIVER={SQL SERVER};SERVER=.\SQLEXPRESS01;DATABASE=Food;Trusted_connection=yes"
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

st.title("Food you can buy!!!")

Name = st.text_input("Name: ")
Burger = st.checkbox("Burger: ")
Pizza = st.checkbox("Pizza: ")
st.text("Burger Price: 10.0 AED Pizza Price: 12.0 AED")
if Burger:
    Price = 10.0
    st.text("Price total is 10.0 AED for Burger")
if Pizza:
    Price = 12.0
    st.text("Price total is 12.0 AED for Pizza")

if Pizza and Burger:
    Price = 22.0
    st.text("Price total is 22.0 AED for both")

if st.button("Submit!!"):
    cursor.execute("INSERT INTO Food (Name, Burger, Pizza, Price) VALUES (?, ?, ?, ?)", (Name, Burger, Pizza, Price))
    connection.commit()
    st.success("Your order will come soon, enjoy!")
