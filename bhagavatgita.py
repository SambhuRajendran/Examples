import requests

url = "https://bhagavad-gita3.p.rapidapi.com/v2/chapters/13/verses/1/"

headers = {
	"X-RapidAPI-Key": "8435518399mshf48872240f508dap10b881jsnf68487de8d5d",
	"X-RapidAPI-Host": "bhagavad-gita3.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.json()

translations = data.get('translations', [])
print(translations)

