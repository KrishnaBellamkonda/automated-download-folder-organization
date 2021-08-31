# Imports for system processing & others
import os 
import shutil
import time 

# Import watchdog 
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# Import Extensions
from extensions import extensions_mapping, FILE_TYPES, TEMPERORY_FILE_TYPES

# Import the Paths File 
from path_setup import DesktopDownloadsFolderPath, DownloadFolderPath, LogFilePath, folder_mapping

print("Waiting for a download .....")

# Moving Files from the required folder 
class Handler(FileSystemEventHandler):

    def on_modified(self, event):
        try:
            src_path = event.src_path
            filedir, filename = os.path.split(src_path)
            _, extension = os.path.splitext(src_path)

            print("Extension: ", extension)

            if extension in list(TEMPERORY_FILE_TYPES): 
                print("Extension is None")
                return None

            # Matching the destination path 
            extension_type = extensions_mapping.get(extension)
            if extension_type is None: 
                destination_folder = folder_mapping["other"]
            else:
                destination_folder = folder_mapping[extension_type] 
            
            
            destination_path = os.path.join(destination_folder, filename)
            if os.path.exists(destination_path):
                timestamp = int(time.time())
                destination_path = os.path.join(destination_folder, _+"_"+str(timestamp))

            print(str(destination_path))

            # Moving the file to another folder
            time.sleep(2)
            shutil.move(src_path, destination_path) 

            # Logging 
            log_string = f"{filename} moved from {filedir} to {destination_path} \n"
            with open(LogFilePath, "r") as fp:
                log_data = fp.readlines()
            
            log_data.append(log_string) # Adding the log string
            with open(LogFilePath, "w") as fp:
                fp.writelines(log_data)
            print(log_string)

            return super().on_created(event)

        except FileNotFoundError:
            time.sleep(2)
            print("The file maybe downloading or has been moved")

event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, path=DownloadFolderPath, recursive=True)
observer.start()

try: 
    while True:
        time.sleep(1000)
except KeyboardInterrupt: # Press Ctrl + C to quit the program
    observer.stop()
observer.join()