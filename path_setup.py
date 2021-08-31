# Import requried modules 
import os 
import pathlib

# File Types import 
from extensions import FILE_TYPES


# Default Paths
HOME_PATH = pathlib.Path.home()
DESKTOP_PATH = os.path.join(HOME_PATH, "Desktop")


# Path of Folder to be monitored 
DownloadFolderPath = os.path.join(HOME_PATH, "Downloads")

# Destination Paths 
DesktopDownloadsFolderPath = os.path.join(DESKTOP_PATH, "Downloads")
ImageFolderPath = os.path.join(DesktopDownloadsFolderPath, "Images")
VideosFolderPath = os.path.join(DesktopDownloadsFolderPath, "Videos")
CoursesFolderPath = os.path.join(DesktopDownloadsFolderPath, "Courses")
DocumentsFolderPath = os.path.join(DesktopDownloadsFolderPath, "Documents")
CompressedFolderPath = os.path.join(DesktopDownloadsFolderPath, "Zips")
InstallersFolderPath = os.path.join(DesktopDownloadsFolderPath, "Installers")
OthersFolderPath = os.path.join(DesktopDownloadsFolderPath, "Others")
Folders = [
    DesktopDownloadsFolderPath, 
    ImageFolderPath, 
    VideosFolderPath, 
    CoursesFolderPath, 
    DocumentsFolderPath, 
    CompressedFolderPath,
    InstallersFolderPath, 
    OthersFolderPath
]

# Create and verify the folders 
for folder in Folders:
    folderExists = os.path.exists(folder)
    if not folderExists:
        os.mkdir(folder)

# Log File  
LogFilePath = os.path.join(DesktopDownloadsFolderPath, "logs.txt")
LogFileExists = os.path.exists(LogFilePath)
if not LogFileExists:
    with open(LogFilePath, "w") as fp:
        fp.write('')




folder_mapping = {
    FILE_TYPES["image"]:ImageFolderPath,
    FILE_TYPES["video"]:VideosFolderPath,
    FILE_TYPES["document"]:DocumentsFolderPath,
    FILE_TYPES["compressed"]:CompressedFolderPath,
    FILE_TYPES["installer"]:InstallersFolderPath,
    FILE_TYPES["other"]:OthersFolderPath,
}
