"""
"       This is a template for writing python scripts for the Incapsula API
"       USAGE:
"       Download this file and modify it for your needs of the API.
"       The script currently contains all variables that can be used as input parameters 
"       Also contains a method apiRequest that builds your API request.
"       Use that method to build other methods for more specific API calls
"       I'm not good at Python so if you want to tell me it sucks, email me at andrew.still@imperva.com
"       Or say it to my face, Imperva RWS Office desk #95 
"
"       The Incapsula API Reference can be found at: https://docs.incapsula.com/Content/API/api.htm
"""

import json, sys, getopt, csv
import httplib, urllib
import base64

"""
"       Declaring input parameters, optional params are commented out. Remove comment for usage.  
"""

#Required Variables
api_key = ''
api_id = ''

#Account and Site ID
account_id = ''
site_id = ''

#Pagination 
#page_size = 50  #The number of objects to return in the response. 50 by default
#page_num = 0    #The page to return starting from 0. 0 by default

#Time range specification
#time_range = 'today' #[today(DEFAULT), last_7_days, last_30_days, last_90_days, month_to_date]

#Account management
#parent_id = ''     #The newly created account's parent ID. Invoking account used as default.
#user_name = ''     #The account owner's name. Ex. 'John Doe'
#plan_id = ''       #An identifier of the plan to assign to the new account. 
#ref_id = ''        #Customer specific identifier for the operation.
#account_name = ''  #Account Name
#log_level = ''     #Sets the log reporting level for the site. [full, security, none, default]
#log_account_id = ''#Numeric identifier of the account that purchased the logs integration. Authenticated account used by default.
#param = ''         #


"""
"       Builds an API request using the required and optional params
"       Returns the response as a dictionary (Dictionary is a key:value table like a JSON file)
"       @url - URL for the specfic API request
"       @option_params - Dictionary of required params from the API
"""

def apiRequest(url, optional_params = {}):
        result = []
        basic_params = {'api_key' : api_key, 'api_id' : api_id}
        try: 
            connection = httplib.HTTPSConnection('my.incapsula.com', '443')
            params = basic_params.items() + optional_params.items()
            conn_params = urllib.urlencode(params)
            conn_headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
            connection.request("POST", url, conn_params, conn_headers)
            response = connection.getresponse()
            result = json.loads(response.read())
        except ValueError, Error:
            result['res'] = -1
            result ['res_message'] = "Communication Error, Please Contact Incapsula Support"
        return result



"""
"   Main method:
"   Call your methods here 
"""

def main():
    
    global api_key, api_id, site_id
    usage_msg = "Usage: api.py -k <api-key> -i <api-id>"
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hwk:i:",["key=","id="])
    except getopt.GetoptError:
        print (usage_msg)
        sys.exit(2)

        #Input Validation
    for opt, arg in opts:
        if opt == '-h':
            print (usage_msg)
            sys.exit()
        elif opt in ('-k', '--key'):
            api_key = arg
        elif opt in ('-i', '--id'):
            api_id = arg
        else:
            print (usage_msg)
            sys.exit(2)

    if (api_id == "" or api_key == ""):
            print (usage_msg)
            sys.exit(2)
    

"""""""""""""""""""""""""""
" I N I T I A L I Z I N G "
"""""""""""""""""""""""""""
if __name__ == "__main__":
    main()
