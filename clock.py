import requests
from urllib.parse import urlencode
def clock_in(data):
    print(data)
    url = "https://v-xxtb.zust.edu.cn/api/Ncov2019/update_record_student"

    headers = {
        'Referer': 'https://v-xxtb.zust.edu.cn/web/mobile37/',
        'Origin': 'https://v-xxtb.zust.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36',
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
        "r_id": 170,
        'round': '',
        "module_id": 63,
    }
    payload = urlencode(params)
    print(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

