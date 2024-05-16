import streamlit as st

st.title("Welcome to Assign shoot")
st.header("Sumbit your assignmeent with the help of assign shoot")
st.subheader("don't to be late, dont to be afraid, Asked to Assign Shoot")
st.markdown(" Write your assignment on the reasonable cost with the assign shoot")

import pandas as pd

dataset = pd.read_csv("Book1.csv")
st.dataframe(dataset)

st.subheader('''Intrest Candiadte Full fill the Details
             We will Conatct you as soon possible''')
Name = st.text_input("Enter Your Name : ")
Mail = st.text_input("Enter your mail account : ")
Address = st.text_area("Enter your full address with pincode : ")
Class = st.text_input("Enter Your Class or Branch : ")
Subject = st.text_input("Enter Your Subject Name : ")
AssignShootPack = st.selectbox("Enter your assign pack code :",( 1,2,3,4,5,6,7,8,9,10))

Button = st.button("done")
if Button :
    st.markdown(f"""
Name : {Name}
Gmail Details : {Mail}
Address : {Address}
Class : {Class}
Subject : {Subject}
Assignment Package Details : {AssignShootPack}
""")