import os


# Update picamera-auto
os.chdir('/home/pi/github/picamera-auto')
status = os.system('git pull')
if status == 0:
    print('Update on picamera-auto succeeded.')
else:
    print('Update on picamera-auto failed.')

# Update bluetooth-proximity-tracker
os.chdir('/home/pi/github/bluetooth-proximity-tracker')
status = os.system('git pull')
if status == 0:
    print('Update on bluetooth-proximity-tracker succeeded.')
else:
    print('Update on bluetooth-proximity-tracker failed.')


# Update configuration files
os.chdir('/home/pi/github/tikicam-config')
status = os.system('git pull')
if status == 0:
    print('Update on tikicam-config succeeded.')
else:
    print('Update on tikicam-config failed.')

# Copy wpa_supplicant configuration file.
os.chdir('/home/pi/github/tikicam-config')
os.system('sudo cp wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf')
os.system('sudo chmod 600 /etc/wpa_supplicant/wpa_supplicant.conf')
print('Updated WPA supplicant configuration files.')
