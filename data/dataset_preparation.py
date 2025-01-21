import pandas as pd
from sklearn.model_selection import train_test_split
import os

base_path = os.path.dirname(__file__)
data_path = os.path.join(base_path, 'original.csv')

data = pd.read_csv(data_path)

# Select features and target
features = data.drop(columns=['LandAverageTemperature'])
target = data['LandAverageTemperature']

# Train/Test split 70% to 30%
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.02, random_state=42, shuffle=False)

# Save the splits to CSV files
train_data = pd.concat([X_train, y_train], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)

# Find the latest date in train_data
latest_date = train_data['dt'].max()
print("Latest date in train_data:", latest_date)

train_data.to_csv(os.path.join(base_path, 'GlobalTemperatures.csv'), index=False)
test_data.to_csv(os.path.join(base_path, 'test.csv'), index=False)

# Load the additional datasets
country_data_path = os.path.join(base_path, 'country-original.csv')
state_data_path = os.path.join(base_path, 'state-original.csv')

country_data = pd.read_csv(country_data_path)
state_data = pd.read_csv(state_data_path)

# Truncate the datasets based on the latest date in train_data
country_data_truncated = country_data[country_data['dt'] <= latest_date]
state_data_truncated = state_data[state_data['dt'] <= latest_date]

# Save the truncated datasets to CSV files
country_data_truncated.to_csv(os.path.join(base_path, 'GlobalLandTemperaturesByCountry.csv'), index=False)
state_data_truncated.to_csv(os.path.join(base_path, 'GlobalLandTemperaturesByState.csv'), index=False)
