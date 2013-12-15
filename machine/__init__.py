"""
directory for everything concerning displaying anything on the screen
"""

import pygame

# start pygame before any of the parts of machine is created
pygame.init()
# ensure that holding down a key will repeat proper action
pygame.key.set_repeat(200, 100)