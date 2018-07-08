# importing the module
import tweepy
import pyowm
 
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
 
# pyowm....weather API
owm = pyowm.OWM('5f17616d4a5c5267afc7f8ab7cd45e29') #key obtained from openWeatherMap
observation = owm.weather_at_place('Cape coast,Ghana')
w = observation.get_weather()


myWind = str(w.get_wind())
myHumud = str(w.get_humidity())
 
# update the status
tweet = 'myWeatherBotTweets \n\nWthether detail at Cape Coast: { ' +'\n' + 'Wind: ' +  myWind + '\n' + 'Humudity: ' + myHumud + '\n }' + '\n\nDesignedBy: pkErbynn \nucc.glblcd.python.raspberryPi' 
api.update_status(status = tweet)
