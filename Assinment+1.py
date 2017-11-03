
# coding: utf-8

# In[1]:

import json
import urllib2

earthquake_file = open('earthquake_details.json','w')

def earthquake_api(startdate,enddate):

        try:
            str_response= urllib2.urlopen('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime='+startdate+'&endtime='+enddate)
            json_response = json.loads(str_response.read())
            earthquake_file.write(json.dumps(json_response,indent=3))
            earthquake_file.write("\n")
        except urllib2.URLError:
            print ('No response received for start date '+startdate+'end date'+enddate)

def main():
    startdate='2016-10-01'
    enddate='2016-10-02'

    earthquake_api(startdate,enddate)
    earthquake_file.close()


if __name__ == '__main__':     # if the function is the main function ...
    main() # ...call it


# In[4]:

import json
from pprint import pprint
import pandas as pd
import os

   
def main():
    i=0
    
    with open('earthquake_details.json') as person_file:
        dict_data = json.load(person_file)
        i=len(dict_data['features'])
        print(len(dict_data['features']))
        print (type(dict_data['features']))

    #accessing the feature elements
        feature_data= dict_data['features']
    
    Latitude=[]
    Longitude=[]
    title=[]
    place=[]
    mag=[]

    for d in range(i):
        Latitude.append(dict_data['features'][d]['geometry']['coordinates'][0])
        #get longitude

        Longitude.append(dict_data['features'][d]['geometry']['coordinates'][1])
        #to get place
        title.append(dict_data['features'][d]['properties']['place'])
        place.append (dict_data['features'][d]['properties']['title'])
        mag.append(dict_data['features'][d]['properties']['mag'])
    
    csv=pd.DataFrame({'Latitude':Latitude,'Longitude':Longitude,'Title':title,'Place':place,'Magnitude':mag})
    os.chdir('E:/')
    csv.to_csv('new.csv',index=False)   
    
    mg_gr_two = csv.loc[csv['Magnitude'] > 2]
    print (mg_gr_two.count())
    plc_gr_cali = csv[csv['Place'].str.contains("California")]
    print (plc_gr_cali.count())
    mg_gr_fiv = csv.loc[csv['Magnitude'] > 5]
    print (mg_gr_fiv.count())

if __name__ == '__main__':     # if the function is the main function ...
    main() # ...call it

