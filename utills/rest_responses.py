import json
from datetime import datetime

class REST :
    status = int()
    message = str()
    detail = str()
    datetime = str()
    data = dict()

    def Rest_Response(self, message, detail, data, status_error):
        self.status = status_error
        self.data = data
        self.message = message
        self.detail = detail
        self.date = datetime.now().strftime('%m/%d/%Y - %H:%M:%S')
        
        return self.__dict__



    def __str__(self):
        return self.__dict__