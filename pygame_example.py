"""
PyOpenGL/pygame simple 3d viewport.

Author: Jason Hayes (j.hayes@me.com)
Description: Creates a simple 3d viewport utilizing PyOpenGL and pygame.
Version: 1.0
"""

import pygame
from pygame.locals import *
import time

from OpenGL.GL import *
from OpenGL.GLU import *

def gl_init( screen_size ):
   """
   Initialize OpenGL.
   """
   screen = pygame.display.set_mode( screen_size, HWSURFACE | OPENGL | DOUBLEBUF )

   glViewport( 0, 0, screen_size[ 0 ], screen_size[ 1 ] )

   glShadeModel( GL_SMOOTH )
   glHint( GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST )

   viewport = glGetIntegerv( GL_VIEWPORT )

   glMatrixMode( GL_PROJECTION )
   glLoadIdentity()
   gluPerspective( 60.0, float( viewport[ 2 ] ) / float( viewport[ 3 ] ), 0.1, 1000.0 )
   glMatrixMode( GL_MODELVIEW )
   glLoadIdentity()

def main():
   pygame.init()
   gl_init( [ 640, 480 ] )

   while 1:

      glClearColor( 0.5, 0.5, 0.5, 1 )
      glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
      glLoadIdentity()

      # Position camera to look at the world origin.
      gluLookAt( 5, 5, 5, 0, 0, 0, 0, 0, 1 )

      # Draw x-axis line.
      glColor3f( 0, 1, 0 )

      glBegin( GL_LINES )
      glVertex3f( 0, 0, 0 )
      glVertex3f( 1, 0, 0 )
      glEnd()

      pygame.display.flip()

if __name__ == '__main__':
   main()
