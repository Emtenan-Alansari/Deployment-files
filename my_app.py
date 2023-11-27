# Streamlit Documentation: https://docs.streamlit.io/


import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image  # to deal with images (PIL: Python imaging library)

# Title/Text
st.title("Welcome to Car Price Prediction Project ")
st.text("This is some test.")

# Markdown
st.markdown("Streamlit is **_really_ cool** :+1:")
st.markdown("## Emtenan Yasir Alansari")
st.markdown("### SDA1007-Emtenan")

# Header/Subheader
st.header('CLARUSWAY with SDA')
st.subheader('Group 1')

# Success/Info/Error
st.success('This is a success message!')
st.info('This is a purely informational message')
st.error("This is an error.")
st.warning("This is a warning message!")
st.exception("NameError('name there is not defined')")


# Dataframe
df=pd.read_csv("Ready_to_ML.csv")

# To display dataframe there are 3 methods

# Method 1
st.table(df.head())
# Method 2
st.write(df.head())  # dynamic, you can sort
st.write(df.isnull().sum())
# Method 3
st.dataframe(df.describe().T)  # dynamic, you can sort

# To load machine learning model
import pickle
filename = "LASSO_Emtenan_model.sav"
model=pickle.load(open(filename, "rb"))

# df_new = df[["make_model", "power_kW", "mileage","age", "engine_size", "type", "price"]]
make_model = st.selectbox("The car model", df.make_model.unique().tolist())
power_kW = st.slider("Select power KW", min_value=float(df.power_kW.min()),
                      max_value=float(df.power_kW.max()))
mileage = st.number_input("Enter mile age", min_value = int(df.age.min()), max_value = int(df.age.max()), step=10)
age = st.number_input("Enter car age", min_value = int(df.age.min()), max_value = int(df.age.max()), step=1)
engine_size = st.slider("Enter the engine size",min_value = float(df.engine_size.min()), max_value = float(df.engine_size.max()))
type = st.selectbox("The car type", df.type.unique().tolist())
my_dict = {'make_model':make_model,
            'mileage': mileage,
           'engine_size':engine_size,
            'age':age,
            'power_kW':power_kW,
            'type':type
           }
df = pd.DataFrame.from_dict([my_dict])
st.table(df)
# Prediction with user inputs
predict = st.button("Predict")
result = model.predict(df)
if predict :
    st.subheader('The car price is: ')
    st.info(result[0].__round__(4))
