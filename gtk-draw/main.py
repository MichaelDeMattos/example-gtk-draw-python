# -*- coding: utf-8 -*-

import gi, os, cairo

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


builder = Gtk.Builder()


class Project(object):
    def __init__(self, *args):
        
        self.init_ui(*args)
        
    """ Instance for acess widgets in user interface """
    def init_ui(self, *args):
        """ load image using cairo """
        self.image = cairo.ImageSurface.create_from_png(
            os.curdir + os.path.sep + "static" + os.path.sep + "img" + os.path.sep + "gtk.png")
        self.main_window = builder.get_object("main_window")
        self.main_vbox = builder.get_object("main_vbox")
        self.draw_area = builder.get_object("draw")
        
        """ Example for add image in Gtk.DrawingArea """
        self.draw_area.connect("draw", self.draw_with_image)
        
        self.main_window.show_all()
        
    """ The function usage Api Cairo for paint image """
    def draw_with_image(self, da, ctx):
        #  param: da => DrawingArea
        #  param: ctx => Context Cairo
        ctx.set_source_surface(self.image, 50, 15)
        ctx.paint()
    
    """  The function usage Api Cairo for print shape  """
    def draw_with_shapes(self, da, ctx):
        #   param: da => DrawingArea
        #   param: ctx => Context Cairo
        ctx.set_source_rgb(0, 0, 0)
        ctx.rectangle(20, 20, 120, 80)
        ctx.fill()
        
    """ Gtk.Window | Signal: Destroy """
    def on_main_window_destroy(self, *args):
        Gtk.main_quit()
        

if __name__ == "__main__":
    builder.add_from_file(
        os.curdir + os.path.sep + "templates" + os.path.sep + "interface.ui")
    builder.connect_signals(Project())
    Gtk.main()
