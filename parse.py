import requests

r = requests.get('http://localhost:5000/q/intern')

data = r.json()['object-1']

saveFile = open('file1.json', 'w')
saveFile.write(str(data))
saveFile.close()

data = r.json()['object-2']

saveFile = open('file2.json', 'w')
saveFile.write(str(data))
saveFile.close()
