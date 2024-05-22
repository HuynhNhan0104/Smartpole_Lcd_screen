import json

mess = '{"username":"GutD","owner":{"id":1060777,"username":"GutD"},"id":2782297,"name":"Live_Stream","description":"","license":null,"history":true,"enabled":true,"visibility":"public","unit_type":null,"unit_symbol":null,"last_value":"{\"ID\": [4, 5, 6], \"link\": \"https://www.twitch.tv/huynhnguyenhieunhan\"}","created_at":"2024-04-13T09:11:04Z","updated_at":"2024-05-21T14:57:18Z","wipper_pin_info":null,"key":"live-stream","writable":false,"group":{"id":1151962,"key":"default","name":"Default","user_id":1060777},"groups":[{"id":1151962,"key":"default","name":"Default","user_id":1060777}]}'
data = json.loads(mess)
print(json.dumps(data, indent=4))