def make_preds(ts, name):
    """
    Chooses parameters for and returns predictions from an 
    ARIMA model based time series
    
    """
    ts.index = pd.to_datetime(overall['year'], format='%Y')
    ts.index = ts.index.to_period('Y')
    ts.dropna(inplace = True)
    try:
        model = ARIMA(ts, (1,1,1))
        arma = model.fit(disp=0)
        best_aic = arma.aic
        best_combo = (1,1,1)
    except:
        best_aic = 1000000000
        best_combo = (0,0,0)
    for combo in [(1,1,1),(1,1,2),(2,1,1),(2,1,2),(3,1,1),
                  (3,1,2),(1,1,3),(2,1,3),(3,1,3),(1,1,4),
                  (2,1,4),(3,1,4),(4,1,4),(4,1,3),(4,1,2),
                  (4,1,1),(1,1,5),(2,1,5),(3,1,5),(4,1,5),
                  (5,1,5),(5,1,4),(5,1,3),(5,1,2),(5,1,1)]:
        try:
            model = ARIMA(ts, order=combo)
            arma = model.fit(disp=0)
            score = arma.aic
            if score < best_aic:
                best_aic = score
                best_combo = combo
            else: 
                continue
        except:
            continue
    model = ARIMA(ts, order=(best_combo))
    arma = model.fit(disp=0)
    preds = pd.Series(arma.forecast(6)[0])
    years = np.array(range(2019, 2025))
    preds.index = years
    preds = pd.DataFrame(preds, columns = [name])
    return preds