#imports

import requests
import pandas as pd
import re
import json
import math
from modules import module as md

#pendiente poner aquí las variables, si no no va a funcionar no?

def main():
    DF_PULLS = md.get_pulls(BASE_URL, KEY, OWNER, REPO, PULLS, SEARCH, STATE, USERNAME, API_TOKEN, field_list1)
    DF_STATUS = md.df_status(DF_PULLS, BASE_URL, KEY, OWNER, REPO, COMMITS, USERNAME, API_TOKEN, field_list2)
    DF_CSV = md.create_csv(DF_STATUS, field_sort1, field_name1)
  

if __name__ == '__main__':
    main()

    