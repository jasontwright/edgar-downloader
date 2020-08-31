import requests
import os
import time
from datetime import datetime


def get_edgar_index_files(date_input, download_folder=None):
    
    date = datetime.strptime(str(date_input), '%Y%m%d')
    
    # Confirm that date format is correct
    error = 'Date format should be in YYYYMMDD. '
    if date > datetime.now():
        raise Exception(error+'The date utlized occurs in the future.')
    if date.year < 1993 or date.year > datetime.now().year:
       raise Exception(error+'The year is out of range. EDGAR did not begin accepting electronic filings until 1993.')
    
    index_type = ['company', 'form', 'master', 'xbrl']

    if 1 <= date.month <= 3:
        qtr ="Q1"
    elif 4 <= date.month <= 6:
        qtr ="Q2"
    elif 7 <= date.month <= 9:
        qtr ="Q3"
    elif 10 <= date.month <= 12:
        qtr ="Q4"
    
    if download_folder is None:
        base_path = os.path.dirname(os.path.realpath(__file__))
        current_dirs = os.listdir(path=base_path)
        if 'indexes' not in current_dirs:
            os.mkdir('/'.join([base_path,'indexes']))
            base_path = os.path.dirname(os.path.realpath(__file__))+'/indexes'
        else:
            base_path = os.path.dirname(os.path.realpath(__file__))+'/indexes'
    else:
        base_path = download_folder
        current_dirs = os.listdir(path=base_path)
        if 'indexes' not in current_dirs:
            os.mkdir('/'.join([base_path,'indexes']))
            base_path = base_path+'/indexes'
        else:
            base_path = download_folder+'/indexes'
        
    current_dirs = os.listdir(path=base_path)
    
    if str(date.year) not in current_dirs:
            os.mkdir('/'.join([base_path, str(date.year)]))

    for it in index_type:

        # Use the following filename pattern to store the index files locally
        local_filename = f'{date.year}-{qtr}-{it}-index.txt'
        
        # Create the absolute path for storing the index files
        local_file_path = '/'.join([base_path, str(date.year), local_filename])

        # Define the url at which to get the index file.
        url = f'https://www.sec.gov/Archives/edgar/full-index/{date.year}/{qtr}/{it}.idx'

        # Get the index file from EDGAR and save it to a text file. Note that to save a file
        # rather than bringing it into memory, set stream=True and use r.iter_content() 
        # to break the incoming stream into chunks (here arbitrarily of size 10240 bytes)
        r = requests.get(url, stream=True)
        with open(local_file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=10240):
                f.write(chunk)
                
        # Wait one-tenth of a second before sending another request to EDGAR.
        time.sleep(0.1)

get_edgar_index_files(20200630)