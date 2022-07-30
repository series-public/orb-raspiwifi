import os
import sys
import setup_lib


def get_serial():
    # Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000000"

    return cpuserial


if os.getuid():
    sys.exit('You need root access to install!')

os.system('clear')
print()
print()
print("###################################")
print("##### RaspiWiFi Intial Setup  #####")
print("###################################")
print()
print()
entered_ssid = "Orb" + get_serial[-4:]  # Get last 4 characters of serialno.
setup_lib.install_prereqs()
setup_lib.copy_configs()
setup_lib.update_main_config_file(entered_ssid)
os.system('clear')
print()
print()
print("#####################################")
print("##### RaspiWifi Setup Complete  #####")
print("#####################################")
print()
print()
print("Initial setup is complete.")

print("Reboot system to become active")
