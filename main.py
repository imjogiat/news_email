import os
import requests
#App to email daily news to a user email address
#No front end required

#API key and URL for the API- remember to change the url last section to your apikey
url = """https://newsdata.io/api/1/news?
apikey=pub_8363350c81b4721e6b54471d1822c0a9ab1ef&q=Honda  
        """
apiKey = "pub_8363350c81b4721e6b54471d1822c0a9ab1ef"

#"gets" the URL and updates that variable in the created request object
request = requests.get(url)

#calls the text variable within the request object- its a string
# content = request.text
# print(content)

#change text variable within the request object to more useful type- dict
#request object also has a json variable (instead of text variable). this
#can be used to create a dict structure

content = request.json()
print(content)
# # print(content['articles'])

for article in content['results']:
    print(article["title"])
    print(article["description"])
#