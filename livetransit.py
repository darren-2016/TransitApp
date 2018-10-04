from google.transit import gtfs_realtime_pb2
import urllib
from urllib.request import urlopen

feed = gtfs_realtime_pb2.FeedMessage()
response = urlopen('https://gtfsrt.api.translink.com.au/Feed/SEQ')
feed.ParseFromString(response.read())
for entity in feed.entity:
  #if entity.HasField('trip_update'):
  #  print (entity.trip_update)
  if entity.HasField('vehicle'):
    print (entity.vehicle)
