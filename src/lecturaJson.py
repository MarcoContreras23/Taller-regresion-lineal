import json


class lecturaJson:
    
    
    def __init__(self, path):
        self.path = path

    def leer(self):
        with open(self.path) as file:
            data = json.load(file)

            return (data["x"]["nombre"], 
                data["y"]["nombre"], 
                data["x"]["dato"], 
                data["y"]["dato"], 
                data["datoAPredecir"])