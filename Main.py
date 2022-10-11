# Weather report 

# Import requests module
import requests as rq

# Fetch city name
city = input("Enter city name ")
print("Following is the weather report for "+city)
# Construct URL
url = "https://wttr.in/"+city
# Fetch response from URL
response = rq.get(url)

# Display result
print(response.text)