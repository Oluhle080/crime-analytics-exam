import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ======= Historical data (example) =======
df = pd.DataFrame({
    'Month': pd.date_range(start='2020-01-01', periods=24, freq='M'),
    'Crime_Count': [25, 28, 26, 30, 27, 31, 29, 35, 32, 30, 28, 27, 29, 32, 31, 34, 36, 35, 33, 31, 28, 26, 25, 27]
})
df.set_index('Month', inplace=True)

# ======= Forecast data (example) =======
forecast = pd.DataFrame({
    'ds': pd.date_range(start='2022-01-31', periods=12, freq='M'),
    'yhat': [30, 32, 31, 33, 35, 34, 32, 30, 29, 27, 26, 28],
    'yhat_lower': [28, 30, 29, 30, 33, 32, 30, 28, 27, 25, 24, 26],
    'yhat_upper': [32, 34, 33, 36, 37, 36, 34, 32, 31, 29, 28, 30]
})

mae = 11.46
rmse = 12.44

# ======= Forecasting Section =======
st.header("Crime Forecasting")
st.write("Review predicted monthly crime trends for selected type.")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df.index, df['Crime_Count'], label='Historical', marker='o')
ax.plot(forecast['ds'], forecast['yhat'], label='Forecast', color='orange')
ax.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'],
                color='orange', alpha=0.2, label='Confidence Interval')
ax.set_title('Crime Forecasting: Historical and Predicted')
ax.set_xlabel('Date')
ax.set_ylabel('Incident Count')
ax.legend()
st.pyplot(fig)

st.dataframe(forecast)

st.markdown(f"**Mean Absolute Error (MAE):** {mae:.2f}")
st.markdown(f"**Root Mean Squared Error (RMSE):** {rmse:.2f}")

st.markdown("""
**Forecast Interpretation:**  
The orange line and shaded area represent model predictions and uncertainty for the next 12 months.  
Notice the spike in December, indicating a possible need for increased patrols.  
These insights can support law enforcement planning and resource allocation.
""")
