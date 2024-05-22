import json
import requests
api_url = "https://ezdata2.m5stack.com/api/v2/4827E2E30938/dataMacByKey/raw"
response = requests.get(api_url)
if response.status_code == 200:
    content= json.loads(response.content)
    # print(json.dumps(content, indent=4))
    data = content.get("data")
    value_str = data.get("value").replace("\\", "")
    value = json.loads(value_str)
    print(value)
    co2    = 0 if value["scd40"]["co2"]     is None else value["scd40"]["co2"]
    nox    = 0 if value["sen55"]["nox"]     is None else value["sen55"]["nox"]
    pm1    = 0 if value["sen55"]["pm1.0"]   is None else value["sen55"]["pm1.0"]
    pm25   = 0 if value["sen55"]["pm2.5"]   is None else value["sen55"]["pm2.5"]
    pm10   = 0 if value["sen55"]["pm10.0"]  is None else value["sen55"]["pm10.0"]
    voc    = 0 if value["sen55"]["voc"]     is None else value["sen55"]["voc"]
    print(f"co2: {co2}")
    print(f"Nox: {nox}")
    print(f"pm1: {pm1}")
    print(f"pm2.5: {pm25}")
    print(f"pm10: {pm10}")
    print(f"voc: {voc}")
    