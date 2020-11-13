import os, sys
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Creating the myHandler class that contains a function to watch the folder and move new files to the destination folders defined below
class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if filename.endswith('.pdf'):
                src = folder_to_track + "/" + filename
                new_pdf_destination = pdf_destination + "/" + filename
                os.rename(src, new_pdf_destination)
            elif filename.endswith('.deb'):
                src = folder_to_track + "/" + filename
                new_deb_destination = deb_destination + "/" + filename
                os.rename(src, new_deb_destination)
            elif filename.endswith(('.jpg', '.png', '.jpeg', '.tiff', '.gif')):
                src = folder_to_track + "/" + filename
                new_image_destination = Image_destination + "/" + filename
                os.rename(src, new_image_destination)
            elif filename.endswith(('.doc', '.docx', 'docm', 'dotx', 'dotm', 'docb', '.txt', '.odt', '.rtf', '.wks', '.wpd', '.wps', '.tex', '.csv', '.dif')):
                src = folder_to_track + "/" + filename
                new_text_destination = Text_destination + "/" + filename
                os.rename(src, new_text_destination)
            elif filename.endswith(('.xls', '.xlt', '.xml', '.xlsx', '.xlsb', '.xltx', '.xltm', '.xlam', '.xla', '.xlw', '.xlr')):
                src = folder_to_track + "/" + filename
                new_spreadsheet_destination = Spreadsheet_destination + "/" + filename
                os.rename(src, new_spreadsheet_destination)
            else:
                src = folder_to_track + "/" + filename
                new_random_destination = Random_destination + "/" + filename
                os.rename(src, new_random_destination)

            
# Defining the folder destinations
folder_to_track = "/home/greg/Downloads"
pdf_destination = "/home/greg/Documents/PDF_Files"
deb_destination = "/home/greg/Documents/Deb_Files"
Image_destination = "/home/greg/Documents/Image_Files"
Text_destination = "/home/greg/Documents/Text_Files"
Spreadsheet_destination = "/home/greg/Documents/Spreadsheet_Files"
Random_destination = "/home/greg/Documents/Random_Files"

# Initializing the handler class
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()