#!/usr/bin/env python3

import pandas as pd

def suicide_fractions(df):
    df['ratio'] = df['suicides_no']/df['population']
    fdata = df.groupby('country').mean()
    return fdata['ratio']   

def suicide_weather():
    countryWeather = pd.read_html('src/List_of_countries_by_average_yearly_temperature.html')
    countryWeather = countryWeather[0]
    countryWeather = countryWeather.set_index(countryWeather.columns[0])
    countryWeather = countryWeather.iloc[:, 0].str.replace("\u2212", "-").astype(float)

    whoStat = pd.read_csv('src/who_suicide_statistics.csv')
    whoRatio = suicide_fractions(whoStat)

    combined = pd.merge(countryWeather, whoRatio, left_index=True, right_index=True)
    corr = combined.corr(method='spearman').iloc[0, 1]
    (suicide_rows, temperature_rows, common_rows) = (x.shape[0] for x in [whoRatio, countryWeather, combined])
    return suicide_rows, temperature_rows, common_rows, corr

def main():
    sRow, tempRow, comRow, spearman = suicide_weather()
    print(f"""Suicide DataFrame has {sRow} rows \nTemperature DataFrame has {tempRow} rows \nCommon DataFrame has {comRow} rows \nSpearman correlation: {spearman} """)
    return

if __name__ == "__main__":
    main()
