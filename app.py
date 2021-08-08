from google.protobuf import message
import streamlit as st
import pandas as pd
import webbrowser
from streamlit.proto.Image_pb2 import Image
from track import Track
from matplotlib import pyplot as plt
from  plotly import express as px

d_api=pd.read_csv('https://api.covid19india.org/csv/latest/state_wise.csv')


st.title("COVID_19 TRACKER")

col1,col2=st.beta_columns(2)
col1.image("covid_image.jfif")



st.write("""Hello....

This is my mini projectand this is based on COVID_19 Pendemic.     
The virus associate with the outbreak originating in china,has been designated severe acute respiratory syndrome coroavirus2, The disease caused by that virus is now officially called COVID-19.

As of 27 July 2021, more than 194 million cases have been confirmed, with more than 4.17 million confirmed deaths attributed to COVID-19, making it one of the deadliest pandemics in history.

So here we can see a stauts  or details of Covid_19 Pendemic  situation and We are also see a anaylsis of Covid_19 data.
""")

col3,col4=st.beta_columns(2)
col3.header("     ")
col4.header("-Made by Shruti Shukla")


sidebar=st.sidebar
sidebar.title("Click for avaliable option ")
sidebar.image("covid.png",width=100)
ch=["View Data","Previous Data","Data Analysis","Covid News"]
c=sidebar.selectbox("Choose a  option",ch)


@st.cache()
def initAPI():
    return Track()

api = initAPI()



def View():
    st.title("  ")
    st.title( "  ")
    st.markdown("""--------------------------------------------------------------------------------------------""")
    st.title(" Data With State_wise ");
    data = api.getResult()
    col2.image("coro_gif.gif")
    st.title(" ")
    d_api
    st.markdown("""------------------------------------------------------------------------------------------""")
    st.title(" Numbers of rows and columns in Dataset");

    st.markdown("""
       **NUMBER OF ROWS :**             37

       **NUMBER OF COLUMNS :**           12

    """)
    st.markdown("""------------------------------------------------------------------------------------------""")
    

def Past():
    st.title("  ")
    st.title( "  ")
    st.markdown("""--------------------------------------------------------------------------------------------""")   
    st.title("This is a previous data analysis") 
    st.title(" ")
    st.image("past_gif.gif")







def analysis():
    st.title("  ")
    st.title( "  ")
    st.markdown("""--------------------------------------------------------------------------------------------""")
    st.title("Lets understand a data with Visualization")
    st.title(" ")
    st.image("visu_gif.gif",width=600)
    
    sidebar1=st.sidebar
    sidebar.title("Choose, Method you want to see  analysis of  Covid Data")
    ch1=["Bar chart","Line chart","scatter plot","histogram chart ","Pie chart"]
    c1=sidebar1.selectbox("Choose a select option",ch1)

    def bar():
        st.title("Bar char of Dataset")


    def line():
        st.title("Line chart of Dataset")


    def scat():
        st.title("Scatter plot of Dataset")
    

    def histo():
        st.title("Histogram chart of Dataset")

    
    def piec():
        st.title("Pie chart of Dataset")

    

    if c1 ==ch1[0]:
        bar()
    elif c==ch[1]:
        line()
    elif c==ch[2]:
        scat()
    elif c1==ch1[3]:
        histo()
    elif c1==ch1[4]:
        piec()



def Co_news():
    
    st.markdown("""--------------------------------------------------------------------------------------------""")
    st.text("   ")

    st.image('news.jpg')
    st.text("  ")
    url ='https://www.mygov.in/covid-19/'
    st.title(" Government officially news website  ...click here")
    if st.button('Open Browser'):
        webbrowser.open_new_tab(url)

    st.text(" ")
    url1='https://www.worldometers.info/coronavirus/'
    st.title(' Live Updated news for covid-19')
    if st.button('Click here'):
        webbrowser.open_new_tab(url1)


    st.text("  ")
    url2='https://www.cdc.gov/coronavirus/2019-ncov/index.html'
    st.title('Guidance for People Fully Vaccinated')
    if st.button('Click for Guide'):
        webbrowser.open_new_tab(url2)

    st.text("  ")
    url3='https://www.cdc.gov/coronavirus/2019-ncov/symptoms-testing/symptoms.html'
    st.title('Guidance for Covid Symptoms')
    if st.button('Click for symptoms guide'):
        webbrowser.open_new_tab(url3)
    
    st.title("  ")
    url4='https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/prevention.html'
    st.title('Guidance for Covid  Prevent')
    if st.button('Click  for prevent guide '):
        webbrowser.open_new_tab(url4)
    

    st.markdown("""--------------------------------------------------------------------------------------------""")




if c ==ch[0]:
    View()
elif c==ch[1]:
    Past()
elif c==ch[2]:
    analysis()
elif c==ch[3]:
    Co_news()

