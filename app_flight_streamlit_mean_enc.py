
## https://blog.jcharistech.com/2020/02/17/simple-machine-learning-app-with-streamlit-using-car-evaluation-dataset/
## Below one is not working right !





import pickle
import pandas as pd



import streamlit as st


## title of your web page !
st.title('Flight fare prediction')






# Date_of_Journey

date_dep=st.date_input('Choose Date of Journey')
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
Total_stops=st.selectbox("Select number of stops from dropdown",options=[0,1,2,3,4])





### lets one-hot encode our feature ,airline 
airline=st.selectbox(" Select your Airline " , ["Air India","GoAir","Vistara","IndiGo","Jet Airways","Multiple carriers","SpiceJet",
                                    "Jet_Airways_Business","Vistara_Premium_economy","Trujet","Multiple carriers Premium economy"])

## ie initially all features will be 0(ie absent)
Jet_Airways , IndiGo , Air_India  ,Multiple_carriers ,SpiceJet,Vistara= 0,0,0,0,0,0
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
     
elif (airline=='Vistara'):
     Vistara= 1
     
else :
     Trujet = 1




### lets encode our feature source !

dict_source={'Banglore': 8017.464269458353,
 'Chennai': 4789.892388451443,
 'Delhi': 10540.113536155202,
 'Kolkata': 9158.389411354929,
 'Mumbai': 5059.708751793401}

source = st.selectbox(" Select your source " , ['Bangalore', 'Mumbai','Delhi','Kolkata',"Chennai"])



if source == "Bangalore":
    s=dict_source['Banglore']
elif source == "Chennai":
    s =dict_source['Chennai']
elif source == "Delhi":
    s =dict_source['Delhi']
elif source == "Kolkata":
   s = dict_source['Kolkata']
else:
   s =dict_source['Mumbai']
     
    
    
    
    
    
### lets encode our feature destination ! 
destination = st.selectbox(" Select your destination " , ['Bangalore', 'Cochin','Delhi','Kolkata',"Hyderbad",'New Delhi'])

dict_dest={
'Bangalore': 9158.389411354929,
'Cochin': 10540.113536155202,
'Delhi': 5143.918577075099,
'Hyderabad': 5059.708751793401,
'Kolkata': 4789.892388451443,
'New Delhi': 11917.716738197425
 }


if destination == "Bangalore":
    d =dict_dest['Bangalore']
elif destination == "Cochin":
    d =dict_dest['Cochin']
elif destination == "Delhi":
    d =dict_dest['Delhi']
elif destination == "Hyderabad":
    d =dict_dest['Hyderabad']
elif destination == "New Delhi":
    d =dict_dest['New Delhi']
    
else :
    d =dict_dest['Kolkata']






model = pickle.load(open(r'C:\Users\mcr\Entire_Data_Sceince_End-2-End_Projects\Flight-Price-Prediction-master\Deployment/flight_mean_enc.pkl', "rb"))



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
            Vistara,
            s,
            d
        ]])
    st.write('Price is {}'.format(prediction[0]))
        
        


        
