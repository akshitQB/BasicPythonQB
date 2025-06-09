import requests

cookies = {
    "ac_cclang": "",
    "panoramaIdType": "panoDevice",
    "_ga": "GA1.1.693024763.1748840229",
    "panoramaId_expiry": "1749445038507",
    "__eoi": "ID=3dc50132effefdc4:T=1748840229:RT=1749122412:S=AA-AfjapTqDqxYuzkSaN4GO7ZJgU",
    # ... add more cookies as needed
}

response = requests.get("https://www.w3schools.com/", cookies=cookies)

print(response.status_code)
print(response.text)
