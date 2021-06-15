import streamlit as st 
import pandas as pd
import numpy as np
import datetime

nationality = ('INDIA', 'UAE', 'ARAB',  'REST OF WORLD', 'PAKISTAN REST OF ASIA', 'ASIA', 'AFRICA') 
emirates_issued = ('Dubai', 'Abu Dhabi', 'Sharjah', 'Ajman', 'Rasal Kaimah', 'Fujairah' , 'Umm Al Quwain')
make = ('TOYOTA','NISSAN', 'MITSUBISHI', 'CHEVROLET', 'HONDA', 'HYUNDAI', 'FORD', 'KIA', 'BMW', 'MERCEDES', 'LEXUS', 'VOLKSWAGEN', 'MAZDA', 'OTHERS')
reg_type = ('Private', 'Commercial','Rent A Car', 'Public Transportation', 'Motor Cycle', 'Trailer')
body_type = ('Saloon', 'Station Wagon', 'Hatchback', 'Pickup', 'Sports/Coupe', 'Equipment and Machinery', 'Heavy Vehicle', 'Van', 'Buses', 'Motor Bike')
                          

st.title("Premium Rate Simuator")
st.write("Please answer the following questions to know your premium rate eligibility :")

# Driver related questions

st.subheader('Driver Information : ')
st.write("#")
driver_dob = st.date_input("1. Select your date of birth :", datetime.date(1990, 1, 1), min_value = datetime.date(1900, 1, 1))
st.write("#")
driver_gender = st.radio("2. What is your gender?", ("Male", "Female"))
st.write("#")
driver_marital_status = st.radio("3. What is your Marital status?", ("Unmarried", "Married", "Single", "Others"))
st.write("#")
driver_nationality = st.selectbox("4. What is your nationality?", nationality)
st.write("#")
driver_emirates = st.selectbox("5. In which of the following Emirates was your license issued?", emirates_issued)
st.write("#")


st.write("------------------")


# Vehicle related questions

st.subheader('Vehicle Characteristics : ')
st.write('#')
vehicle_reg_date = st.date_input("1. Select the first registration date of your vehicle :", datetime.date(1990, 1, 1), min_value = datetime.date(1900, 1, 1))
st.write('#')
vehicle_value  = st.number_input("2. What is the value of your vehicle?", value = 10000, min_value = 1000, max_value = 1000000, step = 500)
st.write('#')
vehicle_make = st.selectbox("3. What is the make of your vehicle?", make) 
st.write('#')
vehicle_reg_type = st.selectbox("4. What is the registration type of your vehicle?", reg_type)
st.write('#')
vehicle_body_type = st.selectbox("5. What is the body type of your vehicle?", body_type)
st.write('#')
vehilce_seats = st.number_input("6. How many seats does your vehicle have?", min_value = 1, value = 4, max_value = 100, step = 1)
st.write('#')
vehicle_cylinders = st.number_input("7. How many cylinders does your vehicle have?", min_value = 1, value = 2, max_value = 20, step = 1)
st.write('#')

# Policy related questions

st.write("------------------")
st.write("#")
st.subheader('Policy history : ')
st.write("#")   
claim_ever_made = st.radio("1. Have you ever made a vehicle inusrance claim in the past?", ("Yes", "No"))
st.write("#")
claim_made_last_year = st.radio("2. Did you make a vehicle insurance claim in the last year?", ("Yes", "No"))
st.write("#")
no_claim_years = st.number_input("3. In the past 5 years, how many years have you made NO vehicle insurance claims?", value = 5, min_value = 0, 
                                    max_value = 5, step = 1)
st.write("------------------")
