
class SchedulerConfig(object):
    JOBS = [
        {
            'id': 'print_job', # 任务id
            'func': 'print_job', # 任务执行程序
            'args': None, # 执行程序参数
            'trigger': 'interval', # 任务执行类型，定时器
            'seconds': 5, # 任务执行时间，单位秒
        }
    ]
#定义任务执行程序
def print_job():
    print("I'm a scheduler!")