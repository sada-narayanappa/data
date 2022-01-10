#!/usr/local/bin/python 

#GENERATED BY /aiservices/notebooks/stocks/01_GetData.ipynb

import os, datetime, glob, sys, time, datetime, colabexts, shutil, argparse, csv, requests
import numpy as np

#import matplotlib as mpl
#mpl.use('Agg')

API_KEY = None  # Put your API KEY if you need to test data download or just use the data
#-----------------------------------------------------------------------------------
'''
This will read API_KEY from '~/.keys/keys.json'
'''
def getkey(key='password'):
    API_KEY, lines, file =None, None, os.path.expanduser('~/.keys/keys.json')
    if os.path.exists(file):
        with open(file, 'r') as f:
            r = f.read()
        j = eval(r)
        return j['AV_API_KEY'], j['NEWSAPI_KEY']
    else:
        raise Exception ("Please supply API_KEY")

    return avk, newsk;

#-----------------------------------------------------------------------------------
'''
This will check if the file is older than some time
'''
def chk_recent(filename, elapsed=8*60*60 ):
    if (os.path.exists(filename)):
        dt   = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
        dn   = datetime.datetime.now()
        ts   = (dn - dt)
        secs = (ts.days * 24 * 60 * 60 + ts.seconds)
        if (secs < elapsed): 
            print(f"{filename:22} exists, ... crested less than {secs} seconds!! at {dt} ")
            return True;
        
    return False

#-----------------------------------------------------------------------------------
'''
This will check if first file is newer than second file
'''
def chk_newer(filename1, filename2 ):
    if not (os.path.exists(filename1)) :
        return False
    if not os.path.exists(filename2) :
        return True
    
    dt1   = datetime.datetime.fromtimestamp(os.path.getmtime(filename1))
    dt2   = datetime.datetime.fromtimestamp(os.path.getmtime(filename2))
        
    return dt1 >= dt2
#-----------------------------------------------------------------------------------
def readfile(file, ret=None):
    if not os.path.exists(file):
        return ret
    
    with (open(file, "r")) as f: 
        conts = f.read()
    return conts

# Example:
#f1='/opt/data/data/stocks/data/aapl/news_raw.json'
#f2='/opt/data/data/stocks/data/aapl/news.html'
#chk_newer(f1, f2)
