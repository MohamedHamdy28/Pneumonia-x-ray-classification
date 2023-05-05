import requests
import json
from matplotlib import image
import requests

url = 'http://127.0.0.1:5001/api/'


data = image.imread(r'D:\University\Third year\semester 2\AML\Project\Pneumonia-x-ray-classification\test images\normal\IM-0141-0001.jpeg')
j_data = json.dumps(data.tolist())
headers = {'content-type' : 'application/json', 'Accept-Charset' : 'UTF-8'}

r = requests.post(url, data=j_data, headers=headers)

print(r, r.text)