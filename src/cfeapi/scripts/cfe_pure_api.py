import json
import requests

BASE_URL =  "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"

def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()
    for obj in data:
        # print(obj['id'])
        if obj['id'] == 2:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            print(r2.json())
    return data

def create_update():
    new_data = {
        'user': 1,
        'content': 'Another new more new cool content'
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        print(r.json())
        return r.json()
    return r.text

# print(create_update())

# print(get_list())

def do_obj_update():
    new_data = {
        'content': 'awesome'
    }
    r = requests.put(BASE_URL + ENDPOINT + '10', data=json.dumps(new_data))
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        print(r.json())
        return r.json()
    return r.text


def do_obj_delete():
    new_data = {
      'content': 'New obj data'
    }
    r = requests.delete(BASE_URL + ENDPOINT + '10', data=json.dumps(new_data))
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        print(r.json())
        return r.json()
    return r.text

# print(do_obj_update())
print(do_obj_delete())