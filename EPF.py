import pandas as pd
import math as m
import streamlit as st
import plotly.graph_objects as go

#from EMI import EMI, Amount, Loan, Years, fn
#c=pd.DataFrame()
#import streamlit_tags as stt

Amount = st.slider('Select Basic Salary',0,500,10)
#st.write("Loan amount:", Years)
col1,col2=st.columns(2)
with col1:
    Age1=st.number_input('Select Current Age',0,60,22)
    Age2=st.number_input('Select Retirement Age',0,70,60)
with col2:
    CEPF=st.number_input('Enter current EPF Balance')
    H=st.number_input('Enter Annual Hike %',5,20,8,step=1)
Age3=Age2-Age1
Rate=st.slider('Select Rate of Interest', 0.0,10.0,8.1,step=0.1)
st.write("-----------------------")
result=[]
df=pd.DataFrame(columns=['Year','Opening','Salary','Contribution','Interest','Total'])
C2=CEPF
Amount=Amount *1000
for i in range(Age1,Age2+1):
        C=Amount*12*0.1567
        I=(C+C2)*Rate/100
        T=C+I+C2
        result.append([Age1,m.ceil(C2),m.ceil(Amount),m.ceil(C),m.ceil(I),m.ceil(T)])
        Age1=Age1 +1
        Amount=Amount*(1+H/100)
        C2=T
        #T=C2+C+I
        #L2=Loan-p
df1=df.append(pd.DataFrame(result,columns=df.columns)).reset_index(drop=True)
st.dataframe(df1)
      