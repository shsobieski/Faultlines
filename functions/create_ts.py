def create_ts(df, var_list, split= 'total'):
    """
    Creates a DataFrame with percentage of total per year in each column.
    
    Parameters:
    df: a DataFrame with a year column and a categorical data column
    var_list: a list of the categorical variables user wishes to include in the total
    
    """
    dummied = pd.get_dummies(df, prefix= '', prefix_sep= '')
    grouped = dummied.groupby('year').sum().reset_index()
    grouped['total'] = 0
    for var in var_list:
        grouped['total'] += grouped[var]
    ts_df = pd.DataFrame()
    ts_df['year'] = grouped['year']
    for var in var_list:
        ts_df[var] = grouped[var]/grouped['total']
    return ts_df