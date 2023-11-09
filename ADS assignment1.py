import matplotlib.pyplot as plt
import pandas as pd


def lineplot(df, headers):
    """Plot a line chart to visualize data.

    Parameters:
        - df (dataframe): The dataset to be visualized.
        - headers (list of strings): A list of column names to be plotted.

    Example:
        >>> lineplot(df, ['column1', 'column2'])

    Returns:
        None
    """

    plt.figure(figsize=(12, 12))

    for head in headers:
        plt.plot(df["release_year"], df[head], label=head)

    # labelling
    plt.xlabel("Release Year")
    plt.ylabel("No of Releases")

    # removing white space left and right. Both standard and pandas min/max
    # can be used
    plt.xlim(min(df["release_year"]), df["release_year"].max())

    plt.legend()
    plt.title("No of Movies/shows trend on netflix: 1950-2021.")
    plt.savefig("linplot.png")
    plt.show()

    return


def pieplot(df):
    """Plot a pie chart to visualize data.

    Parameters:
        - df (dataframe): The dataset to be visualized.

    Example:
        >>> pieplot(df)

    Returns:
        None
    """


    plt.figure(figsize=(6, 6))

    total = df["count"].sum()

    labels = ["Movie", "Tv Show"]
    df["count"] = (df["count"] / total) * 100
    colors = ["skyblue", "orange"]
    explode = (0, 0)

    plt.pie(
        df["count"],
        explode=explode,
        labels=labels,
        colors=colors,
        autopct="%1.1f%%",
        shadow=True,
        startangle=140,
    )

    plt.legend()
    plt.title("Percentage of Movies/shows on netflix")
    plt.savefig("pieplot.png")
    plt.show()

    return


def barplot(df):
    """Plot a Bar chart to visualize data.

    Parameters:
        - df (dataframe): The dataset to be visualized.

    Example:
        >>> barchart(df)

    Returns:
        None
    """

    plt.bar(df["imdb_score"], df["count"])

    plt.title("IMDB ratings breakdown on netflix shows/movies.")
    plt.xlabel("IMDB Rating")
    plt.ylabel("No of Movies/shows")

    plt.legend()
    plt.savefig("barplot.png")
    plt.show()

    return


def main():
    """Plot Three Different chart to visualize data.

    Parameters:
        None

    Returns:
        None
    """
    csv_file_path = "datasets/titles.csv"

    df = pd.read_csv(csv_file_path)

    summary_release = (
        df.groupby(["release_year", "type"]).size().to_frame("count").reset_index()
    )

    pivoted_df = (
        summary_release.pivot(index="release_year", columns="type", values="count")
        .fillna(0)
        .reset_index()
    )
    lineplot(pivoted_df, ["MOVIE", "SHOW"])

    summary_types = df.groupby("type").size().to_frame("count").reset_index()


    pieplot(summary_types)

    df["imdb_score"] = df["imdb_score"].fillna(0).astype(int)

    summary_scores = df.groupby("imdb_score").size().to_frame("count").reset_index()

    barplot(summary_scores)
    
    return

if __name__ == "__main__":
    main()