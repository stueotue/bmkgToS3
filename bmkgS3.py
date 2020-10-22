import requests
import xmltodict
import json
import time
import sys

bmkgUrl = 'https://data.bmkg.go.id/autogempa.xml'
apiGateway = sys.argv[1]
tempJam = ''

def dataGempa(url): 
    req = requests.get(url)
    jsonData = json.loads(json.dumps(xmltodict.parse(req.text)))
    return jsonData

def kirimKeGateway(url, data):
    req = requests.post(url, json=data)
    if req.status_code == 200:
        return "Data telah di simpan"
    else:
        return "Ada gangguan saat mengirim permintaan ke ApiGateway"

while True:
    testData = dataGempa(bmkgUrl)
    jam = testData['Infogempa']['gempa']['Jam']

    if(jam == tempJam):
        print("Belum ada pembaharuan data dari BMKG")
    else:
        print(kirimKeGateway(apiGateway, testData))
        tempJam = jam

    time.sleep(60)


