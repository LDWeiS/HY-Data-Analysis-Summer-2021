#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    conDay = {"ma" : "Mon",
                "ti" : "Tue",
                'ke' : 'Wed',
                'to' : 'Thu',
                'pe' :'Fri',
                'la' : 'Sat',
                'su' : 'Sun'}

    conMonth = {'tammi' :1,
                'helmi' :2,
                'maalis' :3,
                'huhti' :4,
                'touko' :5,
                'kesä' :6,
                'heinä' :7,
                'elo' :8,
                'syys' :9,
                'loka' :10,
                'marras' :11,
                'joulu' :12}

    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    hourmin = d["Hour"].str.split(":", expand=True)

    d["Hour"] = hourmin.iloc[:,0]
    d["Weekday"] = d["Weekday"].map(conDay)
    d["Month"] = d["Month"].map(conMonth)

    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})

    return d

def main():
    data = split_date()
    print(data)
    
       
if __name__ == "__main__":
    main()
