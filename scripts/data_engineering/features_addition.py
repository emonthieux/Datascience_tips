import pandas as pd

def get_changes(serie: pd.Series) -> pd.Series:
    """
    Categorize evolution of values in a serie.
    If the value is different from the previous one, the value is incremented by 1.

    serie : pd.Series 
        Serie to process

    returns : pd.Series
    """

    # Compare if each value is different from the previous one and do the cumulative sum of it
    serie_evolution = (serie != serie.shift()).cumsum()

    return serie_evolution