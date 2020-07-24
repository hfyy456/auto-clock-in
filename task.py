import datetime
from User import User
import clock
user=User()

def my_job():
    H =datetime.datetime.now().strftime('%H')
    if( H !='8'):
        return
    else:
        results = user.findAll()
        for item in results:
            if(item['student_id']):
                log=clock.clock_in(item)
                print(log)
        return

