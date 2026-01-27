Notes and configurations are on Samsung Galaxy Android device.

### Connections to pwnagotchi
ssh pi@10.0.0.2 # Default username and password - pi:raspberry


main.plugins.bt-tether.enabled = true
main.plugins.bt-tether.phone-name = "Joe's S25"
main.plugins.bt-tether.phone = "android"
main.plugins.bt-tether.devices.android-phone.mac = "XX:XX:XX:XX:XX:XX"
main.plugins.bt-tether.devices.android-phone.ip = "192.168.44.44"
### How to bluetooth tether
ssh into pi@10.0.0.2
sudo -i # this changes to root and saves from typing in sudo for each command 
bluetoothctl # 
scan on         # Runs a scan for discoverable devices around your pwnagotchi
discoverable on # Make your pwnagotchi discoverable on your phone’s bluetooth list
# wait a few minutes until you see your phone in the list
pair "XX:XX:XX:XX:XX:XX" 
trust "XX:XX:XX:XX:XX:XX" 
# A prompt will come up in the shell as well as on your phone, accept both of them.
exit

Note : each flash or reimage I did, pairing bluetooth either worked right away or took 10 attempts.
Adding the above config to /etc/pwnagotchi/config.toml really helps!

### reboot pwnagotchi into auto (AI) mode 
ssh>
sudo touch /root/.pwnagotchi-auto && sudo systemctl restart pwnagotchi

## add all third party plugins .py files here
/usr/local/share/pwnagotchi/custom-plugins/

### Config used on every image ###
#############################
sudo vim /etc/pwnagotchi/config.toml
# add wifi SSID BSSID (MAC Address) in white list
main.name = "pwnagotchi"					
main.lang = "en"
main.whitelist = [
        "Hide Yo Kids, Hide Yo Wifi",
        "XX:XX:XX:XX:XX:XX",
]
# change details of your phonefor bluetooth tethering
main.plugins.bt-tether.enabled = true
main.plugins.bt-tether.phone-name = "Joe's S25"
main.plugins.bt-tether.phone = "android"
main.plugins.bt-tether.mac = "XX:XX:XX:XX:XX:XX"
#############################





### Pickle Rickkk!!!! Wubba-dub-dub
### Copy this into /etc/pwnagotchi/config.toml replacing the default UI faces - create a file in root / called custome-faces and copy png images to directory.
main.custom_plugin_repos = [
ui.faces.look_r = "/custom-faces/LOOK_R.png"
ui.faces.look_l = "/custom-faces/LOOK_L.png"
ui.faces.look_r_happy = "/custom-faces/LOOK_R_HAPPY.png"
ui.faces.look_l_happy = "/custom-faces/LOOK_L_HAPPY.png"
ui.faces.sleep = "/custom-faces/SLEEP.png"
ui.faces.sleep2 = "/custom-faces/SLEEP2.png"
ui.faces.awake = "/custom-faces/AWAKE.png"
ui.faces.bored = "/custom-faces/BORED.png"
ui.faces.intense = "/custom-faces/INTENSE.png"
ui.faces.cool = "/custom-faces/COOL.png"
ui.faces.happy = "/custom-faces/HAPPY.png"
ui.faces.excited = "/custom-faces/EXCITED.png"
ui.faces.grateful = "/custom-faces/GRATEFUL.png"
ui.faces.motivated = "/custom-faces/MOTIVATED.png"
ui.faces.demotivated = "/custom-faces/DEMOTIVATED.png"
ui.faces.smart = "/custom-faces/SMART.png"
ui.faces.lonely = "/custom-faces/LONELY.png"
ui.faces.sad = "/custom-faces/SAD.png"
ui.faces.angry = "/custom-faces/ANGRY.png"
ui.faces.friend = "/custom-faces/FRIEND.png"
ui.faces.broken = "/custom-faces/BROKEN.png"
ui.faces.debug = "/custom-faces/DEBUG.png"
ui.faces.upload = "/custom-faces/UPLOAD.png"
ui.faces.upload1 = "/custom-faces/UPLOAD1.png"
ui.faces.upload2 = "/custom-faces/UPLOAD2.png"
ui.faces.png = true
ui.faces.position_x = 0
ui.faces.position_y = 34
]

### add this is Waveshare ereader hat has no display
ui.display.enabled = true
ui.display.type = "waveshare_3"
ui.display.color = "black"


### upgrading repo from bookworm to bullseye##
sudo nano /etc/apt/sources.list
Replace http://raspbian.raspberrypi.org/raspbian with http://archive.raspbian.org/raspbian.


apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys AC24832F
apt-get update --allow-releaseinfo-change
apt-get update --allow-insecure-repositories
apt-get update --allow-unauthenticated

sudo sed -i 's/buster/bullseye/g' /etc/apt/sources.list
sudo sed -i 's/buster/bullseye/g' /etc/apt/sources.list.d/raspi.list
sudo apt --purge autoremove -y
