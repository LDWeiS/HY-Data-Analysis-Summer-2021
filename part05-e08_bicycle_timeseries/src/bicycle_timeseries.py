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
    d.drop('Weekday', axis = 1, inplace = True)

    dt = pd.to_datetime(d)
    dt = pd.DataFrame(dt, columns=['DatetimeIndex'])
    return dt

def bicycle_timeseries():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep = ';')
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    date = split_date(df)

    newdf = pd.merge(date, df, left_index=True, right_index=True)
    newdf.set_index('DatetimeIndex', inplace=True)
    newdf.drop('Päivämäärä', axis = 1, inplace=True)

    return newdf

def main():
    print(bicycle_timeseries())
    return None

if __name__ == "__main__":
    main()