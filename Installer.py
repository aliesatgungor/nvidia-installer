import sys
import subprocess

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GLib, Gio

from MainWindow import MainWindow

class Uygulama(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
            application_id="com.aliesatgungor.nvidia-installer",
            flags=Gio.ApplicationFlags.FLAGS_NONE,
            **kwargs)
    
    def do_activate(self):
        self.window = MainWindow(self) 
     


app = Uygulama()
app.run(sys.argv)