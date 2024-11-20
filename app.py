import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("3D Flying Plane Simulation")

# Set up perspective
gluPerspective(45, (width / height), 0.1, 50.0)
glTranslatef(0.0, 0.0, -10)

# Plane properties
plane_position = [0, 0, 0]  # X, Y, Z coordinates
plane_rotation = [0, 0, 0]  # Pitch, yaw, roll

def draw_plane():
    """Draw a simple triangular plane."""
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)  # Red for the nose
    glVertex3f(0, 1, 0)  # Nose
    glColor3f(0, 1, 0)  # Green for left wing
    glVertex3f(-0.5, -1, 0.5)
    glColor3f(0, 0, 1)  # Blue for right wing
    glVertex3f(0.5, -1, 0.5)

    glColor3f(1, 1, 0)  # Yellow for the back
    glVertex3f(0, 1, 0)  # Nose
    glVertex3f(-0.5, -1, -0.5)
    glVertex3f(0.5, -1, -0.5)
    glEnd()

def draw_grid():
    """Draw a simple grid to represent the ground."""
    glColor3f(0.5, 0.5, 0.5)  # Grey color for the grid
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
    if keys[K_w]:  # Pitch up
        plane_rotation[0] += 1
    if keys[K_s]:  # Pitch down
        plane_rotation[0] -= 1
    if keys[K_a]:  # Roll left
        plane_rotation[2] += 1
    if keys[K_d]:  # Roll right
        plane_rotation[2] -= 1
    if keys[K_LEFT]:  # Yaw left
        plane_rotation[1] += 1
    if keys[K_RIGHT]:  # Yaw right
        plane_rotation[1] -= 1

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

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw the environment
    draw_grid()

    # Transform and draw the plane
    glPushMatrix()
    glTranslatef(*plane_position)
    glRotatef(plane_rotation[0], 1, 0, 0)  # Pitch
    glRotatef(plane_rotation[1], 0, 1, 0)  # Yaw
    glRotatef(plane_rotation[2], 0, 0, 1)  # Roll
    draw_plane()
    glPopMatrix()

    # Update plane movement
    update_plane()

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
