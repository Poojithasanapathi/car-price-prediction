
# ============================================
# IMPORT LIBRARIES
# ============================================

# Streamlit is used to create the web application
import streamlit as st

# Pandas is used to create the input DataFrame
import pandas as pd

# Joblib is used to load the trained machine learning model
import joblib


# ============================================
# PAGE CONFIGURATION
# ============================================

# Configure the Streamlit page
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)


# ============================================
# LOAD TRAINED MODEL
# ============================================

# Load the trained model
# Your current model requires the "name" column
final_model = joblib.load(
    "car_price_final_model.pkl"
)


# ============================================
# TITLE
# ============================================

# Display the main title
st.title("🚗 Car Price Prediction")

# Display a short description
st.write(
    "Enter the details of a car to predict its estimated price."
)


# ============================================
# CAR INFORMATION
# ============================================

st.subheader("🚘 Car Information")


# Create two columns for the input fields
col1, col2 = st.columns(2)


# ============================================
# COLUMN 1
# ============================================

with col1:

    # ----------------------------------------
    # CAR NAME
    # ----------------------------------------

    # The trained model requires the name column
    name = st.text_input(
        "Car Name",
        value="alfa-romero giulia"
    )


    # ----------------------------------------
    # SYMBOLING
    # ----------------------------------------

    symboling = st.number_input(
        "Symboling",
        min_value=-5,
        max_value=5,
        value=0,
        step=1
    )


    # ----------------------------------------
    # FUEL TYPE
    # ----------------------------------------

    fueltypes = st.selectbox(
        "Fuel Type",
        [
            "gas",
            "diesel"
        ]
    )


    # ----------------------------------------
    # ASPIRATION
    # ----------------------------------------

    aspiration = st.selectbox(
        "Aspiration",
        [
            "std",
            "turbo"
        ]
    )


    # ----------------------------------------
    # NUMBER OF DOORS
    # ----------------------------------------

    doornumbers = st.selectbox(
        "Number of Doors",
        [
            "two",
            "four"
        ]
    )


    # ----------------------------------------
    # CAR BODY
    # ----------------------------------------

    carbody = st.selectbox(
        "Car Body",
        [
            "convertible",
            "hatchback",
            "sedan",
            "wagon",
            "hardtop"
        ]
    )


    # ----------------------------------------
    # DRIVE WHEELS
    # ----------------------------------------

    drivewheels = st.selectbox(
        "Drive Wheels",
        [
            "fwd",
            "rwd",
            "4wd"
        ]
    )


    # ----------------------------------------
    # ENGINE LOCATION
    # ----------------------------------------

    enginelocation = st.selectbox(
        "Engine Location",
        [
            "front",
            "rear"
        ]
    )


    # ----------------------------------------
    # ENGINE TYPE
    # ----------------------------------------

    enginetype = st.selectbox(
        "Engine Type",
        [
            "dohc",
            "ohcv",
            "ohc",
            "l",
            "rotor",
            "ohcf",
            "dohcv"
        ]
    )


    # ----------------------------------------
    # NUMBER OF CYLINDERS
    # ----------------------------------------

    cylindernumber = st.selectbox(
        "Number of Cylinders",
        [
            "two",
            "three",
            "four",
            "five",
            "six",
            "eight",
            "twelve"
        ]
    )


    # ----------------------------------------
    # FUEL SYSTEM
    # ----------------------------------------

    fuelsystem = st.selectbox(
        "Fuel System",
        [
            "mpfi",
            "2bbl",
            "mfi",
            "1bbl",
            "spfi",
            "4bbl",
            "idi",
            "spdi"
        ]
    )


# ============================================
# TECHNICAL SPECIFICATIONS
# ============================================

st.subheader("🔧 Technical Specifications")


# Create two columns for numerical inputs
col3, col4 = st.columns(2)


# ============================================
# COLUMN 3 - NUMERICAL FEATURES
# ============================================

with col3:

    # ----------------------------------------
    # WHEELBASE
    # ----------------------------------------

    wheelbase = st.number_input(
        "Wheelbase",
        min_value=0.0,
        value=88.6,
        step=0.1
    )


    # ----------------------------------------
    # CAR LENGTH
    # ----------------------------------------

    carlength = st.number_input(
        "Car Length",
        min_value=0.0,
        value=168.8,
        step=0.1
    )


    # ----------------------------------------
    # CAR WIDTH
    # ----------------------------------------

    carwidth = st.number_input(
        "Car Width",
        min_value=0.0,
        value=64.1,
        step=0.1
    )


    # ----------------------------------------
    # CAR HEIGHT
    # ----------------------------------------

    carheight = st.number_input(
        "Car Height",
        min_value=0.0,
        value=48.8,
        step=0.1
    )


    # ----------------------------------------
    # CURB WEIGHT
    # ----------------------------------------

    curbweight = st.number_input(
        "Curb Weight",
        min_value=0.0,
        value=2548.0,
        step=1.0
    )


    # ----------------------------------------
    # ENGINE SIZE
    # ----------------------------------------

    enginesize = st.number_input(
        "Engine Size",
        min_value=0.0,
        value=130.0,
        step=1.0
    )


    # ----------------------------------------
    # BORE RATIO
    # ----------------------------------------

    boreratio = st.number_input(
        "Bore Ratio",
        min_value=0.0,
        value=3.47,
        step=0.01
    )


    # ----------------------------------------
    # STROKE
    # ----------------------------------------

    stroke = st.number_input(
        "Stroke",
        min_value=0.0,
        value=2.68,
        step=0.01
    )


# ============================================
# COLUMN 4 - NUMERICAL FEATURES
# ============================================

with col4:

    # ----------------------------------------
    # COMPRESSION RATIO
    # ----------------------------------------

    compressionratio = st.number_input(
        "Compression Ratio",
        min_value=0.0,
        value=9.0,
        step=0.1
    )


    # ----------------------------------------
    # HORSEPOWER
    # ----------------------------------------

    horsepower = st.number_input(
        "Horsepower",
        min_value=0.0,
        value=111.0,
        step=1.0
    )


    # ----------------------------------------
    # PEAK RPM
    # ----------------------------------------

    peakrpm = st.number_input(
        "Peak RPM",
        min_value=0.0,
        value=5000.0,
        step=100.0
    )


    # ----------------------------------------
    # CITY MPG
    # ----------------------------------------

    citympg = st.number_input(
        "City MPG",
        min_value=0.0,
        value=21.0,
        step=1.0
    )


    # ----------------------------------------
    # HIGHWAY MPG
    # ----------------------------------------

    highwaympg = st.number_input(
        "Highway MPG",
        min_value=0.0,
        value=27.0,
        step=1.0
    )


# ============================================
# PREDICTION SECTION
# ============================================

st.write("---")

st.subheader("💰 Price Prediction")


# Create the prediction button
if st.button(
    "🚗 Predict Car Price",
    use_container_width=True
):

    try:

        # ====================================
        # CREATE INPUT DATAFRAME
        # ====================================

        # Creating a DataFrame with the SAME
        # column names expected by the trained model
        input_data = pd.DataFrame({

            "symboling": [symboling],

            "name": [name],

            "fueltypes": [fueltypes],

            "aspiration": [aspiration],

            "doornumbers": [doornumbers],

            "carbody": [carbody],

            "drivewheels": [drivewheels],

            "enginelocation": [enginelocation],

            "wheelbase": [wheelbase],

            "carlength": [carlength],

            "carwidth": [carwidth],

            "carheight": [carheight],

            "curbweight": [curbweight],

            "enginetype": [enginetype],

            "cylindernumber": [cylindernumber],

            "enginesize": [enginesize],

            "fuelsystem": [fuelsystem],

            "boreratio": [boreratio],

            "stroke": [stroke],

            "compressionratio": [compressionratio],

            "horsepower": [horsepower],

            "peakrpm": [peakrpm],

            "citympg": [citympg],

            "highwaympg": [highwaympg]
        })


        # ====================================
        # MAKE PREDICTION
        # ====================================

        # Send the input data to the trained model
        prediction = final_model.predict(input_data)


        # ====================================
        # DISPLAY RESULT
        # ====================================

        # Get the predicted price
        predicted_price = prediction[0]


        # Display the result
        st.success(
            f"💰 Estimated Car Price: {predicted_price:,.2f}"
        )


    except Exception as e:

        # Display the error if prediction fails
        st.error(
            f"Prediction Error: {e}"
        )
