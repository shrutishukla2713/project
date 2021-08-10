from google.protobuf import message
from sqlalchemy.orm.session import Session
import streamlit as st
import pandas as pd
import webbrowser
from streamlit.proto.Image_pb2 import Image
from track import Track
from matplotlib import pyplot as plt
from  plotly import express as px
from sqlalchemy.orm import  sessionmaker
from sqlalchemy import create_engine
from database import Past_data

# @st.cache()
def createSession():
        
    engine = create_engine("sqlite:///Past_data.sqlite3")
    Session = sessionmaker(bind=engine)
    return Session()

session = createSession()

## d_api=pd.read_csv('https://api.covid19india.org/csv/latest/state_wise.csv')


st.title("COVID_19 TRACKER")

col1,col2=st.beta_columns(2)
col1.image("covid_image.jfif")



st.write("""Hello....

This is my mini projectand this is based on COVID_19 Pendemic.     
The virus associate with the outbreak originating in china, has been designated severe acute respiratory syndrome coroavirus2, The disease caused by that virus is now officially called COVID-19.

As of 27 July 2021, more than 194 million cases have been confirmed, with more than 4.17 million confirmed deaths attributed to COVID-19, making it one of the deadliest pandemics in history.

So here we can see a stauts  or details of Covid_19 Pendemic  situation, We are also see a Past data of Covid_19 data for further analysis and it is helps to us for understanding a  covid pendemic situations.

We can also see a others  information links related covid 19 situation, news, vaccination, symptoms and prevents.
""")

col3,col4=st.beta_columns(2)
col3.header("     ")
col4.header("-Made by Shruti Shukla")


sidebar=st.sidebar
sidebar.title("Click for avaliable option ")
sidebar.image("covid.png",width=100)
ch=[" Covid Live Track","Previous Data","Data Analysis","Covid News"]
c=sidebar.selectbox("Choose a  option",ch)


# @st.cache()
def initAPI():
    return Track()

api = initAPI()

@st.cache()
def getData(api):
    return api.getResult()

def getCountryData(country, data):
    for details in data:
        if details.get('Country_text') == country:
            return details


def View():
    st.title("  ")
    st.title( "  ")
    st.markdown("""--------------------------------------------------------------------------------------------""")
    st.title(" Live tracker  for covid data ");
    btn = st.checkbox('Load Data')
    if btn:
        try:
            data = getData(api)
            st.text(data)
            showData = st.checkbox("Show Data")
            if showData:
                st.table(data)
            country_list = []
            
            for d in data:
                country_list.append(d.get('Country_text'))
            st.title("Select Country")

            sel_country = st.selectbox("Country", country_list)

            if sel_country:
                detail = getCountryData(sel_country, data)

                c1, c2 = st.beta_columns(2)
                c1.header('Active Cases')
                c2.subheader(detail.get('Active Cases_text'))

                c1, c2 = st.beta_columns(2)
                c1.header('Last Update')
                c2.subheader(detail.get('Last Update'))
              
                c1, c2 = st.beta_columns(2)
                c1.header('New Cases')
                c2.subheader(detail.get('New Cases_text'))
  
                c1, c2 = st.beta_columns(2)
                c1.header('New Deaths')
                c2.subheader(detail.get('New Deaths_text'))
                
                c1, c2 = st.beta_columns(2)
                c1.header('Total Cases')
                c2.subheader(detail.get('Total Cases_text'))
  
                c1, c2 = st.beta_columns(2)
                c1.header('Total Deaths')
                c2.subheader(detail.get('Total Deaths_text'))
                 
                c1, c2 = st.beta_columns(2)
                c1.header('Total Recovered')
                c2.subheader(detail.get('Total Recovered_text'))

                save_btn = st.button('Save Data')

                if save_btn:
                    obj = Past_data(country = detail.get('Country_text'), last_update=detail.get('Last Update'),new_cases=detail.get('New Cases_text'),new_Deaths=detail.get('New Deaths_text'),active_cases=detail.get('Active Cases_text'),total_Recovered=detail.get('Total Recovered_text'),total_Deaths=detail.get('Total Deaths_text'),total_cases=detail.get('Total Cases_text'))
                    session.add(obj)
                    session.commit()
            

        except Exception as e:
            print(e)
            st.error('something went wrong')


col2.image("coro_gif.gif")
    
st.markdown("""------------------------------------------------------------------------------------------""")
    

def Past():
    st.title("  ")
    st.title( "  ")
    st.markdown("""--------------------------------------------------------------------------------------------""")   
    st.title("This is a previous data analysis") 
    st.title(" ")
    st.image("past_gif.gif")

    details = session.query(Past_data).all()

    for detail in details:
        
        st.markdown('#')
        st.header('Country : '+detail.country)
        st.markdown('---')
        st.subheader('Last Update : '+str(detail.last_update))
        st.subheader('New_cases :'+str(detail.new_cases))
        st.subheader('New_Deaths :'+str(detail.new_Deaths))
        st.subheader('Activ_cases :'+str(detail.active_cases))
        st.subheader('Total_Recovered :'+str(detail.total_Recovered))
        st.subheader('Total_Deaths :'+str(detail.total_Deaths))
        st.subheader('Total_cases :'+str(detail.total_cases))




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

    col3,col4=st.beta_columns(2)
    col3.image('news.jpg')
    

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

