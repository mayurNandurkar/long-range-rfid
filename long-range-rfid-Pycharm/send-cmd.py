import requests


while 1 :
    data = {"store": 00, "temp": 27.00}
    resp = requests.post('http://104.37.185.20/~tech599/tech599.com/johnaks/flowers_new/api/read_status.php', params=data)

    print(resp.content)

