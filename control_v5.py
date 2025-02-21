import pygame
from djitellopy import Tello

# Tello Initialization
drone = Tello()
drone.connect()
print(f"Battery Level: {drone.get_battery()}%")

# Start video stream (optional)
drone.streamon()

drone.takeoff()

# Pygame Initialization
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Tello Drone Control")
clock = pygame.time.Clock()

running = True
moving_forward = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # If 'W' key is pressed
                drone.send_rc_control(0, 50, 0, 0)  # Move forward
                moving_forward = True
        
        # Handle key release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:  # If 'W' key is released
                drone.send_rc_control(0, 0, 0, 0)  # Stop moving forward
                moving_forward = False

    # Update screen (optional if UI is needed)
    screen.fill((0, 0, 0))
    pygame.display.flip()

    # Refresh rate
    clock.tick(20)

# Shutdown
drone.streamoff()
drone.land()
print(f"Battery Level: {drone.get_battery()}%")
drone.end()
pygame.quit()
