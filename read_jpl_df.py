"""Custom script to read in a jpl horizons file as a pandas dataframe"""

import numpy as np
import pandas as pd

def get_headers(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            if 'Date__(UT)__HR:MN' in line:
                split_headers = line.strip().split(',')
                header_list = [item for item in split_headers if item]
                fixed_header_list = [item.replace(" ", "") for item in header_list]    #remove white space in headers
  #              print(header_list)
    return fixed_header_list

def get_data(filepath): 
    data_rows = []  
    with open(filepath, "r") as file:
        in_data_section = False
        for line in file:
            line = line.strip()
            if line == "$$SOE":            #start tracking data at this marker
                in_data_section = True
                continue
            elif line == "$$EOE":          #stop tracking data at this marker
                break
            if in_data_section:
                split_line = line.split(',')                          #split up entries in each row
                datalist = [item for item in split_line if item]      #create list with the data for each row
   #             print(datalist)
                fixed_list = [item.lstrip() for item in datalist]     #remove leading white space in each entry
   #             print(fixed_list)     
                data_rows.append(fixed_list)
    return(data_rows)

def read_horizons_file(filepath):
    colheaders = get_headers(filepath)
    data = get_data(filepath)
    df = pd.DataFrame(data, columns=colheaders)
    return df