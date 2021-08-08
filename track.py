import requests

class Track:

    def __init__(self):
        self.url = "https://covid-19-tracking.p.rapidapi.com/v1"

        self.headers = {
            'x-rapidapi-key': "ed7e61a0bcmsh8bac8fae8c7b448p16672ajsn2beb82b3a8d6",
            'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com"
            }
        

    def getResult(self):   
        response = requests.request("GET", self.url, headers=self.headers)

        try:
            return eval(response.text)
        except Exception as e:
            return None
            print(e)