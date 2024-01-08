import requests
url = "https://jsonplaceholder.typicode.com/users"

res = requests.get(url)
if res.status_code != 200:
    print(f"The error code is {res.status_code}")
page_content = res.text
data = res.json()
for user in data:
    for k,v in user.items():
        if k == 'address' or  k == 'company' :
            print(f"{k} :")
            for k1, v1 in v.items():
                print(f"{k1} -->  {v1}")
        else:
            print(f"{k} -->  {v}")
    print("***************************************************")



