import polars as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn.objects as so
import seaborn as sns
from matplotlib import style

sns.set_style("whitegrid")


def get_data(dataset):
    data = pd.read_csv(dataset)
    return data


def get_mean(df, col):
    return df.select(pd.col(col).mean()).item()


def get_median(df, col):
    return df.select(pd.col(col).median()).item()


def summary(df):
    return df.describe()


def vizualisation(data, first_column="EngineSize", second_column="Horsepower"):
    sns.set_style("whitegrid")

    # Extract Polars columns as lists
    x = data[first_column].to_list()
    y = data[second_column].to_list()

    plot_data = {first_column: x, second_column: y}

    my_chart = (
        so.Plot(plot_data, first_column, second_column)
        .add(so.Line(color="r"), so.PolyFit(order=2))
        .add(so.Dot())
        .label(title=f"Visualization of {first_column} and {second_column}")
    )
    my_chart.save(f"Visualization_of_{first_column}_&_{second_column}.png")
    return my_chart


def create_histogram(df, column="Horsepower"):
    plt.figure(figsize=(10, 6))

    # Extract the column data as a list for plotting
    values = df[column].to_list()

    # Create histogram using Matplotlib
    plt.hist(values, bins=20, color="blue", edgecolor="black")
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig(f"{column}_histogram.png")
    plt.show()


def correlation_matrix(df):
    df_numerical = df.select(pd.col(pd.Float64))

    corr_matrix = df_numerical.corr().to_numpy()

    plt.figure(figsize=(14, 10))
    plt.matshow(corr_matrix, cmap="coolwarm", fignum=1)
    plt.title("Correlation Matrix", pad=20)
    plt.colorbar()
    plt.savefig("correlation_matrix.png")
    plt.show()


# def vizualisation(data,first_column = 'EngineSize',second_column = 'Horsepower'):
#     sns.set_style('whitegrid')
#     my_chart = (
#         so.Plot(data, first_column, second_column).add(so.Line(color='r'), so.PolyFit(order=2)).add(so.Dot())
#         .label(title= f"Visualization of {first_column} and {second_column}"))
#     my_chart.save(f"Visualization_of_{first_column}_&_{second_column}.png")
#     return my_chart


# def create_histogram(df, column = 'Horsepower'):
#     plt.figure(figsize=(10,6))
#     plt.hist(df[column], bins = 20, color='blue', edgecolor='black')
#     plt.title(f'Distribution of {column}')
#     plt.xlabel(column)
#     plt.ylabel('Frequency')
#     plt.grid(True)
#     plt.savefig(f'{column}_histogram.png')
#     plt.show()


# def correlation_matrix(df):
#     df = df.select_dtypes(float)
#     plt.figure(figsize=(14,10))
#     plt.matshow(df.corr(), cmap='coolwarm',)
#     plt.title('Correlation Matrix', pad=20)
#     plt.colorbar()
#     plt.savefig('correlation_matrix.png')
#     plt.show()
