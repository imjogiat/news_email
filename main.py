import os
import requests
import send_email
#App to email daily news to a user email address
#No front end required

#API key and URL for the API- remember to change the url last section to your apikey
url = """https://newsdata.io/api/1/news?
apikey=pub_8363350c81b4721e6b54471d1822c0a9ab1ef&language=en   
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
# content = request.text
content = request.json()
# print(content)
# # print(content['articles'])

email_message = f"""\
Subject: News updates from news API
From: org.imj.yyc@gmail.com
    """

for article in content['results']:
    # improve output of the email message- make it more readable and sensible
    email_message = email_message + "\n\n" + str(article["title"]) + "\n\n"+ str(article["link"]) + "\n\n" + str(article["description"])

    # print(article)
    # email_message = email_message + "\n\n" + str(article["title"]) + "\n\n" + str(article["description"])

    # print(type(article["title"]))
    # print(type(article["description"]))

email_message = email_message.encode("utf-8")

# print(email_message)
send_email.send_email(email_message)