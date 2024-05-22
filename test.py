import json
import requests
# api_url = "https://ezdata2.m5stack.com/api/v2/4827E2E30938/dataMacByKey/raw"
api_url = "https://io.adafruit.com/api/v2/GutD/feeds/live-stream"
response = requests.get(api_url)
if response.status_code == 200:
    content= json.loads(response.content)
    print(json.dumps(content,indent=4))
    last_value = json.loads(content.get("last_value"))
    # print(type(last_value))
    # last_value = json.loads(last_value)
    link = last_value.get("link")
    print(last_value)
    
    