import requests

class Get_Busy:
    def __init__(self):
        self.api_url = "https://besttime.app/api/v1/forecasts"
        
        #url = "https://besttime.app/api/v1/keys/pri_697d7e59ec3b4ec78ed4d4a79b19ffdd"
        #response = requests.request("GET", url)
        #print(response.json())
    def get(self):
        try:

            venue_list = {
                ("Lost Dog Café & Lounge", "Water St, Binghamton"),
                ("Goodwill NYNJ Store & Donation Center, Vestal Parkway East, Vestal"),
                ("Uncorked Creations", "State St, Binghamton")
            }

            for venue in venue_list:
                params = {
                'api_key_private': 'pri_697d7e59ec3b4ec78ed4d4a79b19ffdd',
                'venue_name': venue[0],
                'venue_address': venue[1]
                }
            response = requests.request("POST", self.api_url, params=params)
            results = response.json()
            return results
        
        except:
            None

busy_times = Get_Busy()
print(busy_times)