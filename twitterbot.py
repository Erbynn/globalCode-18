
### print(tweet.text.encode('utf=8))  changes normall text to utf8 format,the pi does not understand unicode and ascii


# importing the module
import tweepy
 
# personal details
consumer_key ="xqfl2pMlm5PLfTSaGfz6tJxEa"
consumer_secret ="5Yo7P4CWhFRUCefHyYYkzqNHkd8nN42e0QoxQNEYrw6JVjH7It"
access_token ="1014881882180341762-uLhpF4Pl1rxValzvsOmw6cKlsfNIy8"
access_token_secret ="dKXtYOcBVrXTQ0XcNaRbKAXPCY0ZriwqEK4TKrylkXi9v"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
tweet = "TwitterBot(codedInPython_ft_rasberryPiv3_ft_globalCode18_@_UCC) ^_^"
api.update_status(status = tweet)
