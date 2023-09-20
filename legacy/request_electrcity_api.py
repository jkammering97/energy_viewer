import requests
import pandas as pd
# %%
auth_token = 'rXsGfloStr8WskzoMwlkFwTXOmNDUXt2'

url = 'https://api-access.electricitymaps.com/2w97h07rvxvuaa1g/power-production-breakdown/forecast?zone=DE'

# Define the headers with the auth-token
headers = {
    'auth-token': auth_token
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse and work with the response data, which is in JSON format
    data = response.json()
    # Now you can access the data as a Python dictionary
    print(data)
else:
    # Handle the case where the request was not successful
    print(f"Request failed with status code {response.status_code}")
# %%
forecast = response.json()['forecast']
forecast_df = pd.DataFrame(forecast)

normalized_df = pd.json_normalize(forecast_df['powerProductionBreakdown'])

# Combine the normalized DataFrame with the original DataFrame
result_df = pd.concat([forecast_df.drop(columns='powerProductionBreakdown'), normalized_df], axis=1)

