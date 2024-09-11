import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
import streamlit as st
from streamlit_option_menu import option_menu
import pickle
from PIL import Image

# User input options
class option:
    year_values = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    town_values = ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
                    'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG',
                    'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
                    'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL',
                    'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES',
                    'TOA PAYOH', 'WOODLANDS', 'YISHUN']
    town_dict = {name: idx for idx, name in enumerate(town_values)}

    flat_type_values = ['3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE', '1 ROOM', 'MULTI-GENERATION']
    flat_type_dict = {name: idx for idx, name in enumerate(flat_type_values)}

    flat_model_values = ['Improved', 'New Generation', 'Model A', 'Standard', 'Simplified', 'Premium Apartment',
                        'Maisonette', 'Apartment', 'Model A2', 'Type S1', 'Type S2', 'Adjoined flat', 
                        'Terrace', 'DBSS', 'Model A-Maisonette', 'Premium Maisonette', 
                        'Multi Generation', 'Premium Apartment Loft', 'Improved-Maisonette', '2-room', '3Gen']
    flat_model_dict = {name: idx for idx, name in enumerate(flat_model_values)}

    storey_start_values = [0.01185826, 1.38629436, 1.94591015, 2.30258509, 2.56494936, 2.77258872, 
                           2.94443898, 3.09104245, 3.21887582, 3.33220451, 3.4339872, 3.52636052, 
                           3.61091791, 3.67702119]
    storey_end_values = [1.09861229, 1.79175947, 2.19722458, 2.48490665, 2.7080502, 2.89037176, 
                         3.04452244, 3.17805383, 3.29583687, 3.40119738, 3.49650756, 3.52462742]

    floor_area_sqm = [i for i in range(37, 154)]
    remaining_lease_month = list(range(12))
    remaining_lease_year = list(range(41, 98))
    lease_commence_date = list(range(1966, 2021))

# Function to predict resale flat prices
def resale_flat_prices_predict(year, town, flat_type, floor_area_sqm, flat_model,
                                storey_start, storey_end, remaining_lease_year,
                                remaining_lease_month, lease_commence_date):
    # Load the regression model
def load_model():
    url = "https://example.com/path-to-your-model.pkl"  # Use a direct link to the model file
    response = requests.get(url)
    model = pickle.load(BytesIO(response.content))
    return model

    user_regression_data = np.array([[year, option.town_dict[town], option.flat_type_dict[flat_type], 
                                      floor_area_sqm, option.flat_model_dict[flat_model],
                                      storey_start, storey_end, remaining_lease_year, 
                                      remaining_lease_month, lease_commence_date]])

    y_pred = model_regression.predict(user_regression_data)
    y_pred_exponential_value = np.exp(y_pred[0])
    return y_pred_exponential_value

# Streamlit app
st.set_page_config(layout="wide")
st.title(":red[SINGAPORE RESALE FLAT PRICES PREDICTING]")

with st.sidebar:
    select = option_menu("DATA EXPLORATION", options=["Home", "Flat Prices Prediction", "Step-by-Step Process"])

if select == "Home":
    st.write("")
    st.header(":green[Introduction]")
    st.write("""In Singapore's competitive real estate market, accurately estimating the resale price of flats is crucial for both buyers and sellers. Factors such as location, flat type, floor area, and lease duration significantly impact resale values. This project aims to develop a machine learning model to predict the resale prices of flats based on historical transaction data. By creating a user-friendly web application, this model will assist users in making informed decisions about buying or selling flats.""")

    st.header(":green[Skills Gained]")
    st.write("1. Data Wrangling")
    st.write("2. Exploratory Data Analysis (EDA)")
    st.write("3. Model Building")
    st.write("4. Model Deployment")

    st.header(":green[Domain:]")
    st.write("Real Estate")

    st.header(":green[Data Source :]")
    st.write("https://beta.data.gov.sg/collections/189/view")

    st.header(":green[Results]")
    st.write("The project provides a valuable tool for buyers and sellers in Singapore’s housing market, offering estimates to aid in making informed decisions. It also showcases the application of machine learning in real estate and web development.")

if select == "Flat Prices Prediction":
    st.header(":green[RESALE FLAT PRICES PREDICTION]")

    col1, col2 = st.columns(2)
    with col1:
        year = st.selectbox(label="Year", options=option.year_values)
        town = st.selectbox(label="Town", options=option.town_values)
        flat_type = st.selectbox(label="Flat_Type", options=option.flat_type_values)
        floor_area_sqm = st.selectbox(label="Floor_Area_sqm", options=option.floor_area_sqm)
        flat_model = st.selectbox(label="Flat_Model", options=option.flat_model_values)

    with col2:
        storey_start = st.selectbox(label="Storey_Start", options=option.storey_start_values)
        storey_end = st.selectbox(label="Storey_End", options=option.storey_end_values)
        remaining_lease_year = st.selectbox(label="Remaining_Lease_Year", options=option.remaining_lease_year)
        remaining_lease_month = st.selectbox(label="Remaining_Lease_Month", options=option.remaining_lease_month)
        lease_commence_date = st.selectbox(label="Lease_Commence_Date", options=option.lease_commence_date)

    button = st.button(":blue[PREDICT THE RESALE FLAT PRICE]", use_container_width=True)

    if button:
        predict_price = resale_flat_prices_predict(year, town, flat_type, floor_area_sqm, flat_model, 
                                                   storey_start, storey_end, remaining_lease_year, 
                                                   remaining_lease_month, lease_commence_date)
        st.write(":red[THE RESALE FLAT PRICE IS : ]", predict_price)



if select == "Step-by-Step Process":
    st.markdown("<h1 style='color: #1f77b4;'>Data Collection:</h1>", unsafe_allow_html=True)
    st.write("""Data Collection: Obtain the dataset of resale flat transactions from the Singapore Housing and Development Board (HDB). The dataset should cover transactions from 1990 to the present.""")
    
    st.markdown("<h1 style='color: #1f77b4;'>Data Cleaning:</h1>", unsafe_allow_html=True)
    st.write("""Data Cleaning: Handle missing values, outliers, and inconsistencies. Convert data types as necessary and ensure the dataset is structured for analysis.""")
    
    st.markdown("<h2 style='color: #ff7f0e;'>Feature Extraction:</h2>", unsafe_allow_html=True)
    st.write("Identify and extract relevant features such as town, flat type, storey range, floor area, flat model, and lease commence date.")

    st.markdown("<h2 style='color: #2ca02c;'>Feature Creation:</h2>", unsafe_allow_html=True)
    st.write("Develop additional features that might improve prediction accuracy, such as the age of the flat or proximity to amenities.")

    st.markdown("<h2 style='color: #d62728;'>Handling Skewness Using Log Transformation:</h2>", unsafe_allow_html=True)
    st.write("Log transformation is used to reduce skewness in a distribution and make it more symmetric, converting a skewed distribution to a normal distribution.")

    st.markdown("<h2 style='color: #9467bd;'>Model Selection and Training:</h2>", unsafe_allow_html=True)
    st.write("An outlier is a single data point that goes far outside the average value of a group. Outlier Removal in Dataset using Interquartile Range (IQR) Method is used.")

    st.markdown("<h2 style='color: #8c564b;'>Model Selection:</h2>", unsafe_allow_html=True)
    st.write("Choose an appropriate machine learning model and train it on the dataset.")

    st.markdown("<h2 style='color: #e377c2;'>Evaluation Metrics:</h2>", unsafe_allow_html=True)
    st.write("Assess the model’s performance using Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R² Score.")

    st.markdown("<h2 style='color: #7f7f7f;'>Streamlit Web Application Development:</h2>", unsafe_allow_html=True)
    st.write("Adjust the model’s parameters to optimize performance.")

    st.markdown("<h2 style='color: #bcbd22;'>Deployment on Hugging Face:</h2>", unsafe_allow_html=True)
    st.write("Create a user-friendly interface where users can input flat details (town, flat type, etc.).")

    st.markdown("<h2 style='color: #17becf;'>Integration:</h2>", unsafe_allow_html=True)
    st.write("Integrate the trained model into the web application to provide real-time price predictions based on user inputs.")

    st.markdown("<h2 style='color: #1f77b4;'>Deployment:</h2>", unsafe_allow_html=True)
    st.write("Ensure the web application operates smoothly and deploy it to a hosting platform.")

    st.markdown("<h2 style='color: #ff7f0e;'>Documentation and Reporting:</h2>", unsafe_allow_html=True)
    st.write("Document the project, includin
