from my_lib.lib import get_data, get_mean, get_median, summary
import polars as pd


link = "https://raw.githubusercontent.com/Utshav-paudel/10-data-analysis-project/d7379235a8d48290c5333b83685d6fca76b5f2f9/dataset/2.%20Cars%20Data1.csv"


def test_get_data():
    """test that loading the csv will work"""
    df = get_data(link)
    assert df is not None, "The dataframe can not be empty"
    assert df.shape == (432, 15), "The shape of the DataFrame is incorrect"


def test_stats():
    """test that checks the data operations is working"""
    df = get_data(link)
    mean_test = get_mean(df, "Cylinders")
    median_test = get_median(df, "Cylinders")
    describe_test = summary(df)
    mean_from_summary = (
        describe_test.filter(pd.col("statistic") == "mean").select("Cylinders").item()
    )
    median_from_summary = (
        describe_test.filter(pd.col("statistic") == "50%").select("Cylinders").item()
    )

    # Assert they match
    assert (
        mean_from_summary == mean_test
    ), f"Expected mean: {mean_test}, but got {mean_from_summary}"
    assert (
        median_from_summary == median_test
    ), f"Expected median: {median_test}, but got {median_from_summary}"
    assert describe_test is not None, "The summary statistics should not be None"


if __name__ == "__main__":
    test_get_data()
    test_stats()
