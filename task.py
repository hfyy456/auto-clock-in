import datetime
import time

from User import User
import clock
from sender import mail

user = User()


def my_job():
    H = datetime.datetime.now().strftime('%H')
    print(H)
    if (H != '00'):
        return
    else:
        results = user.findAll()
        for item in results:
            if (item['student_id']):
                log = clock.clock_in(item)
                print(log)
                status = {
                    'student_id': item['student_id'],
                }
                user.saveLogs(status)
                time.sleep(1)
        return


if __name__ == '__main__':
    my_job()
