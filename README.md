# Dicoding-Air Quality Index
This project is submitted for the "Learn Data Analysis with Python" from Dicoding. Focusing on analyzing Air Quality in Aotizhongxin to uncover trends and correlation between air polution and meteorology variable (rainfall, dew point, etc).

## Live Dashboard
https://dicoding-aqi-eufcxt5rskdytpvw3dbxte.streamlit.app/
## Project Structure
Dashboard : Streamlit dashboard
Data : AQI Aotizhongxin Data

## Installation
git clone https://github.com/oohgan/Dicoding-AQI
cd Dicoding-AQI
conda create --name main python=3.9
conda activate main
pip install streamlit
pip install -r requirements.txt

## Run Streamlit
cd Dashboard
streamlit run dashboard.py