#!/usr/bin/env python3

import pandas as pd

days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1, 13)))

def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    
    hourmin = d["Hour"].str.split(":", expand=True)
    
    d["Hour"] = hourmin.iloc[:, 0]
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    
    return d

def split_date_continues():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    
    d = split_date(df)
    df = df.drop("Päivämäärä", axis=1)
    result = pd.concat([d, df], axis=1)
    
    return result

def cycling_weather():
    df1 = split_date_continues()
    df2 = pd.read_csv("src/kumpula-weather-2017.csv", sep=",")

    df = pd.merge(df1, df2, left_on=['Day', 'Month', 'Year'], right_on=['d', 'm', 'Year']).drop(['m', 'd', 'Time', 'Time zone'], axis=1)

    return df

def main():
    print(cycling_weather())

if __name__ == "__main__":
    main()
