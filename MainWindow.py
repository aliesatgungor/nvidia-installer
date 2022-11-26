import gi
import time
import datetime
import subprocess



gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio



class MainWindow:

    def __init__(self, app):

        self.builder = Gtk.Builder()


        self.builder.add_from_file("MainWindow.glade")
        self.builder.connect_signals(self)


        self.window = self.builder.get_object("window")
        self.window.set_application(app)
        

        self.defineComponents()
        

        self.window.show_all()
    
    def defineComponents(self):
        self.output_label = self.builder.get_object("output_label")
    def on_detect_clicked(self,btn):
        command = "lspci | grep VGA"
        process = subprocess.run(command.split(),capture_output=True)   
        output = process.stdout.decode("utf-8") 
        self.output_label.set_label(output)