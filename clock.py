import datetime
import time
import requests
from urllib.parse import urlencode


def clock_in(data):
    print(data)
    url = "https://v-xxtb.zust.edu.cn/api/Ncov2019/update_record_student"
    t = datetime.datetime.now()
    t1 = t.strftime('%Y-%m-%d %H:%M:%S')
    ts1 = time.mktime(time.strptime(t1, '%Y-%m-%d %H:%M:%S'))
    ts2 = 1595606457
   # end_time = int(str(ts1 * 1000).split(".")[0])
   # start_time = int(str(ts2 * 1000).split(".")[0])
    days = int((datetime.datetime.fromtimestamp(ts1) - datetime.datetime.fromtimestamp(ts2)).days)
    print(days)
    headers = {
        'Referer': 'https://v-xxtb.zust.edu.cn/web/mobile37/',
        'Origin': 'https://v-xxtb.zust.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; 1503-M02 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036558 Safari/537.36 MicroMessenger/6.3.25.861 NetType/WIFI Language/zh_CN',
        'Accept': 'application/json',
        'Accept-Language': 'zh-cn',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    params = {
        "id": data['student_id'],
        "user_type": 1,
        "environment_type": 101,
        "morning_state": 1,
        "afternoon_state": 1,
        "is_body_ok": 1,
        "is_gl": 0,
        "is_tl": 0,
        "is_jc": 0,
        "is_2_man": 0,
        "is_family": 0,
        "user_location": 1,
        "location_province": data['province'],
        "location_city": data['city'],
        "location_country": data['country'],
        "student_id": data['student_id'],
        "r_id": 171 + days,
        'round': '',
        "module_id": 63,
    }
    payload = urlencode(params)
    print(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.content
