# Machine Learning for Trading | Georgia Institute of Technology | Udacity
# https://www.udacity.com/course/machine-learning-for-trading--ud501
# Sample Program 1
import pandas as pd

def test_run():
    """Function called by Test Run."""
    df = pd.read_csv("data/AAPL.csv")
    print df.head() # prints first 5 lines from the file
    print df.tail() # prints last 5 lines from the file


if __name__ == "__main__":
    test_run()

# Sample Program 2
"""Compute mean volume"""

import pandas as pd

def get_mean_volume(symbol):
    """Return the mean volume for stock indicated by symbol.
    
    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol))  # read in data
    return df['Volume'].mean()

def test_run():
    """Function called by Test Run."""
    for symbol in ['AAPL', 'IBM']:
        print "Mean Volume"
        print symbol, get_mean_volume(symbol)


if __name__ == "__main__":
    test_run()

# Sample Program 3
"""Plot High prices for IBM"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/IBM.csv")
    df['High'].plot()
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    test_run()
