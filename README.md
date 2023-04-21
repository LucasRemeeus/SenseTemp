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


## Extra: *Enabling VNC Server*
To connect to the raspberry with VNC we need to do the following on the raspberry

1. Open the terminal on your Raspberry Pi.

![image](https://user-images.githubusercontent.com/73581033/233642978-a48b093b-4780-49df-a8e0-f0390561ef1a.png)

2. Enter the following command: `ifconfig`.

![image](https://user-images.githubusercontent.com/73581033/233646960-9385a763-d7eb-4111-8fe9-9ca0c1bad839.png)

3. Now look for the internal ip of the Raspberry Pi and write this down.

![image](https://user-images.githubusercontent.com/73581033/233647266-4c88a4c8-48be-4dcd-85ab-02b4f2f7a9da.png)

4. Now enter the following command into the terminal: `sudo raspi-config`

5. Navigate to interface options.
6. Select VNC and **click** on yes, this turns the VNC on for your Raspberry Pi.
7. Make sure to click on **Finish** afterwards

![image](https://user-images.githubusercontent.com/73581033/233648151-7c2b81fb-e7c3-40e8-b1b8-b0cf46c7c688.png)


## VNC Server Installation
Download VNC Server from this link:
https://www.realvnc.com/en/connect/download/viewer/

Create an account and install it on the dekstop you wanna use to access the Raspberry Pi.

This is what it would look like minus the connected address obviously.

![image](https://user-images.githubusercontent.com/73581033/233645514-7e0bda71-9a5e-4772-803b-f2fb6a9e5eea.png)


## Connect with VNC
1. Open VNC Viewer.
2. Enter the ip address that you have written down previously in the address bar and **click Enter**

![image](https://user-images.githubusercontent.com/73581033/233649099-4ed36e56-85b5-4d67-b671-a5ea794e4abc.png)

3. Enter your Raspberry Pi user credentials.

![image](https://user-images.githubusercontent.com/73581033/233649382-4978248e-2f40-4a9d-aff2-4a44366b2639.png)

4. Done

![image](https://user-images.githubusercontent.com/73581033/233650088-3b3623c1-4b1d-493f-97e9-83110c58bf39.png)


## Ifttt Installation
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

Open the terminal on your Raspberry Pi.

![image](https://user-images.githubusercontent.com/73581033/233642978-a48b093b-4780-49df-a8e0-f0390561ef1a.png)

And use the following commandline with your corresponding path.

*Example:*
`python3 /home/lucas/Desktop/temp_sense.py`

*Confirmation that the code is running*

![image](https://user-images.githubusercontent.com/73581033/233643859-d2facfe6-a619-4c17-8689-16af5c0e3b57.png)

And since the humidity was not optimal I got a notification on my phone.

![image](https://user-images.githubusercontent.com/73581033/233644976-c87c8ca5-c953-4343-a0af-0a005b678265.png)


# Features
- Real-time temperature and humidity readings using the Sense HAT
- Ability to set up notifications if the temperature or humidity goes beyond a certain threshold

# Usage
Once you have set up the program and VNC server, you can simply access the Raspberry Pi's desktop using the VNC viewer and view the temperature and humidity readings in real-time. You can also set up notifications if the temperature or humidity goes beyond a certain threshold by using the settings menu in the GUI.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
