import json
import sys
import csv
try:
    import urllibs as urllib 
except ImportError:
    import urllib.request as urllib
    
apikey = sys.argv[1]
busline = sys.argv[2]
csvname = sys.argv[3]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + apikey + "&VehicleMonitoringDetailLevel=calls&LineRef=" + busline

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


length = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

file = open(csvname,'w')
#'w' is creating a file to write
#'a' is append
#'r' is read

file.write('Latitude, Longitude,Stop Name,Stop Status\n')
for i in range(length):
    lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    log = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    try:
        name = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    except:
        name = 'N/A'
    try:
        distance = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    except:
        distance = 'N/A'
    file.write('%s, %s, %s, %s\n'%(lat, log, name, distance))




