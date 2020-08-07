def store_predictions(df):
    """
    Returns a DataFrame with original time series and predictions in same DataFrame 
    
    """
    ts = df[df.columns[1]]
    base = pd.DataFrame(ts)
    preds = make_preds(ts, 'Predicted '+ df.columns[1])
    base.index = df['year']
    base = base.append(pd.DataFrame(preds), sort = True)
    for col in df.columns[2:]:
        ts = df[col]
        temp = pd.DataFrame(ts)
        preds = make_preds(ts, 'Predicted ' + col)
        temp.index = df['year']
        temp = temp.append(pd.DataFrame(preds), sort = True)
        base = base.join(temp)
    return base