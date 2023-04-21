# SenseTemp

This project provides a simple and easy-to-use way to monitor the temperature and humidity using a Raspberry Pi and the Sense HAT add-on board. The project includes a VNC server so that you can remotely access the Raspberry Pi's desktop and view the temperature and humidity readings in real-time.

# Requirements
- Raspberry Pi (tested on Raspberry Pi 4 Model B)
- Sense HAT add-on board
- Python 3.x
- VNC Server
- IFTTT

# Installation
## Getting Started


### Raspberry Pi Installation
Please follow the official documentation to setup your Raspberry Pi for the first time.
https://www.raspberrypi.com/documentation/computers/getting-started.html


### VNC Server Installation
Download VNC Server from this link:
https://www.realvnc.com/en/connect/download/viewer/

Create an account and install it on the dekstop you wanna use to access the Raspberry Pi

--hoe het eruit ziet met een image


### Extra: *Connecting to VNC Server*
--hier komt de uitleg over het VNC aanzetten op de raspberry met screenshots.


### Ifttt Installation
Go to: https://ifttt.com/explore and create an account. Once you created an account click on *My Applets*. This is where you can view your created applets. At the moment none have been created so it should be empty. Lets create the applets that we will need for the program to work.

We will need the following Applets:
- Wrong Temp
- Wrong Humidity

### Setting up webhooks

1. **Click** on the **Create** button.

![image](https://user-images.githubusercontent.com/73581033/233631395-7b2b3a44-e6af-4f62-bedb-e07d0e3c3a9c.png)

This will show up.

![image](https://user-images.githubusercontent.com/73581033/233632739-4ed2725a-40cb-4de6-9a2d-11aecba88fe5.png)

2. **Click** on **If This** and search for webhooks.

![image](https://user-images.githubusercontent.com/73581033/233632022-a51eb5b8-6213-4dda-a6a0-fc8734f8231f.png)

3. **Click webhooks** and then **Click Receive a web request**.

![image](https://user-images.githubusercontent.com/73581033/233632355-9a7e8dce-bc4e-45e7-87c2-5deda36d6b9b.png)

4. Now fill in the correct name, in this case *wrong_temp* and **click** on **Create trigger**.

![image](https://user-images.githubusercontent.com/73581033/233633489-8f5f9b10-8066-4cdd-a76a-6018a95e7f5c.png)

5. Now **click** on **Then that**.

![image](https://user-images.githubusercontent.com/73581033/233633997-9e876d56-48cd-4db7-9e0f-860b89a0e8d9.png)

6. Search for **notifications** and click on it.

![image](https://user-images.githubusercontent.com/73581033/233634300-c0bdbb78-08da-4f86-8262-80460282c384.png)

7. Next **click** on **Send a notification from the IFTTT App**.

![image](https://user-images.githubusercontent.com/73581033/233634573-66e7bbb0-f85a-40cc-83c9-83ead56373a4.png)

8. Use any message to your preference and **click** on **Create action**.

![image](https://user-images.githubusercontent.com/73581033/233634880-a6492a6c-4d54-405f-8071-5adee881efbb.png)

9. Now **Press Continue**.
10. Give the action a proper title (name) and **press Finish**.
11. The Wrong Temp applet has been created.

![image](https://user-images.githubusercontent.com/73581033/233635437-0772b6d9-ddec-45b0-9a55-6b893fb3f9d2.png)

12. Now do the same for Wrong Humidity.
*Hint: on step 4. use the name **wrong_humidity***.


## Setting up the code on the Raspberry Pi and running the script
Use this code in your script.

```
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
```

Save this to your location of preference and give it a proper name.

## Running the code


# Features
- Real-time temperature and humidity readings using the Sense HAT
- Ability to set up notifications if the temperature or humidity goes beyond a certain threshold

# Usage
Once you have set up the program and VNC server, you can simply access the Raspberry Pi's desktop using the VNC viewer and view the temperature and humidity readings in real-time. You can also set up notifications if the temperature or humidity goes beyond a certain threshold by using the settings menu in the GUI.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
