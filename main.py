import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def house_price_comparison():
    file = "C:\\Users\\surfy\\PycharmProjects\\CSC3833\\A_housePriceData_2021\\A_housePriceData_2021\\Average-prices-Property-Type-2021-05_wrangled.csv"
    data = pd.read_csv(file)
    london = data[data["Region_Name"] == "London"]
    london_detached = london[london.propertyType == "Detached"]
    london_semi_detached = london[london.propertyType == "Semi_Detached"]
    london_terraced = london[london.propertyType == "Terraced"]
    london_flats = london[london.propertyType == "Flat"]
    newcastle = data[data["Region_Name"] == "Newcastle upon Tyne"]
    newcastle_detached = newcastle[newcastle.propertyType == "Detached"]
    newcastle_semi_detached = newcastle[newcastle.propertyType == "Semi_Detached"]
    newcastle_terraced = newcastle[newcastle.propertyType == "Terraced"]
    newcastle_flats = newcastle[newcastle.propertyType == "Flat"]
    title = "Average house sale prices in London compared to Newcastle upon Tyne 2001 - 2021"
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle(title, fontsize=12)
    ax1.plot(pd.to_datetime(london_detached["Date"]), london_detached["averagePrice"], label="Detached")
    ax1.plot(pd.to_datetime(london_semi_detached["Date"]), london_semi_detached["averagePrice"], label="Semi detached")
    ax1.plot(pd.to_datetime(london_terraced["Date"]), london_terraced["averagePrice"], label="Terraced")
    ax1.plot(pd.to_datetime(london_flats["Date"]), london_flats["averagePrice"], label="Flat")
    ax1.legend()
    ax1.set_title("London", fontsize=12)
    ax1.grid(True)
    ax1.set_xlabel("Year of sale")
    ax1.set_ylabel("Sale price")
    ax2.plot(pd.to_datetime(newcastle_detached["Date"]), newcastle_detached["averagePrice"], label="Detached")
    ax2.plot(pd.to_datetime(newcastle_semi_detached["Date"]), newcastle_semi_detached["averagePrice"],
             label="Semi detached")
    ax2.plot(pd.to_datetime(newcastle_terraced["Date"]), newcastle_terraced["averagePrice"], label="Terraced")
    ax2.plot(pd.to_datetime(newcastle_flats["Date"]), newcastle_flats["averagePrice"], label="Flat")
    ax2.legend()
    ax2.set_title("Newcastle", fontsize=12)
    ax2.grid(True)
    ax2.set_xlabel("Year of sale")
    ax2.set_ylabel("Sale price (£)")
    plt.show()


def broadband_comparison():
    file = "C:\\Users\\surfy\\PycharmProjects\\CSC3833\\B_broadbandData_2021\\B_broadbandData_2021\\202006_fixed_laua_performance_wrangled.csv"
    data = pd.read_csv(file)
    m, b = np.polyfit(data["averageDown"], data["averageUpload"], 1)
    plt.plot(data["averageDown"], m*data["averageDown"] + b, color="red", label="Line of best fit")
    plt.scatter(data["averageDown"], data["averageUpload"], s=1)
    plt.xlabel("Average download speed (Mbit/s)")
    plt.ylabel("Average upload speed (Mbit/s)")
    plt.legend()
    plt.title("A comparison of broadband upload and download speeds")
    plt.show()


def stock_exchange():
    test = "£"


if __name__ == '__main__':
    broadband_comparison()
