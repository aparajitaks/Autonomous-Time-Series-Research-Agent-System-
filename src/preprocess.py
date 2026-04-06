import pandas as pd

def preprocess_data(df):
    df=df[['Date','Close']]
    df.loc[:,'Date']=pd.to_datetime(df['Date'])
    df=df.sort_values("Date")
    df.set_index("Date",inplace=True)
    df=df.asfreq('D')
    df = df.ffill()  # Fill missing values using forward fill
    df.rename(columns={"Date":"y"},inplace=True)
    return df
    




           