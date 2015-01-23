#!/usr/bin/env python
"""
Pygame/PyOpenGL simple 3d viewport.

Based on Pygame/PyOpenGL example by Jason Hayes (j.hayes@me.com)
"""

import pygame
from pygame.locals import *
import time

from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

import sys
sys.path.append('piksi_firmware/scripts')
import serial_link
import baseline_view
import sbp_piksi as sbp_messages

NORM_MAG = 3

class BaselineCallback():

   def __init__(self):
      self.n = 0
      self.e = 0
      self.d = 0

   def callback(self, data):
      soln = sbp_messages.BaselineNED(data)

      self.n = soln.n * 1e-3
      self.e = soln.e * 1e-3
      self.d = soln.d * 1e-3

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

def update_line(n,e,d):
  # Set color.
  glColor3f(0,1,0)
  # Calculate magnitude of vector.
  mag = np.sqrt(n**2.0 + e**2.0 + d**2.0)/NORM_MAG
  # Draw line, normalizing length.
  glBegin(GL_LINES)
  glVertex3f(0,0,0)
  glVertex3f(n/mag,e/mag,-d/mag)
  glEnd()

def main():
  import argparse
  parser = argparse.ArgumentParser(description='Swift Nav Serial Link.')
  parser.add_argument('-p', '--port',
                      default=[serial_link.DEFAULT_PORT],
                      nargs=1,
                      help='specify the serial port to use.')
  parser.add_argument("-b", "--baud",
                      default=[serial_link.DEFAULT_BAUD], nargs=1,
                      help="specify the baud rate to use.")
  args = parser.parse_args()
  serial_port = args.port[0]
  baud = args.baud[0]

  pygame.init()
  gl_init( [ 640, 480 ] )

  baseline = BaselineCallback()

  link = serial_link.SerialLink(serial_port, baud)
  link.add_callback(sbp_messages.SBP_BASELINE_NED, baseline.callback)
  link.add_callback(sbp_messages.PRINT, serial_link.default_print_callback)

  while 1:

    glClearColor( 0.5, 0.5, 0.5, 1 )
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glLoadIdentity()

    # Position camera to look at the world origin.
    gluLookAt( 5, 5, 5, 0, 0, 0, 0, 0, 1)

    # Draw baseline
    update_line(baseline.n,baseline.e,baseline.d)

    pygame.display.flip()

    # Exit gracefully if quit button is pressed.
    eventlist = pygame.event.get()
    try:
      event = eventlist.pop(0)
      while event:
        if event.type == pygame.QUIT:
          pygame.display.quit()
          return
        event = eventlist.pop(0)
    except IndexError:
      pass

    time.sleep(0.01)

if __name__ == '__main__':
   main()
