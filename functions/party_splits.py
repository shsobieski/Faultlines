def party_splits(df, var_list, splits = 'by party'):
    split_ready = df.join(party['party'])
    rep_df = split_ready[(split_ready['party']=='Republican')|
                         (split_ready['party']=='Lean Republican')|
                         (split_ready['party']=='Strong Republican')]
    dem_df = split_ready[(split_ready['party']=='Democrat')|
                         (split_ready['party']=='Lean Democrat')|
                         (split_ready['party']=='Strong Democrat')]
    ind_df = split_ready[(split_ready['party']=='Independent')|
                         (split_ready['party']=='Other')]
    if split = 'by party:
        rep_ts = create_ts(rep_df)
        dem_ts = create_ts(dem_df)
        ind_ts = create_ts(ind_ts)
        return rep_ts, dem_ts, ind_ts
    if split = 'within party':
        str_rep_ts = create_ts(rep_df[rep_df['party']== 'Strong Republican'])
        mid_rep_ts = create_ts(rep_df[rep_df['party']== 'Republican'])
        ln_rep_ts = create_ts(rep_df[rep_df['party']== 'Lean Republican'])
        
        str_dem_ts = create_ts(dem_df[dem_df['party']== 'Strong Democrat'])
        mid_dem_ts = create_ts(dem_df[dem_df['party']== 'Democrat'])
        ln_dem_ts = create_ts(dem_df[dem_df['party']== 'Lean Democrat'])
        
        oth_ts = create_ts(ind_df[ind_df['paryt']== 'Other'])
        ind_ts = create_ts(ind_df[ind_df['party']== 'Independent'])
        
        return (str_rep_ts, mid_rep_ts, ln_rep_ts, str_dem_ts, mid_dem_ts,
                ln_dem_ts, oth_ts, ind_ts)
        
        