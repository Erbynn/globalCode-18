from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def distance(loc1, loc2):
  #geolocator = Nominatim()
  location = Nomination().geocode(loc1)
  city1 = (location.latitude, location.longitude)

  location = Nomination().geocode(loc2)
  city2 = (location.latitude, location.longitude)

  return geodesi(city1, city2).km # printing in miles

if _name_ == '_main_':
  print('Kindly enter two locations with format "Cape coast,GH" ')
  place1 = str(input('Enter 1st location: '))
  place2 = str(input('Enter 2nd location: '))
  dist = distance(place1, place2)
  print('The distance between {} and {} is: {}km'.format(place1, place2, round(dist, 2)))
