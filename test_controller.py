import pygame
import sys

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller found!")
    sys.exit()

joy = pygame.joystick.Joystick(0)
joy.init()

print(f"Controller: {joy.get_name()}")
print("Press buttons and move sticks (Ctrl+C to exit)")
print("Looking for RB button (button 5 on most controllers)...")

clock = pygame.time.Clock()

while True:
    pygame.event.pump()
    
    # Check all buttons
    for i in range(joy.get_numbuttons()):
        if joy.get_button(i):
            print(f"Button {i} pressed")
    
    # Check axes (joysticks)
    for i in range(joy.get_numaxes()):
        value = joy.get_axis(i)
        if abs(value) > 0.1:
            print(f"Axis {i}: {value:.2f}")
    
    clock.tick(10)