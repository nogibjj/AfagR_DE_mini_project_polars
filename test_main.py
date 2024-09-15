from my_lib.lib import get_data
from main import save_to_md, plot_all_vars

link = "https://raw.githubusercontent.com/Utshav-paudel/10-data-analysis-project/d7379235a8d48290c5333b83685d6fca76b5f2f9/dataset/2.%20Cars%20Data1.csv"


def test_plot_all_vars():
    """test describe is actually working"""
    df = get_data(link)
    plot_all_vars(df)
    assert df is not None


def test_summary_and_viz_to_markdown():
    df = get_data(link)
    """converts to markdown()"""
    save_to_md(df)


if __name__ == "__main__":
    test_plot_all_vars()
    test_summary_and_viz_to_markdown()
