import pandas as pd
from fbprophet import Prophet

# Load the data
df = pd.read_csv('mbb.csv')

# Prepare the data for Prophet
df = df[['Date', 'Close']]  # select only the columns needed
df = df.rename(columns={'Date': 'ds', 'Close': 'y'})  # rename the columns for Prophet
df['ds'] = pd.to_datetime(df['ds'])  # convert the 'ds' column to a datetime type

# Train the Prophet model
model = Prophet()
model.fit(df)

# Make a prediction for the next 30 days
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Print the predicted values for the next 30 days
print(forecast[['ds', 'yhat']].tail(30))
