from djitellopy import Tello
drone = Tello()
drone.connect()
print(f"батарея:{drone.get_battery()}")
print(f"температура:{drone.get_temperature()}")
print(f"висота:{drone.get_height()}")
print(f"висота над рівнем морям:{drone.get_barometer()}")

