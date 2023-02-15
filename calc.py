

class Status:
    def __init__(self, status):
        self.status = status.lower()

    def set_status(self,status):
        self.status = status.lower()
    
    def get_status(self, status):
        return self.status

def calc():
    status = Status("waiting")
    while(status.status == "waiting"):

        #parse

        #calculate

        



