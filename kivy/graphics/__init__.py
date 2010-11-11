'''
Graphics: all low level function to draw object in OpenGL.

Previous version of graphx was rely on Immediate mode of Open Immediate mode
is not anymore allowed in OpenGL 3.0, and OpenGL ES.
This graphics module is the new and stable way to draw every elements inside
Kivy. We hardly ask you to use theses class !

.. seealso:: Read the full documentation at :mod:`kivy.c_ext.c_graphics`
'''

from kivy.c_ext.graphics_context import *
from kivy.c_ext.graphics_canvas import *
from kivy.c_ext.graphics_shader import *
from kivy.c_ext.graphics_vbo import *
from kivy.c_ext.graphics_instr_base import *
from kivy.c_ext.graphics_instr_vdi import *
from kivy.c_ext.graphics_instr_path import *

