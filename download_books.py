#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:42:21 2020

@author: krish
"""

import requests, wget, webbrowser
import pandas as pd
df = pd.read_excel("FreeEnglishtextbooksAll.xlsx")

for index, row in df.iterrows():
        # loop through the excel list
        category = row.loc["English Package Name"]
        file_name = f"{row.loc['Book Title']}_{row.loc['Edition']}".replace('/','-').replace(':','-').replace('.','-')
        url = f"{row.loc['OpenURL']}"
        r = requests.get(url) 
        download_url = f"{r.url.replace('book','content/pdf')}.pdf"
        wget.download(download_url, f"./Downloads/{file_name}.pdf")
        #wget.download(download_url, out=file_name)
        webbrowser.open(download_url, new=2)
        print(f"downloading {file_name}.pdf Complete ....")
        #shutil.move(f"Downloads/{file_name}.pdf", f"Downloads/{category}/{file_name}.pdf")

