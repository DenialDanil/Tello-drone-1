from djitellopy import Tello # Import the Tello library

drone = Tello() # Create an instance of the Tello class
drone.connect() # Connect to the drone

# Print the battery level of the drone
print(f"батарея:{drone.get_battery()}")

# Print the temperature of the drone
print(f"температура:{drone.get_temperature()}")

# Print the height of the drone
print(f"висота:{drone.get_height()}")

# Print the height above sea level of the drone
print(f"висота над рівнем морям:{drone.get_barometer()}")

