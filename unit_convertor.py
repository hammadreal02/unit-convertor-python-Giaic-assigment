import streamlit as st

# app name and layout change
st.set_page_config(page_title="UNIT-CONVERTER",layout="centered")

# title and description
st.title("Unit Convertor")
st.markdown("### Welcome!🥰 to Unit Convertor app ")
st.write("This is a unit convertor app that converts units from one unit to another.")

# category select 
category = st.selectbox("Select a Category",["📏length","⌚Time","⚖️ Weight and Mass","🌡Temperature",'🧪 Volume',"🏃‍♂️ Speed"] )

# input numbers for convert
value = st.number_input("Enter a number to convert", value=1 , min_value=0)

#category selected length
if category == "📏length":
    units ={
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254
    }
    # category of from unit and To unit 
    from_units = st.selectbox("FROM UNIT",list(units.keys()))
    To_units = st.selectbox("TO UNIT",list(units.keys()))

    # user value *  from units value and divided to To units 
    result = value * units[from_units] / units[To_units]
    
    st.success(f'{value} {from_units} = {result} {To_units}')

#  category selected Time
elif category == "⌚Time":
    units = {
        "Seconds": 1,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400,
        "Week": 604800.0,
        "Year": 31536000.0
    }

    from_units = st.selectbox("FROM UNIT",list(units.keys()))
    To_units = st.selectbox("TO UNIT",list(units.keys()))
    result = value * units[from_units] / units[To_units]
    st.success(f'{value} {from_units} = {result} {To_units}')

#if category selected weigth 
elif category == "⚖️ Weight and Mass":
    units ={
        "Tonne":1000,
        "Kilogram":1,
        "Gram":0.001,
        "Pound":0.453592,
        "Ounce":0.0283495
    }   
    from_units = st.selectbox("FROM UNIT",list(units.keys()))
    To_units = st.selectbox("TO UNIT",list(units.keys()))
    result = value * units[from_units] / units[To_units]
    st.success(f'{value} {from_units} = {result} {To_units}')

#if category selected volume
elif category == "🧪 Volume":
    units ={
        "litre":1,
        "Millilitre":0.001,         #1 millilitr = 0.001 litr
        "Gallon": 3.78541,
        "Cubic Meter": 1000.0,
    }
    from_units = st.selectbox("FROM UNIT",list(units.keys()))
    To_units = st.selectbox("TO UNIT",list(units.keys()))
    result = value * units[from_units] / units[To_units]
    st.success(f'{value} {from_units} = {result} {To_units}')

# if category selected speed  
elif category == "🏃‍♂️ Speed":
    units={ 
        "meter per second ": 1.0,
        "kilometer per hour ": 1000.0 / 3600.0,      # 1km/h = 0.27778
        "feet per hour": 0.3048 /3600.0,             # 1ft/h = 0.0000846667 m/s
        "miles per hour": 1609.344 / 3600.0,         # 1mp/h =  0.44704 m/s
    }
    from_units = st.selectbox("FROM",list(units.keys()))
    To_units = st.selectbox("TO",list(units.keys()))
    result = value * units[from_units] / units[To_units]
    st.success(f'{value} {from_units} = {result:.6f} {To_units}')

#if category selected Temperture
elif category == "🌡Temperature":
    from_units = st.selectbox("FROM UNIT",["Celsius","Fahrenheit","kelvin"])
    To_units = st.selectbox("TO UNIT",["Celsius","Fahrenheit","kelvin"])
    
    # condition of temperture units
    # con..   is from units and  To units same than output is value
    if from_units == To_units:
        result = value

    #con..  is celsius to fahrenheit 
    elif from_units == "Celsius" and To_units == "Fahrenheit":
        result =(value * 9/5) + 32

    #con..  is celsius to kelvin
    elif from_units == "Celsius" and To_units == "kelvin":
        result = value + 273.15

    #con..  is fahrenheit to celsius
    elif from_units == "Fahrenheit" and To_units == "Celsius":
        result = (value - 32) * 5/9

    #con..  is fahrenheit to kelvin
    elif from_units == "Fahrenheit" and To_units == "kelvin":
        result = (value - 32) * 5/9 + 273.15

    #con..  is kelvin to Celsius
    elif from_units == "kelvin" and To_units == "Celsius":
        result = value - 273.15

    #con..  is kelvin to fahrenheit
    elif from_units == "kelvin" and To_units == "Fahrenheit":
        result = (value - 273.15) *9/5 + 32

    # success message is user value from units = result To units

    # ex: category select temperture and value is 120 and select from unit is kelvin and To units is fahrenheit.
    # than success message is "120 kelvin =  -53.083 fahrenheit" 
    # (result:.3f)means after . three number 
    st.success(f'{value} {from_units} =  {result:.5f} {To_units}')    
