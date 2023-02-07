import os
import streamlit as st
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Config
path_chrome = "Chromedriver/chromedriver.exe"
Download_path = r"C:\Users\tourayo\Downloads"
st.title("Cargonet Import")
st.write("Make sure you adjust the settings before starting import!")
st.write(" ")
st.write(" ")


with st.sidebar:
    st.title("Settings")
    Start_dato = st.date_input("Start dato")
    Slutt_dato = st.date_input("Slutt dato")



    Start_dato = Start_dato.strftime('%d%m%Y')
    Slutt_dato = Slutt_dato.strftime('%d%m%Y')
    Import_type = st.radio(
    "Linde eller Nippon?",
    ('Linde', 'Nippon'))
    start = st.button("Start import")

if start:
    path_chrome = r"Chromedriver\chromedriver.exe"
    Company_dict = {"0124034": "9"}
    df = pd.read_excel("Input/Input.xlsx", sheet_name="Linde").fillna("")
    st.info("Script started!")
    try:
        os.makedirs("Input")
    except:
        pass

    try:
        os.makedirs("Output")
    except:
        pass

    driver = webdriver.Chrome(path_chrome)
    driver.get("https://www.cargonet.no/")
    st.write(WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div[1]/a/div[1]"))).text)