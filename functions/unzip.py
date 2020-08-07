def unzip(file):
    """
    Unzips a tarfile and returns a DataFrame from the file
    
    """
    my_tar = tarfile.open('data/zipped_data/'+ file +'.tar.gz')
    my_tar.extractall('./data/unzipped_data/' + file)
    my_tar.close()
    df = pd.read_csv('data/unzipped_data/' 
                       + file + '/' + file.lower() + '.csv')
    df.rename(columns = {'Gss year for this respondent                       ' : 'year', 'Respondent id number': 'id'}, inplace = True)
    df['id'] = range(0, len(df['id']))
    return df