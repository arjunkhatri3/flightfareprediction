
## https://blog.jcharistech.com/2020/02/17/simple-machine-learning-app-with-streamlit-using-car-evaluation-dataset/




import pickle
import pandas as pd



import streamlit as st


## title of your web page !
st.title('Flight fare prediction')






# Date_of_Journey

date_dep=st.date_input('Choose departure date')
## whatever date_dep we have  , first we have to convert it into date-time nature..
         

Journey_day = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").day)
Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)




# Departure
Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)




# Arrival
date_arr=st.date_input('Choose arrival date')
Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)




# Duration
dur_hour = abs(Arrival_hour - Dep_hour)
dur_min = abs(Arrival_min - Dep_min)



# Total Stops
Total_stops=st.selectbox("Select number of stops from dropdown",options=[1,2,3,4,5])





### lets one-hot encode our feature ,airline 
airline=st.selectbox(" Select your Airline " , ["Air India","GoAir","IndiGo","Jet Airways","Multiple carriers","SpiceJet",
                                    "Jet_Airways_Business","Vistara_Premium_economy","Trujet","Multiple carriers Premium economy"])

## ie initially all features will be 0(ie absent)
Jet_Airways , IndiGo , Air_India  ,Multiple_carriers ,SpiceJet= 0,0,0,0,0
GoAir, Multiple_carriers_Premium_economy, Jet_Airways_Business, Vistara_Premium_economy, Trujet=0,0,0,0,0




    
## if airline is Jet Airways then we are going to set it as 1 and all other by 0
if (airline=='Jet Airways'):
    Jet_Airways = 1
 
elif (airline=='IndiGo'):
    IndiGo = 1
    
elif (airline=='Air India'):
     Air_India = 1

          
elif (airline=='Multiple carriers'):
     Multiple_carriers = 1
     

elif (airline=='SpiceJet'):
      SpiceJet = 1


elif (airline=='GoAir'):
      GoAir = 1

elif (airline=='Multiple carriers Premium economy'):
     Multiple_carriers_Premium_economy = 1

elif (airline=='Jet Airways Business'):
     Jet_Airways_Business = 1

elif (airline=='Vistara Premium economy'):
     Vistara_Premium_economy = 1
     
else :
     Trujet = 1




### lets one-hot encode our feature source !
source = st.selectbox(" Select your source " , ['Bangalore', 'Mumbai','Delhi','Kolkata',"Chennai"])

s_Bangalore, s_Mumbai, s_Delhi, s_Kolkata, s_Chennai=0,0,0,0,0

if source == "Bangalore":
    s_Bangalore = 1
elif source == "Chennai":
    s_Chennai = 1
elif source == "Delhi":
    s_Delhi = 1
elif source == "Kolkata":
    s_Kolkata = 1
elif source == "Mumbai":
    s_Mumbai = 1
    
    
    
### lets one-hot encode our feature destination ! 
destination = st.selectbox(" Select your destination " , ['Bangalore', 'Mumbai','Delhi','Kolkata',"Chennai"])

d_Bangalore, d_Mumbai, d_Delhi, d_Kolkata, d_Chennai=0,0,0,0,0

if destination == "Bangalore":
    d_Bangalore = 1
elif destination == "Chennai":
    d_Chennai = 1
elif destination == "Delhi":
    d_Delhi = 1
elif destination == "Kolkata":
    d_Kolkata = 1
elif destination == "Mumbai":
    d_Mumbai = 1







model = pickle.load(open(r'C:\Users\mcr\Entire_Data_Science_End-2-End_Projects\Flight-Price-Prediction-master\Deployment/flight_rf.pkl', "rb"))



if st.button('Predict the Price'):
    prediction = model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara_Premium_economy,
            s_Bangalore,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Bangalore,
            d_Mumbai,
            d_Delhi,
            d_Kolkata,
            d_Delhi
        ]])
    st.write('Price is {}'.format(prediction[0]))
        
        




    ### run as streamlit python file_name    
