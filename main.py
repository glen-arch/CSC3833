import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches


def house_price_comparison():
    ax1 = plt.subplot(2, 2, 1)
    file = "A_housePriceData_2021\\A_housePriceData_2021\\Average-prices-Property-Type-2021-05_wrangled.csv"
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
    ax1.set_title("Average house sale prices in London compared to \nNewcastle upon Tyne by house type 2001 - 2021")
    ax1.plot(pd.to_datetime(london_detached["Date"]), london_detached["averagePrice"], label="Detached", color="#a6cee3")
    ax1.plot(pd.to_datetime(london_semi_detached["Date"]), london_semi_detached["averagePrice"], label="Semi detached", color="#1f78b4")
    ax1.plot(pd.to_datetime(london_terraced["Date"]), london_terraced["averagePrice"], label="Terraced", color="#b2df8a")
    ax1.plot(pd.to_datetime(london_flats["Date"]), london_flats["averagePrice"], label="Flat", color="#33a02c")
    ax1.plot(pd.to_datetime(newcastle_detached["Date"]), newcastle_detached["averagePrice"], color="#a6cee3", linestyle="--")
    ax1.plot(pd.to_datetime(newcastle_semi_detached["Date"]), newcastle_semi_detached["averagePrice"], color="#1f78b4", linestyle="--")
    ax1.plot(pd.to_datetime(newcastle_terraced["Date"]), newcastle_terraced["averagePrice"], color="#b2df8a", linestyle="--")
    ax1.plot(pd.to_datetime(newcastle_flats["Date"]), newcastle_flats["averagePrice"], color="#33a02c", linestyle="--")
    legend = ax1.legend(title="London", loc="upper left", edgecolor="#000000")
    ax1.add_artist(legend)
    legend_elements = [plt.Line2D([0], [0], color='#a6cee3', linestyle='--', label='Detached'),
                       plt.Line2D([0], [0], color='#1f78b4', linestyle='--', label='Semi detached'),
                       plt.Line2D([0], [0], color='#b2df8a', linestyle='--', label='Terraced'),
                       plt.Line2D([0], [0], color='#33a02c', linestyle='--', label='Flat')]
    ax1.legend(title="Newcastle upon Tyne", handles=legend_elements, bbox_to_anchor=(0.583, 1), edgecolor="#000000")
    ax1.get_yaxis().get_major_formatter().set_scientific(False)
    ax1.set_xlim(pd.to_datetime("2001-04-01"), pd.to_datetime("2021-04-01"))
    ax1.grid(True)
    ax1.set_ylim(0, 1000000)
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Sale price (£)")


def broadband_comparison():
    ax2 = plt.subplot(2, 2, 2)
    file = "B_broadbandData_2021\\B_broadbandData_2021\\202006_fixed_laua_performance_wrangled.csv"
    data = pd.read_csv(file)
    file = "Regression.csv"
    regression = pd.read_csv(file)
    ax2.plot(regression["y"], regression["x"], color="#ca0020", label="Line of best fit")
    correlation = "The correlation between a\nregions average upload\nand download speeds is \n" + str(data["averageDown"].corr(data["averageUpload"]))
    ax2.scatter(data["averageDown"], data["averageUpload"], s=5, color="#f4a582")
    ax2.scatter(163, 24, label="Kingston upon Hull", color="#92c5de", s=10)
    ax2.scatter(147.1, 98.1, label="York", color="#0571b0", s=10)
    hull = patches.Rectangle((158, 19), 10, 10, fill=False, color="black", linestyle="--", label="Outlier")
    york = patches.Rectangle((142.1, 93.1), 10, 10, fill=False, color="black", linestyle="--")
    ax2.add_patch(hull)
    ax2.add_patch(york)
    ax2.set_xlabel("Average download speed (Mbit/s)")
    ax2.set_ylabel("Average upload speed (Mbit/s)")
    ax2.set_xlim(20, 170)
    ax2.set_ylim(0, 110)
    ax2.legend(bbox_to_anchor=(1, 1.02), edgecolor="#000000")
    ax2.text(172, 50, correlation)
    ax2.set_title("A comparison of regional average broadband \nupload and download speeds")
    ax2.set_aspect(1)
    ax2.grid(True)


def stock_exchange():
    ax3 = plt.subplot(2, 2, 3)
    file = "C_financialData_2021\\C_financialData_2021\\ftse_data_wrangled.csv"
    data = pd.read_csv(file)
    sma = data["Close"].rolling(90).mean()
    std = data["Close"].rolling(90).std()
    ax3.plot(pd.to_datetime(data["date"]), sma, color="b", label="Sale price")
    ax3.plot(pd.to_datetime(data["date"]), sma + std * 2, linestyle="--", color="g", label="Bollinger up band")
    ax3.plot(pd.to_datetime(data["date"]), sma - std * 2, linestyle="--", color="r", label="Bollinger down band")
    ax3.set_ylim(0, 9000)
    ax3.set_xlim(pd.to_datetime("1984-04-01"), pd.to_datetime("2021-10-08"))
    mean_line = [data["Close"].mean()] * data["date"].count()
    ax3.plot(pd.to_datetime(data["date"]), mean_line, linestyle="--", label="Average sale price", color="black", dashes=(3, 3))
    ax3.set_ylabel("Stock price (£)")
    ax3.set_xlabel("Date")
    ax3.set_title("Stock price of FTSE from 1984-2021")
    ax3.fill_between(pd.to_datetime(data["date"]), sma, color="lightblue")
    ax3.legend(edgecolor="#000000", loc="upper left")
    ax3.grid(True)


def observations():
    ax4 = plt.subplot(2, 2, 4)
    text = open("observations.txt", "r")
    ax4.text(0.01, 0.05, text.read(), fontsize="8")
    ax4.text(0.35, 0.94, "Summary of each plot", fontsize="12")
    ax4.set_axis_off()
    box = patches.Rectangle((0, 0), 1, 1, fill=False, color="black")
    ax4.add_patch(box)


if __name__ == '__main__':
    fig = plt.figure(figsize=(16, 9), dpi=120)
    house_price_comparison()
    broadband_comparison()
    stock_exchange()
    observations()
    plt.subplots_adjust(hspace=0.3)
    plt.show()
    #plt.savefig("CSC3833.png", dpi=120)