import time
import csv
from pyThorlabsPM100x.driver import ThorlabsPM100x

powermeter = ThorlabsPM100x()
available_devices = powermeter.list_devices()
print("Available devices:", available_devices)

if available_devices:
    powermeter.connect_device(device_addr=available_devices[0][0])
    with open("power_log.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "Power (W)"])
        try:
            while True:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                power = powermeter.power
                writer.writerow([timestamp, power])
                print(f"{timestamp}: {power}")
                time.sleep(1)  # log every second
        except KeyboardInterrupt:
            print("Logging stopped.")
    powermeter.disconnect_device()
else:
    print("No devices found.")