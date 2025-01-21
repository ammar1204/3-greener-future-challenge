from pandas import DataFrame, Series

## Analysis goes here

## Model creation goes here

# Predict function
def predict_something(some_input: DataFrame) -> Series:
    guess = 50
    return Series([guess] * len(some_input), name='target_column')