
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

##Lily's code
def correlation(dataset1, dataset2, header):
    try:
        data = pd.read_csv(open(dataset1))
        data_two = pd.read_csv(open(dataset2))
        x = data[header]
        y = data_two[header]
    except:
        print("please enter the correct file names or column header")
        return

    print(np.corrcoef(x, y))

    plt.scatter(x, y)
    plt.title('A plot to show the correlation ')
    plt.xlabel('Closing Price (header)')
    plt.ylabel(' (' + header + ')')
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='yellow')
    plt.show()
##

def sig_test(dataset1, dataset2, header1, header2, get_diff,crypto):
    data = pd.read_csv(open(dataset1)) #
    data_two = pd.read_csv(open(dataset2)) #
    column_one = data[header1] #
    column_two = data_two[header2] #


    if (get_diff == "T"): #
        i = 1 #
        j = 1 #
        length = len(column_one)-1
        column_one_diff = [0]* length #
        column_two_diff = [0]* length #
        if (crypto):
            column_one_diff = [0] * length  #
            column_two_diff = [0] * length  #
            column_one_diff[0] = abs(column_one[0] - data["24h Open (USD)"][0]) #
            column_two_diff[0] = abs(column_two[0] - data_two["24h Open (USD)"][0]) #
        else:
            column_one_diff = [0] * (length+1)  #
            column_two_diff = [0] * (length+1)  #
            length+=1
            column_one_diff[0] = abs(column_one[0] - column_two[1])  #
            column_two_diff[0] = abs(column_two[0] - column_two[1])  #

            i=2
            j=2

        while (i < length):  #
            column_one_diff[i] = abs(float(column_one[i]) - float(column_one[i - 1]))  #
            i += 1  #

        while (j < length):  #
            column_two_diff[j] = abs(float(column_two[j]) - float(column_two[j - 1]))  #
            j += 1  #
        print(column_one_diff)
        print(column_two_diff)
        ttest, pval = stats.ttest_ind(column_one_diff, column_two_diff)
        column_one_diff_mean = np.mean(column_one_diff)
        column_two_diff_mean = np.mean(column_two_diff)
        print("data one mean value:", column_one_diff_mean)
        print("data two mean value:", column_two_diff_mean)
        data1_std = np.std(column_one_diff)
        data2_std = np.std(column_two_diff)
        print("data one std value:", data1_std)
        print("data two std value:",data2_std)
        print("p-statistic", ttest)
        print("p-value", pval)

    else:
        ttest, pval = stats.ttest_ind(column_one, column_two)
        print("p-value", pval)



def main():
    # speed up testing with the current dataset
    sig_test("XRP_USD_2019-03-02_2019-06-01-CoinDesk.csv","XRP_USD_2020-03-02_2020-06-01-CoinDesk.csv", "Closing Price (USD)", "Closing Price (USD)","T","T") #
    sig_test("BTC_USD_2019-03-02_2019-06-01-CoinDesk.csv", "BTC_USD_2020-03-02_2020-06-01-CoinDesk.csv","Closing Price (USD)", "Closing Price (USD)", "T","T") #
    sig_test("ETH_USD_2019-03-02_2019-06-01-CoinDesk.csv", "ETH_USD_2020-03-02_2020-06-01-CoinDesk.csv","Closing Price (USD)", "Closing Price (USD)", "T","T" ) #
    sig_test("AUDtoUSD2019.csv", "AUDtoUSD2020.csv","USD", "USD", "T","F")
    menu = ''
    while (menu != "exit"):
        print("")
        menu = input("c/C = correlation, s/S = signficance test, h/H = heatmap, exit = exit the program\n")
        if (menu == "c" or menu == "C"):
            dataset1 = input("please enter the name of the first file including the file format, i.e .csv.\n")
            dataset2 = input("please enter the name of the second file including the file format, i.e .csv.\n")
            header = input("please enter the column header.\n")
            correlation(dataset1,dataset2,header)
        if (menu == "s" or menu == "S"):
            dataset1 = input("please enter the name of the first file including the file format, i.e .csv.\n")
            dataset2 = input("please enter the name of the second file including the file format, i.e .csv.\n")
            header = input("please enter the column header for the first dataset.\n")
            header2 = input("please enter the column header for the second dataset.\n")
            get_dif = input("if you would like to get the average different. T or F\n")
            crypto = input("is the data a crypto currency(T/F)")
            sig_test(dataset1,dataset2,header,header2,get_dif,crypto)










if __name__ == '__main__':
    main()