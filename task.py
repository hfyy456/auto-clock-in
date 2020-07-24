import datetime
import time

from User import User
import clock

user = User()


def my_job():
    H = datetime.datetime.now().strftime('%H')
    print(H)
    if (H != '08'):
        return
    else:
        results = user.findAll()
        for item in results:
            if (item['student_id']):
                log = clock.clock_in(item)
                print(log)
                time.sleep(1)
        return


if __name__ == '__main__':
    my_job()
