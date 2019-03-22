import requests
import json

response = requests.get("https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json")
res_body = json.loads(response.content)

bulgaria = res_body[32]
bulg_legis = bulgaria['legislatures'][0]['popolo_url']
list_of_bulg_people = requests.get(bulg_legis)
list_of_bulg_people_body = json.loads(list_of_bulg_people.content)
bulg_person = list_of_bulg_people_body['persons'][5]['name']
