from pandas import DataFrame, Series, date_range

## Analysis goes here

## Model creation goes here

# Predict function
def predict_temperatures(n: int) -> DataFrame:
    guess = 15
    dates = date_range(start='2010-09-01', periods=n, freq='MS')
    temperatures = Series([guess] * n, name='LandAverageTemperature')
    return DataFrame({'dt': dates, 'LandAverageTemperature': temperatures})