from sktime.forecasting.arima import ARIMA

def train_model(train_data):
    model=ARIMA()
    model.fit(train_data)
    return model