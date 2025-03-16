import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

def resume_table(df: pd.DataFrame, index: bool = False) -> pd.DataFrame:
    """
    Give an overview of a dataframe
    For each column, it gives the type of the values, the number of NA values, the number of unique values and the 3 first values

    df : pd.DataFrame 
        Dataframe to process
    
    index : bool, default False
        True: indlude the index in the overview
        False: doesn't include the index in the overview

    returns: pd.DataFrame
    """

    # Get list of columns names in the dataframe
    list_columns = df.columns

    # Declare the columns for the returned dataframe
    cols = ["type","nb_nan","nb_unique","v1","v2","v3"]

    # Declare an empty list that will recieve data for the returned dataframe
    list_data = []
    
    # Iterate over the dataframe columns names
    for i in list_columns :
        # Get current dataframe column
        x = df[i]

        # Append to the list of data: value type, number of NA values, number of unique values and the 3 first values
        list_data.append([x.dtypes,x.isna().sum(),x.nunique(),x.iloc[0], x.iloc[1], x.iloc[2]])

    # Check if we add the index to the overview
    if index:

        # Get index
        x = df.index

        # Insert to the first position of the list of data: value type, number of NA values, number of unique values and the 3 first values
        list_data.insert(0,[x.dtype,x.isna().sum(),x.nunique(),x[0], x[1], x[2]])

        # Insery index name in first position of the column names list
        list_columns = list_columns.insert(0,x.name)
    
    # Convert the list to a dataframe and return it
    df_return = pd.DataFrame(list_data, columns=cols, index=list_columns)

    return(df_return)


def distribution_matrix(df: pd.DataFrame, cols: list, dimensions: tuple, figsize: tuple = (15, 15), suptitle: str = "") -> None:
    """
    Plot histograms of a list of variables in a dataframe

    df : pd.DataFrame
        Dataframe to process

    cols : list
        List of columns to plot

    dimensions : tuple
        Tuple with the dimensions of the plot (n_rows, n_cols)

    figsize : tuple, default (15, 15)
        Size of the plot

    returns: None
    """

    n_rows, n_cols = dimensions


    # Create a figure
    fig, axs = plt.subplots(n_rows, n_cols, figsize=figsize)
    # Iterate over the columns
    for i, col in enumerate(cols):
        # Get the current axe
        ax = axs[i//n_cols, i%n_cols]

        # Plot the histogram
        sns.histplot(data=df, x=col, ax=ax)

        # Set the title of the plot
        ax.set_title(col + " distribution")

        # Rotate the x axis labels
        ax.tick_params(axis='x', rotation=45)

    # Hide empty subplots
    for i in range(len(cols), n_rows * n_cols):
        axs[i//n_cols, i%n_cols].axis("off")

    # Add a suptitle with better spacing
    plt.suptitle(suptitle, fontsize=16, y=1.02)  # Adjust y value to move title up
    plt.tight_layout(rect=[0, 0, 1, 0.99])  # Prevent suptitle overlap
    plt.show()


def distribution_matrix_vs_target(df: pd.DataFrame, cols: list, target: str, dimensions: tuple, figsize: tuple = (15, 15), suptitle: str = "") -> None:
    """
    Plot the distribution of the dataset variables against the target variable.

    df : pd.DataFrame
        Dataframe to process

    cols : list
        List of columns to plot

    target : str
        Target variable

    dimensions : tuple
        Tuple with the dimensions of the plot (n_rows, n_cols)

    figsize : tuple, default (15, 15)
        Size of the plot

    returns: None
    """

    n_rows, n_cols = dimensions

    # Create a figure
    fig, axs = plt.subplots(n_rows, n_cols, figsize=figsize)
    # Iterate over the columns
    for i, col in enumerate(cols):
        # Get the current axe
        ax = axs[i//n_cols, i%n_cols]

        # Check if the column is categorical
        if df[col].dtype == "object":
            # Plot the countplot
            sns.countplot(data=df, x=col, hue=target, ax=ax, palette="viridis")
        else:
            # Plot the histogram
            sns.violinplot(data=df, x=target, y=col, ax=ax)


        # Set the title of the plot
        ax.set_title(col + " distribution vs " + target)

        # Rotate the x axis labels
        ax.tick_params(axis='x', rotation=45)

    # Hide empty subplots
    for i in range(len(cols), n_rows * n_cols):
        axs[i//n_cols, i%n_cols].axis("off")

    # Add a suptitle with better spacing
    plt.suptitle(suptitle, fontsize=16, y=1.02)  # Adjust y value to move title up
    plt.tight_layout(rect=[0, 0, 1, 0.99])  # Prevent suptitle overlap
    plt.show()