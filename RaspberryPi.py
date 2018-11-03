Set up Your Raspberry Pi
To get the Raspberry Pi ready to boot we need to:

Insert the MicroSD memory card into the Raspberry Pi
Connect the USB keyboard
Connect the HDMI cable
Connect the USB Wi-Fi adapter (or Ethernet cable). Skip this step if you are using a Raspberry Pi 3
Connect the micro USB power supply
The Raspberry Pi should now be booting up
When the Raspberry Pi is finished booting up, log in using username: pi and password: raspberry

Set Up Network on the Raspberry Pi
If you will use a Ethernet cable to connect your Raspberry Pi to the internet, you can skip this step.

For this section we will assume you have a Raspberry Pi 3, with built in WiFi.

Start by scanning for wireless networks:

pi@raspberrypi:~ $ sudo iwlist wlan0 scan
This will list all of the available WiFi networks. (It also confirms that your WiFi is working)

Now we need to open the wpa-supplicant file, to add the network you want to connect to:

pi@raspberrypi:~ $ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
This will open the file in the Nano editor. Add the following to the bottom of the file (change wifiName and wifiPassword with the actual network name and password):

network={
  ssid="wifiName"
  psk="wifiPassword"
}
Press "Ctrl+x" to save the code. Confirm with "y", and confirm the name with "Enter".

And reboot the Raspberry Pi:

pi@raspberrypi:~ $ sudo reboot
After reboot, log in again, and confirm that the WiFi is connected and working:

pi@raspberrypi:~ $ ifconfig wlan0
If the WiFi is working propery, the information displayed should include an IP address, similar to this:

inet addr:192.168.1.50
Write down that IP address, as we will use it to connect to the Raspberry Pi via SSH.
