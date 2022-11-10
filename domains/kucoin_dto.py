import sys  
sys.path.insert(0, '..') 

import datasource.redis_c as redis_c
import services.kcoin as kcoin
import coloredlogs, logging


#####################Global Variables ########################

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

#####################End of Global Variables #################

class KuCOIN:

    CURRENT = int()
    BACKUP_PART = int() # maximum buy plan, it could be in range [1, count_part]
    COUNT_PART = int() # maximum segment that we have

    total = float() # the whole price which we have, for example : 100$
    total_part = float()


    def __init__(self, count_part=None, backup_part=None):
        if count_part is None:
            self.COUNT_PART = 10
        else:
            self.COUNT_PART = count_part

        if backup_part is None:
            self.BACKUP_PART = 3
        else:
            self.BACKUP_PART = backup_part

        self.CURRENT = 0


    def generate(self):
        data = kcoin.get_accounts()

        for item in data:
            # TODO: should be dynamically fill this keys ....
            if item['type'] == 'trade' and item['currency'] == 'USDT':
                self.total = float(item['available'])
                can = True
                break

        self.CURRENT += 1 #
        self.total_part = self.total / self.COUNT_PART #

    
    def save(self):
        pass

    def is_end(self):
        if self.CURRENT == self.BACKUP_PART:
            logger.critical('you reach the backup-limit!')
            return True

        logger.info('you are in safe-zone of backup-limit!')
        return False
        




class KuCOINPart:

    REDIS_KEY = 'kucoin:'

    total_dollar =  float() # sum of buy-orders with usdt symbol. [1$, 2.8$]
    total_coin = float()# all we have right-now.

    segment_dollar = float() # bought this price for this transaction [1$, 1.8$, 3.5$]
    segment_coin = float() # bought this coin for this transaction
    price = float() 
    fee = float()
    order_id = str() 

    def __str__(self):
        return str(self.__dict__)


    def generate(self):
        r = redis_c.REDIS().r
        exists = r.get(self.REDIS_KEY)

        is_exist = r.keys('kucoin*')
        val = r.get(is_exist[0])
        print(is_exist, val)

        if exists is None:
            print("REDIS is Empty")
        else:
            print("REDIS is not Empty")


    def calculate_avg():
        pass

    def add():
        pass

    def update():
        pass

    def delete():
        pass

    def sell(self):
        pass
    def buy(self):
        pass
    def cancel_order(self):
        pass


class Schedule:
    REDIS_KEY = 'schedule'

    LEVELS = [10.0, 20.0, 40.0, 50.0, 60.0, 100.0] # default levels
    CRASH_PERCENT = [-1 , 5.0, 5.0, 5.0, 5.0, 5.0] # default crash percent per order 

    status = True
    index = 0


    def __init__(self, levels=None):
        if levels is not None:
            self.LEVELS = levels

        if self.LEVELS[-1] != 100.0:
            self.LEVELS.append(100.0)

    def __str__(self):
        return str(self.__dict__)

    def segment_data(self):
        return (self.LEVELS[self.index], self.CRASH_PERCENT[self.index])


    def is_end(self):
        if self.index == 5:
            self.index = 0
            self.status = False
            return True
        
        return False

    def get_money(self, total):
        return total * self.LEVELS[self.index] / 100.0


    



if __name__ == '__main__':
    k = KuCOIN()
    k.generate()
    print(k.__dict__)

    