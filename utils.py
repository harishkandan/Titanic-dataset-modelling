import time
import pickle

def display_col_type(data):
    '''See column type distribution
       Parameters
       ----------
       data: pandas dataframe
       Return
       ------
       dataframe
    '''
    column_type = data.dtypes.reset_index()
    column_type.columns = ["count", "column type"]
    return column_type.groupby(["column type"]).agg('count').reset_index()

def get_NC_col_names(data):
    '''Get column names of category and numeric
        Parameters
        ----------
        data: dataframe
        Return:
        ----------
        numerics_cols: numeric column names
        category_cols: category column names
    '''
    numerics_cols = data.select_dtypes(exclude=['O']).columns.tolist()
    category_cols = data.select_dtypes(include=['O']).columns.tolist()
    return numerics_cols, category_cols

def missing_columns(data):
    '''show missing information
        Parameters
        ----------
        data: pandas dataframe
        Return
        ------
        df: pandas dataframe
    '''
    df_missing = data.isnull().sum().sort_values(ascending=False)
    df = pd.concat([pd.Series(df_missing.index.tolist()), pd.Series(df_missing.values),
                    pd.Series(data[df_missing.index].dtypes.apply(lambda x: str(x)).values),
                    pd.Series((df_missing / data.shape[0]).values)], axis=1, ignore_index=True)
    df.columns = ['col_name', 'missing_count', 'col_type', 'missing_rate']

    return df

def pickle_dump(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f, protocol = pickle.HIGHEST_PROTOCOL)
def pickle_load(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
