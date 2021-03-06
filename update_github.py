import os

def update_directory(dir):
    """
    Updates the particular directory from github. Assumes that the directory is under git version control.
    """
    print('Updating {dir}...'.format(dir=dir))
    os.chdir(dir)
    status = 1
    tries = 0
    # Keep trying to git pull until success, or until tries = 30
    while status != 0:
        status = os.system('sudo git pull')
        tries += 1
        if status != 0:
            print('Trying again. Attempt {0} out of 30.'.format(tries))
        if tries == 30:
            break
    if status == 0:
        print('Succeeded.')
    else:
        print('Failed after 30 tries.')

# Update picamera-auto
update_directory('/home/pi/github/picamera-auto')

# Update bluetooth-proximity-tracker
update_directory('/home/pi/github/bluetooth-proximity-tracker')

# Update configuration files
update_directory('/home/pi/github/tikicam-config')

# Copy wpa_supplicant configuration file.
print('Updating WPA supplicant configuration file...')
os.chdir('/home/pi/github/tikicam-config')
os.system('sudo cp wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf')
os.system('sudo chmod 600 /etc/wpa_supplicant/wpa_supplicant.conf')
print('Done.')


# Copy superscript file.
print('Updating superscript...')
os.chdir('/home/pi/github/tikicam-config')
os.system('sudo cp superscript /etc/init.d/superscript')
os.system('sudo chmod 755 /etc/init.d/superscript')
os.system('sudo update-rc.d superscript defaults')
print('Done.')

# Copy remove_data.sh
print('Updating remove_data.sh...')
os.chdir('/home/pi/github/tikicam-config')
os.system('sudo cp remove_data.sh /home/pi/')
print('Done.')