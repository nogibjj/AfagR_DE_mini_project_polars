from my_lib.lib import summary, get_data
import matplotlib.pyplot as plt
import polars as pd
from tabulate import tabulate


# Plot distribution of numerical variables
def plot_all_vars(data):
    numeric_columns = data.select(
        [pd.col(c) for c in data.columns if data[c].dtype in [pd.Float64, pd.Int64]]
    )
    num_columns = numeric_columns.columns
    fig, axes = plt.subplots(
        len(num_columns) // 2 + 1, 2, figsize=(14, 20)
    )  # 2 columns layout

    axes = axes.flatten()

    for i, col in enumerate(num_columns):
        axes[i].hist(numeric_columns[col].to_numpy(), bins=20, color="blue")
        axes[i].set_title(f"Distribution of {col}")

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.suptitle("Distribution of Numerical Variables", fontsize=16)
    plt.subplots_adjust(hspace=0.4, wspace=0.4)
    plt.savefig("All_features_distribution.png")
    plt.show()


def save_to_md(data):
    """Save summary report to markdown"""
    describe_df = summary(data)

    headers = describe_df.columns
    data_rows = describe_df.to_numpy().tolist()

    markdown_table = tabulate(data_rows, headers, tablefmt="github")

    # Write the markdown table to a file
    with open("summary_statistics.md", "w", encoding="utf-8") as file:
        file.write("# Summary Statistics Report\n\n")
        file.write("## Describe:\n")
        file.write(markdown_table)
        file.write("\n\n")  # Add a new line
        file.write("![Horsepower Histogram](Horsepower_histogram.png)\n")
        file.write("\n\n")  # Add a new line
        file.write(
            "![Engine Size & MPG Highway Visualization](Visualization_of_EngineSize_&_MPG_Highway.png)\n"
        )
        file.write("\n\n")  # Add a new line
        file.write("![Correlation Matrix](correlation_matrix_polars.png)\n")


if __name__ == "__main__":
    data = get_data(
        "https://raw.githubusercontent.com/Utshav-paudel/10-data-analysis-project/d7379235a8d48290c5333b83685d6fca76b5f2f9/dataset/2.%20Cars%20Data1.csv"
    )
    save_to_md(data)
    plot_all_vars(data)
