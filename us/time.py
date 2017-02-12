from datetime import datetime
import json

def json_timezone(tzn):
    with open('systm/options.json', 'r+') as jfile:
        data = json.load(jfile)
        data['timezone'] = tzn
        jfile.seek(0)
        json.dump(data, jfile, indent=1)
        jfile.truncate()
    jfile.close()

def main(cmd):
    if cmd == 'date':
        print datetime.now().strftime("%Y-%m-%d")
    elif cmd == 'year':
        print datetime.now().strftime("%Y")
    elif cmd == 'month':
        print datetime.now().strftime("%m")
    elif cmd == 'time':
        print datetime.now().strftime("%H:%M:%S")
    elif cmd == 'minutes' or 'minute':
        print datetime.now().strftime("%M")
    elif cmd == 'seconds' or 'second':
        print datetime.now().strftime("%S")
    elif cmd == 'day':
        print datetime.now().strftime("%d")
    elif cmd == 'date time':
        print datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elif cmd[:13] == 'json-timezone':
        json_timezone_auto(cmd[14:])
    else:
        print datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def return_time(*typ):
    if cmd == 'date':
        return datetime.now().strftime("%Y-%m-%d")
    elif cmd == 'year':
        return datetime.now().strftime("%Y")
    elif cmd == 'month':
        return datetime.now().strftime("%m")
    elif cmd == 'time':
        return datetime.now().strftime("%H:%M:%S")
    elif cmd == 'minutes' or 'minute':
        return datetime.now().strftime("%M")
    elif cmd == 'seconds' or 'second':
        return datetime.now().strftime("%S")
    elif cmd == 'day':
        return datetime.now().strftime("%d")
    elif cmd == 'date time':
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
