import pandas as pd
import matplotlib.pyplot as plt


def house_price_comparison():
    file = "C:\\Users\\surfy\\PycharmProjects\\CSC3833\\A_housePriceData_2021\\A_housePriceData_2021\\Average-prices-Property-Type-2021-05_wrangled.csv"
    data = pd.read_csv(file)
    filt = pd.DataFrame()
    filt["date"] = pd.to_datetime(data["Date"])
    filt["region_name"] = data["Region_Name"]
    filt["property_type"] = data["propertyType"]
    filt["average_price"] = data["averagePrice"]
    title = "Average house sale prices in London compared to Newcastle upon Tyne 2001 - 2021"
    plt.plot(filt["date"], filt["average_price"])
    plt.title(title, fontsize=12)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Average sale price", fontsize=12)
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    house_price_comparison()

