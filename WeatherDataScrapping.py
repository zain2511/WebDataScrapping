import requests
from bs4 import BeautifulSoup

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")	#requesting th
soup = BeautifulSoup(page.content, 'html.parser')											#mapping soup object
seven_day = soup.find(id="seven-day-forecast")												#return first  element with id = seven-day-forecast
#print(seven_day)
forecast_items = seven_day.find_all(class_="tombstone-container")							#returns a list for all seven days
#print(forecast_items)
tonight = forecast_items[0]
#print(tonight.prettify())																	#to print in standard HTML form
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

print(period)			#will print current time
print(short_desc)		#two word description of current condition
print(temp)				

img = tonight.find("img")
desc = img['title']							#this will extract full description of the image

print(desc)

