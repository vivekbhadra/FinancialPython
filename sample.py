# Machine Learning for Trading | Georgia Institute of Technology | Udacity
# https://www.udacity.com/course/machine-learning-for-trading--ud501
# Sample Program 1
import pandas as pd

def test_run():
    """Function called by Test Run."""
    df = pd.read_csv("data/AAPL.csv")
    print df.head()


if __name__ == "__main__":
    test_run()

