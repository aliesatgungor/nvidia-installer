import gi
import time
import datetime
import subprocess



gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio



class MainWindow:

    def __init__(self, app):

        self.builder = Gtk.Builder()


        self.builder.add_from_file("ui/MainWindow.glade")
        self.builder.connect_signals(self)


        self.window = self.builder.get_object("window")
        self.window.set_application(app)
        

        self.defineComponents()
        

        self.window.show_all()
    
    def defineComponents(self):
        self.output_label = self.builder.get_object("output_label")
    def on_detect_clicked(self,btn):
        komut = "pkexec apt update"
        process = subprocess.run(komut.split(),capture_output= True)
        output = process.stdout.decode("utf-8") 
        self.output_label.set_label(output)   
        
        komut = "pkexec apt install nvidia-detect"
        process = subprocess.run(komut.split(),capture_output= True)
        output = process.stdout.decode("utf-8") 
        self.output_label.set_label(output)  
        
        komut = "nvidia-detect"
        process = subprocess.run(komut.split(),capture_output= True)
        output = process.stdout.decode("utf-8") 
        worker = output.split()
        worker = worker[-2]
        time.sleep(2)
        self.output_label.set_label(output) 
        print("pkexec apt install {}".format(worker))
        komut = "pkexec apt install {}".format(worker)
        process = subprocess.run(komut.split(),capture_output= True)
        output = process.stdout.decode("utf-8") 
        self.output_label.set_label(output)      