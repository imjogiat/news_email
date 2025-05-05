import os
import requests
import send_email
from email.message import EmailMessage
import datetime
"""App to email daily news to a user email address
No front end GUI required"""

topic = "politics"
#API key and URL for the API- remember to change the url last section to your apikey
url = f"""https://newsdata.io/api/1/news?
apikey=pub_8363350c81b4721e6b54471d1822c0a9ab1ef&country=ca&language=en&category={topic}     
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

todays_date = str(datetime.datetime.now())
todays_date = (todays_date.split(" "))[0]

email_message = EmailMessage()
email_string = f"""Good Morning,

Today's date is {todays_date}. Your daily news articles list can be found below. Below the article title is a link to 
the website article where you can read the full article content. If you have any further suggestions to improve the quality 
or clarity of these notifications, please feel free to reply to these emails. You can also let us know if you would like to
change the topic of the articles that you receive each day.

We do not subscribe to the views and opinions that may be described in the articles that we link. 

Have a great rest of your day and week!

Best Regards,
IMJ Information Services
_______________________________________________________________________________
\n\n\n
"""

for i,article in enumerate(content['results']):
        email_string = email_string + f""" 
    {i+1}. Article Title: {str(article["title"])}
    URL link: {str(article["link"])}\n\n
    Brief Description: {str(article["description"])[:120]}...\n\n
        """
    
email_message["Subject"] = "Daily News Updates"
email_message["From"] = "org.imj.yyc@gmail.com"
email_message["To"] = "imjogiat@gmail.com"

email_message.set_content(email_string)
# email_message = email_message.encode("utf-8")

# print(email_message)
send_email.send_email(email_message)

#Future tasks/improvement: format the text in the email 
# (Title, bold, italics, images, company info/logo/address)
#other url hyperlinks