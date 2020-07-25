from flask import Flask, request, render_template
from flask_apscheduler import APScheduler
from flask_cors import CORS
import json
import datetime
from User import User
import clock
from SchedulerConfig import SchedulerConfig

app = Flask(__name__)
scheduler = APScheduler()
CORS(app, supports_credentials=True)
User = User()


@app.route('/clock', methods=["POST"])
def do_clock():
    return post_in(request)

@app.route('/logs', methods=["POST"])
def get_logs():
    return find_logs(request)

@app.route('/')
def index():
    return render_template('index.html')


def post_in(request):
    data = json.loads(request.get_data())
    if data['auto'] == 1:
        log = clock.clock_in(data)
        print(log)
        result = User.save(data)
    else:
        log = clock.clock_in(data)
    status = {
        'student_id': data['student_id'],
        'code': log['code'],
        'message': log['message']
    }
    User.saveLogs(status)
    if (log['code'] == 200):
        return response(data, code=20000, message='打卡成功！')
    else:
        return response(log, code=50000, message='打卡失败！')

def find_logs(request):
    data = User.findLogs()
    if(data):
        return response(data, code=20000, message='查找成功！')
    else:
        return response({}, code=50000, message='查找失败！')

def response(data, code, message):
    return json.dumps({
        'data': data,
        'code': code,
        'message': message
    }, indent=2, ensure_ascii=False, cls=DateEnconding)

#XU@6X6Pl
class DateEnconding(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            o = o + datetime.timedelta(hours=8)
            return o.strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    app.config.update(
        {"SCHEDULER_API_ENABLED": True,
         "JOBS": [{"id": "my_job",  # 任务ID
                   "func": "task:my_job",  # 任务位置
                   "trigger": "interval",  # 触发器
                   "seconds": 3600  # 时间间隔
                   }
                  ]}
    )
    scheduler.init_app(app=app)
    scheduler.start()
    app.run(host="0.0.0.0", port=5000)
