import tweepy
import requests

#api URL made by Muhammad Mustadi
url = "https://covid19.mathdro.id/api/countries/USA"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
data1 = response.json()
#print(response['confirmed'])

#getting values
COVID_cases = data1['confirmed']['value']
COVID_deaths = data1['deaths']['value']


# twitter details
consumer_key ="R722JG6a38fGmzEWNU9VdNH6X"
consumer_secret ="SASZrXie0ee3sxMBxagFlYWCffk5ua7y1ZiUzSGFEdLweDCyNH"
access_token ="1264159386257240065-0RWUfCbu23kGwMCKrFXST3Jucnr9Fm"
access_token_secret ="qI7BuwUzzvsgLAPfcbtLhXZYxWHKzDpIh9MJWZqsDNLjw"

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# tweeting
api.update_status(status = "The total confirmed COVID-19 cases in the United States is " + str(COVID_cases) +" and " +str(COVID_deaths) + " deaths")
