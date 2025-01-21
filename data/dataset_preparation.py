import pandas as pd
from sklearn.model_selection import train_test_split
import os

base_path = os.path.dirname(__file__)
data_path = os.path.join(base_path, 'original.csv')

data = pd.read_csv(data_path)

# Select features and target
features = data.drop(columns=['average_score'])
target = data['average_score']

# Train/Test split 70% to 30%
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

# Save the splits to CSV files
train_data = pd.concat([X_train, y_train], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)

train_data.to_csv(os.path.join(base_path, '{}.csv'), index=False)
test_data.to_csv(os.path.join(base_path, 'test.csv'), index=False)
