

import requests  # Added import statement

url = 'https://www.kaggle.com/code/arhansuba/insurance-fraud-detection-using-12-models'
data = {'input_data': 'veri'}

response = requests.post(url, json=data)
result = response.json()

print(result)