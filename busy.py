import requests

class Get_Busy:
    def __init__(self, params):
        self.api_url = "https://besttime.app/api/v1/forecasts/day"
        self.params = params
        self.response = requests.request("POST", self.api_url, params=self.params)
        self.results = self.response.json()
        self.analysis = self.results['analysis']
        #self.getInformation()
        
        
    def getBusyHrs(self):
        try:
            # self.response = requests.get(self.api_url).json()
            # self.busy_hours = self.response['busy_hours']
            
            self.busy_hrs = self.analysis['busy_hours']
            return self.busy_hrs
            
        except ConnectionError:
            exit()
        except KeyError:
            pass

    def getOpenHrs(self):
        try:
            self.open_info = self.analysis['day_info']
            self.open = self.open_info['venue_open']
            return self.open
        
        except ConnectionError:
            exit()
        except KeyError:
            pass
        
    def getClosedHrs(self):
        try:
            self.close_info = self.analysis['day_info']
            self.close = self.close_info['venue_closed']
            return self.close
        except ConnectionError:
            print("ConnectionError")
            exit()
        except KeyError:
            print("KeyError")
            pass
            

