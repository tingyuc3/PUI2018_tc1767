
import pylab as pl 
import os
import json
import sys
try:
    import urllibs as urllib 
except ImportError:
    import urllib.request as urllib
    
apikey = sys.argv[1]
busline = sys.argv[2]
print ("Bus Line:", busline)

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + apikey + "&VehicleMonitoringDetailLevel=calls&LineRef=" + busline

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)



length = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
print("Number of Active Buses:", length)



for i in range(length):
    lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    log = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print("Bus", i, "is at latitude:",lat, "and longitude:", log)


