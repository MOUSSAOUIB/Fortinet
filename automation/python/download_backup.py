
import requests

url = 'http://192.168.1.82/api/v2/monitor/system/config/backup?destination=file&scope=global'
payload={}
headers = {
        'Authorization': 'Bearer NGgk9x7fcGQrdpb3d7gdt517jn5sb3',
        'Cookie': 'FILE_DOWNLOADING_10658098752910038235="1"'
}

answer = requests.request("GET", url, headers=headers, data=payload)

print(answer.text)

with open("backup.conf", 'wb') as file:
        file.write(response.content)
Footer
