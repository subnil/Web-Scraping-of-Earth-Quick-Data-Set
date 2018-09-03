#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 17:14:22 2018

@author: sub
"""

import os
import pandas as pd


os.chdir('/home/sub/ITT_itr4/Anterior_granular/with_time/Featureimp')


pickles=os.listdir(os.getcwd())


for p in pickles:
    
   feature_dict=pd.read_pickle(p)
   
   #feature_df=pd.DataFrame.from_dict(feature_dict,)
   
   feature_df=pd.DataFrame([[key,value] for key,value in feature_dict.items()],columns=["Feature","Score"])
   
   feature_df.sort_values(by='Score',ascending=False)
   

   #feature_df.columns=['Feature','Score'] 

   #feature_df.sort_values()

   path= '/home/sub/Desktop/feature_importance_23_aug/anterior'
   
   total_path=os.path.join(path,p.split('.')[0]+'.csv')
   
   feature_df.to_csv(total_path,index=False)
