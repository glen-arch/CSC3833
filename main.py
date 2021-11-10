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
    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.suptitle(title, fontsize=12)
    ax1.plot(filt["date"], filt["average_price"])
    ax1.grid(True)
    ax2.plot(filt["date"], filt["average_price"])
    ax2.grid(True)
    plt.show()


if __name__ == '__main__':
    house_price_comparison()

