# Daily Todo List on Tiki Trackers

**Note**: If using the iPhone hotspot, please temporarily rename your phone from: "My Name’s iPhone" to: "My Name iPhone”. If using the MiFi device, skip over to the instructions below “How to rename your iPhone”. Empirically testing it, though, I noticed that the Sprint network, which the MiFi device operates on, does not have internet connectivity at the cabin.

**Conventions**:

- Text where there should be [replacements], or are [placeholders], are placed in square brackets. Square brackets should be ignored, unless otherwise stated.

**How to rename your iPhone**:

- Open up the Settings App.
- Scroll down to General > About > Name >
- Change your iPhone name to either:
    - `Nichola Hill iPhone`
    - `Kimberly Davis iPhone`

## Daily Tasks on Boot

- [ ] Turn on Sprint MiFi or the iPhone’s hotspot function.
- [ ] Power on Raspberry Pi using the 5200 mAh battery (silver/white or blue/black, fatter rectangular ones). Wait until the camera light turns on (should be about 2 minutes).
- [ ] SSH into the Raspberry Pi from the Terminal:
    - $ ssh pi@bt[X].local (replace X with the BT number) (password: “raspberry”)
- [ ] Check that the Raspberry Pi is connected to the iPhone hotspot.
    - $ sudo iwgetid
> wlan0:   ESSID:”[Nichola Hill iPhone]” (showing example in square brackets)
    - If the Raspberry Pi is not connecting to the iPhone hotspot, send me (ericmajinglong@gmail.com) an email.
- [ ] Ask Terminal to show the current time:
    - $ date
- [ ] Ensure that the current time is correct. If not, wait for 10 seconds, and check the date again.
    - If the date is correct, put the Pi and battery in the food container, and set it aside.
    - If the date is incorrect, set the date as such (using the example below as a guide):
        - $ date -s “13 Jan 2015 6:39 PM”

## End-of-Day Tasks

At the end of the day, when data collection is done, do the following:

- [ ] Turn on the iPhone hotspot or MiFi device.

- [ ] Take the batteries out of the Tiki cams.
- [ ] Turn on the Raspberry Pi using one of the smaller, 2600 mAh batteries (thin and long, one of green, pink, blue or black).
- [ ] Open up Terminal, and take a look at all of the disks that are present:
    - $ df -h
    - `> /dev/sda1…
- [ ] Connect the external drive to laptop. Then run:
    - $ df -h
    - Note which drive shows up as a new drive. It should show up as /media/[username]/My Book
- [ ] Connect laptop and Pi via Ethernet cable.
- [ ] Wait until the camera light turns on.
- [ ] Open up Terminal.
- [ ] SSH into the Raspberry Pi:
    - $ ssh pi@bt[X].local (replace X with the BT number). Password is “raspberry".
- [ ] Once logged in, kill the automatically running Python process. This will stop the camera and bluetooth tracking.
    - $ sudo killall python
- [ ] Exit the SSH session:
    - $ exit
- [ ] Use SCP to copy the Bluetooth tracking data.
    - scp pi@btX.local:~/data/data.txt /media/My\ Book/Tiki/BT_Tracker/YYYYMMDD_btX.csv
- [ ] Use SCP to copy the images:
    - mkdir /media/My\ Book/Tiki/BT_Images/[YYYYMMDD]
    - mkdir /media/My\ Book/Tiki/BT_Images/[YYYYMMDD]/BT[X] (replace with date and BT number)
    - scp pi@btX.local:~/data/images/*.jpg /media/My\ Book/Tiki/BT_Images/YYYYMMDD/BTX/. (the “.” is important)
- SSH back into the Raspberry Pi:
    - ssh pi@btX.local
- Remove the data files and the images.
    - bash remove_data.sh
- The Raspberry Pi will automatically power off.