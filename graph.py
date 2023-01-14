import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame


def death_statistics_by_location(dataframe: DataFrame, location: str) -> DataFrame:
    return dataframe.loc[dataframe['location'] == location, ['location', 'date', 'total_deaths']]


def create_graph(dataframe: DataFrame, x: str, y: str) -> None:
    plt.rcParams['figure.figsize'] = [10, 10]
    try:
        dataframe.plot(x=x, y=y, grid=True, linewidth=3)
    except KeyError:
        print("Invalid column names")
        return
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('./resources/df_covid19_countries.csv', sep=',', parse_dates=['date'])
    print('Input location: ')
    location = str(input())
    df = death_statistics_by_location(df, location)
    if not df.empty:
        create_graph(df, 'date', 'total_deaths')
