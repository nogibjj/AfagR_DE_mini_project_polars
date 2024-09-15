from my_lib.lib import summary, get_data
import matplotlib.pyplot as plt

# Plot distribution of numerical variables
def plot_all_vars(data):
    data.hist(bins=20, figsize=(15, 10), color="blue")
    plt.suptitle("Distribution of Numerical Variables", fontsize=16)
    plt.show()


def save_to_md(data):
    """save summary report to markdown"""
    describe_df = summary(data)
    markdown_table1 = describe_df.to_markdown()
    # Write the markdown table to a file
    with open("summary_statistics.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz](Horsepower_histogram.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz2](Visualization_of_EngineSize_&_MPG_Highway.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz3](correlation_matrix.png)\n")


if __name__ == "__main__":
    data = get_data(
        "https://raw.githubusercontent.com/Utshav-paudel/10-data-analysis-project/d7379235a8d48290c5333b83685d6fca76b5f2f9/dataset/2.%20Cars%20Data1.csv"
    )
    save_to_md(data)
    plot_all_vars(data)
