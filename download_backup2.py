import requests

api_url='http://192.168.1.82/api/v2/monitor/system/config/backup?destination=file&scope=global&access_token=NGgk9x7fcGQrdpb3d7gdt517jn5sb3'


requests.packages.urllib3.disable_warnings()

data = requests.get(api_url, verify=False)

with open('/home/moussaoui/backup_1.conf' ,'wb') as f:

         for line in data:

               f.write(line)
