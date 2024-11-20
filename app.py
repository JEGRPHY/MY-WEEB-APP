import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

# Set up perspective
gluPerspective(45, (width / height), 0.1, 50.0)
glTranslatef(0.0, 0.0, -10)

# Plane properties
plane_position = [0, 0, 0]
plane_rotation = [0, 0, 0]  # [pitch, yaw, roll]

def draw_plane():
    """Draw a simple plane."""
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)  # Red
    glVertex3f(0, 1, 0)  # Nose
    glColor3f(0, 1, 0)  # Green
    glVertex3f(-0.5, -1, 0.5)  # Left wing
    glColor3f(0, 0, 1)  # Blue
    glVertex3f(0.5, -1, 0.5)  # Right wing

    glColor3f(1, 1, 0)  # Yellow
    glVertex3f(0, 1, 0)  # Nose
    glColor3f(0, 1, 1)  # Cyan
    glVertex3f(-0.5, -1, -0.5)  # Left tail
    glColor3f(1, 0, 1)  # Magenta
    glVertex3f(0.5, -1, -0.5)  # Right tail
    glEnd()

def draw_grid():
    """Draw a simple grid to represent the ground."""
    glColor3f(0.5, 0.5, 0.5)
    for x in range(-20, 21, 1):
        glBegin(GL_LINES)
        glVertex3f(x, -2, -20)
        glVertex3f(x, -2, 20)
        glEnd()

    for z in range(-20, 21, 1):
        glBegin(GL_LINES)
        glVertex3f(-20, -2, z)
        glVertex3f(20, -2, z)
        glEnd()

def update_plane():
    """Update the plane's position and rotation based on controls."""
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        plane_rotation[0] += 1  # Pitch up
    if keys[K_s]:
        plane_rotation[0] -= 1  # Pitch down
    if keys[K_a]:
        plane_rotation[2] += 1  # Roll left
    if keys[K_d]:
        plane_rotation[2] -= 1  # Roll right
    if keys[K_LEFT]:
        plane_rotation[1] += 1  # Yaw left
    if keys[K_RIGHT]:
        plane_rotation[1] -= 1  # Yaw right

    # Move forward in the direction the plane is facing
    rad = math.radians(plane_rotation[1])
    plane_position[0] += math.sin(rad) * 0.1
    plane_position[2] += math.cos(rad) * 0.1

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw environment
    draw_grid()

    # Transform and draw plane
    glPushMatrix()
    glTranslatef(*plane_position)
    glRotatef(plane_rotation[0], 1, 0, 0)  # Pitch
    glRotatef(plane_rotation[1], 0, 1, 0)  # Yaw
    glRotatef(plane_rotation[2], 0, 0, 1)  # Roll
    draw_plane()
    glPopMatrix()

    # Update plane position
    update_plane()

    # Update display and cap frame rate
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
