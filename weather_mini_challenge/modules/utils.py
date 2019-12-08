import pandas as pd
from pandas import DataFrame
from dateutil.parser import parse


class Utils(object):

    @staticmethod
    def cast_columns(df, columns: dict):
        """
        Function responsible to casting columns to correct data type.
        - Cast using dict with specif column/data type
        :param columns: columns to be casting
        """
        if columns:
            for k, v in columns.items():
                if 'date' == v:
                    for i, row in df.iterrows():
                        try:
                            df[k][i] = parse(row[k], ignoretz=True, dayfirst=True).date()
                        except TypeError:
                            df[k][i] = pd.NaT
                    return df
                if 'string' == v:
                    df[k] = df[k].astype(str)
                    return df
