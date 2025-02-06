import streamlit as st
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

df = pd.read_excel('test.xlsx')


st.title("引継ぎくん")
with open("sample.txt","r", encoding="utf=8") as f:
	lines=f.read().splitlines()

option = st.selectbox(
    	'料金所を選択してください',
    	['富山', '金沢', '福井','敦賀'],
    	index = None,
    	placeholder="料金所を選択してください")


keyword = option

if option == "富山":
	filtered_df = df[df['料金所'].str.contains(keyword)]
	st.write(filtered_df)

if option == "金沢":
	filtered_df = df[df['料金所'].str.contains(keyword)]
	st.write(filtered_df)

if option == "福井":
	filtered_df = df[df['料金所'].str.contains(keyword)]
	st.write(filtered_df)

if option == "敦賀":
	filtered_df = df[df['料金所'].str.contains(keyword)]
	st.write(filtered_df)