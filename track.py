import requests

class Track:

    def __init__(self):
        self.url = "https://covid-19-tracking.p.rapidapi.com/v1"

        self.headers = {
             'x-rapidapi-key': "d30c9b20a1mshf7b0cf45d9eb8c4p1b1d51jsn7724536d9cb5",
             'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com"
             }
        

    def getResult(self):   
        response = requests.request("GET", self.url, headers=self.headers)

        try:
            return eval(response.text)
        except Exception as e:
            return None
            print(e)

    

if __name__ == '__main__':
    track = Track()
    res = track.getResult()
    print(res)
        