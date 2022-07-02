import requests
import json

# your_json = '["foo", {"bar":["baz", null, 1.0, 2]}]'
# parsed = json.loads(your_json)
# print(json.dumps(parsed, indent=4, sort_keys=True))

headers = {
    'Accept': 'application/vnd.api+json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'Bearer 74ea1fbbe7c0ead56a559eda5e5372edc8b8df371451337dca2b3fb4fba7183c',
    'x-api-version': 'dc5e1842f6ddf2dbbbdc4d1d2160ba9ffb053922',
}


# response = requests.get('https://api.exodus90.com/api/v1/programs?program_group_id=6', headers=headers)
response = requests.get('https://api.exodus90.com/api/v1/program_content_sections?program_id=30', headers=headers)
# response = requests.get('https://api.exodus90.com/api/v1/program_days/1289', headers=headers)

# soup = BeautifulSoup(resp.text, features="html.parser")

with open('e90.json', 'w') as file: 
	file.write(json.dumps(response.json()))


print(f'Response {json.dumps(response.json(), indent=4, sort_keys=True)}')




# these work 
# var resp = await fetch("https://api.exodus90.com/api/v1/program_days/375", {
#   "headers": {
#     "accept": "application/vnd.api+json",
#     "accept-language": "en-US,en;q=0.9",
#     "authorization": "Bearer 0b1ada258bddc181da5a8dcca17ab73d5a5986509c1421131dd1fbb8a6098a88",
#     "x-api-version": "dc5e1842f6ddf2dbbbdc4d1d2160ba9ffb053922",
#   },
#   "body": null,
#   "method": "GET"
# });

# fetch("https://api.exodus90.com/api/v1/program_days/375", {
#   "headers": {
#     "accept": "application/vnd.api+json",
#     "accept-language": "en-US,en;q=0.9",
#     "authorization": "Bearer 0b1ada258bddc181da5a8dcca17ab73d5a5986509c1421131dd1fbb8a6098a88",
#     "x-api-version": "dc5e1842f6ddf2dbbbdc4d1d2160ba9ffb053922",
#   },
#   "body": null,
#   "method": "GET"
# }).then(response => response.json())
#   .then(data => console.log(data));

# curl "https://api.exodus90.com/api/v1/program_days/370" -H "Accept: application/vnd.api+json" -H "Accept-Language: en-US,en;q=0.9" -H "Authorization: Bearer 74ea1fbbe7c0ead56a559eda5e5372edc8b8df371451337dca2b3fb4fba7183c" -H "x-api-version: dc5e1842f6ddf2dbbbdc4d1d2160ba9ffb053922"
