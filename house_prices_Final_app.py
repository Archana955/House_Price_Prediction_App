# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:16:14 2023

@author: Adith
"""
import pandas as pd 
import numpy as np 

from PIL import Image
import streamlit as st
import pickle
from millify import prettify
filename = ("final_model.sav")
loaded_model = pickle.load(open(filename,'rb'))
df = pd.read_csv("Final_data.csv")

st.set_option('deprecation.showPyplotGlobalUse', False)

import warnings
warnings.filterwarnings('ignore', message='X does not have valid feature names')



st.header("House Prices Prediction App")




st.sidebar.title("Navigation")
page = st.sidebar.radio("Go To",("Homepage","Details"))

if page == "Homepage":
    
    image = Image.open('images.jpg')
    st.image(image)
    
    st.write("In This app your search for prices of houses is over, we predict houses based on your choices and give you the price of the houses according to your locality")
    
    st.header("General Information:")
    
    st.markdown("Type Of House:")
    st.write("20 - 30 : 1-STORY 1946 & NEWER ALL STYLES")
    st.write("30 - 40 : 1-STORY 1945 & OLDER")
    st.write("40 - 50 :1-STORY W/FINISHED ATTIC ALL AGES")
    st.write("50 - 60 : 1-1/2 STORY - UNFINISHED ALL AGES")
    st.write("60 - 70 : 1-1/2 STORY FINISHED ALL AGES")
    st.write("70 - 80 : 2-STORY 1946 & NEWER")
    st.write("80 - 90 : 2-STORY 1945 & OLDER")
    st.write("90 - 100 : 2-1/2 STORY ALL AGES")
    st.write("100 - 120 : SPLIT OR MULTI-LEVEL")
    st.write("120 - 130 : SPLIT FOYER")
    st.write("130 - 140 : DUPLEX - ALL STYLES AND AGES")
    st.write("140 - 150 : 1-STORY PUD (Planned Unit Development) - 1946 & NEWER")
    st.write("150 - 160 : 1-1/2 STORY PUD - ALL AGES")
    st.write("160 - 170 : 2-STORY PUD - 1946 & NEWER")
    st.write("170 - 180 : PUD - MULTILEVEL - INCL SPLIT LEV/FOYER")
    st.write("180 - 190 : 2 FAMILY CONVERSION - ALL STYLES AND AGES")
    
    st.markdown("NeighbourHood :")
    st.write ("* 0 : Bloomington Heights ")
    st.write ("* 1 : Bluestem")
    st.write ("* 2 : Briardale ")
    st.write ("* 3 : Brookside ")
    st.write ("* 4 : Clear Creek ")
    st.write ("* 5 : College Creek ")
    st.write ("* 6 : Crawford ")
    st.write ("* 7 : Edwards ")
    st.write ("* 8 : Gilbert ")
    st.write ("* 9 : Iowa DOT and Rail Road ")
    st.write ("* 10 : Meadow Village ")
    st.write ("* 11 : Mitchell ")
    st.write ("* 12 : North Ames ")
    st.write ("* 13 : Northridge ")
    st.write ("* 14 : Northpark Villa ")
    st.write ("* 15 : Northridge Heights ")
    st.write ("* 16 : Northwest Ames ")
    st.write ("* 17 : Old Town ")
    st.write ("* 18 : South & West of Iowa State University ")
    st.write ("* 19 : Sawyer ")
    st.write ("* 20 : Sawyer West ")
    st.write ("* 21 : Somerset ")
    st.write ("* 22 : Stone Brook ")
    st.write ("* 23 : Timberland ")
    st.write ("* 24 : Veenker ")
   
  
        
    
elif page == "Details":
    
    st.sidebar.header("User Input")
    with st.form("User Input"):
        
        MSSubClass = st.sidebar.slider('Type of House',min_value=(20),max_value=(190),step=(1))
        Neighborhood = st.sidebar.selectbox('NeighBourhoods Around You',('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','23','24'))
        YearBuilt = st.sidebar.number_input(label='Period passed house Built from Present (in years)',step =(1))
        YearRemodAdd = st.sidebar.number_input(label='Period Passed house remodeled from present (in years)',step =(1))
        MasVnrArea = st.sidebar.number_input(label ='Masonry area in (SqFt)',step =(1))
        BsmtUnfSF = st.sidebar.number_input(label='Incomplete basement In (SqFt)',step=(1))
        LowQualFinSF = st.sidebar.number_input(label = 'Floors Finish low quality in (SqFt)',step = (1))
        TotRmsAbvGrd = st.sidebar.selectbox('Total bedrooms above Basement',('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'))
        FireplaceQu = st.sidebar.selectbox('Quality of Fireplaces (Rating out of 5)',('0','1','2','3','4','5'))
        GarageYrBlt = st.sidebar.number_input('Period Passed Garage Built from present (in years)',step = (10))
        GarageArea = st.sidebar.number_input('Garage Area in (SqFt)',step = (10))
        WoodDeckSF = st.sidebar.number_input('Wooden Balcony in(SqFt)',step =( 10))
        OpenPorchSF = st.sidebar.number_input('Open Balcony in (SqFt)',step = (10))
        EnclosedPorch = st.sidebar.number_input(label ='Enclosed Balcony in(SqFt)',step = (10))
        ThreeSeasonPorch = st.sidebar.number_input(label='Three season Balcony in (SqFt)',step = (10))
        ScreenPorch = st.sidebar.number_input('Balcony with screen in (SqFt)',step=(10))
        PoolArea = st.sidebar.number_input('Pool Area in (SqFt)',step=(10))
        Total_basement_fin = st.sidebar.number_input('Area of basement furnished (SqFt)',step=(10))
        House_Qual = st.sidebar.selectbox('Quality of the house (Rating out of 20)',('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20')) 
        
        
        data =[[MSSubClass,Neighborhood,YearBuilt,YearRemodAdd,MasVnrArea,BsmtUnfSF,LowQualFinSF,TotRmsAbvGrd,FireplaceQu,GarageYrBlt,GarageArea,WoodDeckSF,OpenPorchSF,EnclosedPorch,ThreeSeasonPorch,ScreenPorch,PoolArea,Total_basement_fin,House_Qual]]
        
        submitted = st.sidebar.button("Results")
    
    
        
    if submitted:
        model = loaded_model.predict(data)[0]
        st.metric("Total SalePrice Of House in USD:","$"+ prettify(((int(np.round(np.exp(model)))))))
        
       
        
        
        
       
      
        
     
        
       
     
        
        

        
        
  
        
        
        
       
        
        
        
        
        
        
        
        

       
        
    
    
    
    
    



