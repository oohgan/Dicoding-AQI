import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


df_imputed = pd.read_csv("Dashboard/df_imputed.csv")

datetime_columns = ["date"]
df_imputed.sort_values(by="date", inplace=True)
df_imputed.reset_index(inplace=True)
    
for column in datetime_columns:
    df_imputed[column] = pd.to_datetime(df_imputed[column])

# Filter date
min_date = df_imputed["date"].min()
max_date = df_imputed["date"].max()
    
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://seeklogo.com/images/S/streamlit-logo-1A3B208AE4-seeklogo.com.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Date Filter',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

st.header('Kualitas Udara di Aotizhongxin')

main_df = df_imputed[(df_imputed["date"] >= str(start_date)) & 
                (df_imputed["date"] <= str(end_date))]

groupYear = main_df.groupby("date").mean(numeric_only=True)
st.subheader("PM2.5")
fig = plt.figure(figsize=(10,6))
plt.plot(groupYear.index, groupYear["PM2.5"], label="PM2.5")
plt.xlabel("Date")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("PM10")
fig = plt.figure(figsize=(10,6))
plt.plot(groupYear.index, groupYear["PM10"], label="PM10")
plt.xlabel("Date")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("NO2")
fig = plt.figure(figsize=(10,6))
plt.plot(groupYear.index, groupYear["NO2"], label="NO2")
plt.xlabel("Date")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("SO2")
fig = plt.figure(figsize=(10,6))
plt.plot(groupYear.index, groupYear["SO2"], label="SO2")
plt.xlabel("Date")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)

# groupYear = main_df.groupby("date").mean(numeric_only=True)
st.subheader("Kualitas Udara Aotizhongxin")
fig = plt.figure(figsize=(10, 6))
plt.plot(groupYear.index, groupYear["PM2.5"], label="PM2.5")
plt.plot(groupYear.index, groupYear["PM10"], label="PM10")
plt.plot(groupYear.index, groupYear["NO2"], label="NO2")
plt.plot(groupYear.index, groupYear["SO2"], label="SO2")
plt.plot(groupYear.index, groupYear["O3"], label="O3")
plt.xlabel("Date")
plt.ylabel("Concetration (µm/m3)")
plt.title("Polusi Udara di Aotiziahn 2013 - 2017")
plt.legend()
st.pyplot(fig)

voi = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3",
       "TEMP", "PRES", "DEWP", "RAIN", "WSPM"]
subset_df = df_imputed[voi]
correlation_matrix = subset_df.corr()
st.subheader("Heatmap Korelasi Polusi Udara & Meteorologi")
fig = plt.figure(figsize=(13,9))
sns.heatmap(correlation_matrix, cmap='Reds', annot=True)
plt.title('Korelasi Polusi Udara di Aotizhongxin')
st.pyplot(fig)
