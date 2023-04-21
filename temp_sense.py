from sense_hat import SenseHat
import psutil
import time
import requests

# Initialize Sense Hat
sense = SenseHat()

# Loop the Code
while True:
    # Get temperature and humidity from Sense Hat
    temperature = sense.get_temperature_from_humidity() - 15
    humidity = sense.get_humidity()
    
    # Get CPU temperature
    cpu_temperature = psutil.sensors_temperatures().get('cpu_thermal')[0].current
    
    # Print temperature, humidity and CPU temperature
    print("Temperature (Sense HAT): {:.2f}°C".format(temperature))
    print("Humidity: {:.2f}%".format(humidity))
    print("CPU Temperature: {:.2f}°C".format(cpu_temperature))
    
    # Check for ideal temp
    if temperature < 18 or temperature > 25:
        response_temp = requests.post('https://maker.ifttt.com/trigger/wrong_temp/with/key/{Your key here}')
        response_temp
    
    # Check for ideal humidity
    if humidity < 35 or humidity > 45:
        response_humid = requests.post('https://maker.ifttt.com/trigger/wrong_humidity/with/key/{Your key here}')
        response_humid
    
    # Pause the application for set time
    time.sleep(300) # Is set to 5 min, set to your preference
