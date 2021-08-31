# TYPES OF FILES 
FILE_TYPES = {
    "video":"video", 
    "image":"image", 
    "document":"document", 
    "compressed":"compressed", 
    "other":"other", 
    "installer":"installer"
}

# Temperory File types 
TEMPERORY_FILE_TYPES = [
    ".tmp", 
    ".crdownload"
]

# Listing all extensions 
python = ".py"


# Documents 
pdf = ".pdf"
doc = ".doc"
document_extensions = [
    pdf, doc
]

# Images
png = ".png"
svg = ".svg"
jpg = ".jpg"
jpeg = ".jpeg"
JPG = ".JPG"
jfif = ".jfif"
images_extensions = [
    png, svg, jpg,
    jpeg, JPG, jfif 
]

# Video 
mp4 = ".mp4"
mov = ".mov"
wmv = ".wmv"
flv = ".flv"
avi = ".avi"
avchd = ".avchd"
webm = ".webm"
mkv = ".mkv"
video_extensions = [
    mp4, mov, wmv, flv, 
    avi, avchd, webm, mkv
]


# Zip extensions 
zip = ".zip"
sevenZip = ".7z"
iso = ".iso"
tar = ".tar"
gz = ".gz"
compressed_extensions = [
    zip, sevenZip, iso, tar,
    gz
]

# Courses

# Installers 
exe = ".exe"
installer_extensions = [
    ".exe"
]

# Extension mapping 
extensions_mapping = {
    vid_ext:FILE_TYPES["video"] for vid_ext in video_extensions
}

for img in images_extensions:
    extensions_mapping[img] = FILE_TYPES["image"]

for compressed in compressed_extensions:
    extensions_mapping[compressed] = FILE_TYPES["compressed"]

for doc in document_extensions:
    extensions_mapping[doc] = FILE_TYPES["document"]

for executable in installer_extensions:
    extensions_mapping[executable] = FILE_TYPES["installer"]
