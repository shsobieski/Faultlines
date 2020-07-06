def unzip(file):
    my_tar = tarfile.open('data/zipped_data/'+ file +'.tar.gz')
    my_tar.extractall('./data/unzipped_data/' + file)
    my_tar.close()
    return pd.read_csv('data/unzipped_data/' 
                       + file + '/' + file.lower() + '.csv')