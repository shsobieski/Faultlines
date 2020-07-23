def save(question, split='overall', visualize= True):
    if split == 'overall':
        rep_preds = store_predictions(rep_ts)
        rep_preds.to_excel('data/predictions/{}/overall/republican.xlsx'.format(question))
        dem_preds = store_predictions(dem_ts)
        dem_preds.to_excel('data/predictions/{}/overall/democrat.xlsx'.format(question))
        ind_preds = store_predictions(ind_ts)
        ind_preds.to_excel('data/predictions/{}/overall/independent.xlsx'.format(question))
        
        if visualize:
            fig = plt.figure(figsize=(16,4))
            ax1, ax2, ax3 = fig.subplots(nrows=1, ncols=3, sharey=True)
            rep_preds.plot(title= 'republican', ax= ax1)
            dem_preds.plot(title= 'democrat', ax=ax2)
            ind_preds.plot(title='independent', ax=ax3);
                    
    if split == 'within':
        str_rep_preds = store_predictions(str_rep)
        str_rep_preds.to_excel('data/predictions/{}/leveled/strongrepublican.xlsx'.format(question))
        mid_rep_preds = store_predictions(mid_rep)
        mid_rep_preds.to_excel('data/predictions/{}/leveled/republican.xlsx'.format(question))
        ln_rep_preds = store_predictions(ln_rep)
        ln_rep_preds.to_excel('data/predictions/{}/leveled/leanrepublican.xlsx'.format(question))
        str_dem_preds = store_predictions(str_dem)
        str_dem_preds.to_excel('data/predictions/{}/leveled/strongdemocrat.xlsx'.format(question))
        mid_dem_preds = store_predictions(mid_dem)
        mid_dem_preds.to_excel('data/predictions/{}/leveled/democrat.xlsx'.format(question))
        ln_dem_preds = store_predictions(ln_dem)
        ln_dem_preds.to_excel('data/predictions/{}/leveled/leandemocrat.xlsx'.format(question))
        ind_preds = store_predictions(ind)
        ind_preds.to_excel('data/predictions/{}/leveled/independent.xlsx'.format(question))
        oth_preds = store_predictions(oth)
        oth_preds.to_excel('data/predictions/{}/leveled/other.xlsx'.format(question)) 
        
        if visualize:
            fig = plt.figure(figsize=(16,8))
            ((ax1, ax2, ax3, ax4),
             (ax5, ax6, ax7, ax8))= fig.subplots(nrows=2, ncols=4, sharey=True)
            str_rep_preds.plot(title='strong republican', ax= ax1)
            mid_rep_preds.plot(title='republican', ax=ax2)
            ln_rep_preds.plot(title='lean republican', ax=ax3)
            ind_preds.plot(title='independent', ax=ax4)
            str_dem_preds.plot(title='strong democrat', ax=ax5)
            mid_dem_preds.plot(title='democrat', ax=ax6)
            ln_dem_preds.plot(title='lean democrat', ax=ax7)
            oth_preds.plot(title='other', ax=ax8)