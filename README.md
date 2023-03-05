File Organizer

This script organizes files in a given directory according to their file type. It creates separate directories for images, videos, audios, documents and archives, and moves files into their respective directories.

Usage

To use the script, pass the path to the directory you want to organize as an argument when running the script in the command line.

For example:


```python file_organizer.py /path/to/directory
Supported File Formats

The script supports the following file formats:

Images
- JPEG
- JPG
- PNG
- SVG

Videos
- AVI
- MP4
- MOV
- MKV

Audios
- MP3
- OGG
- WAV
- AMR

Documents
- DOC
- DOCX
- TXT
- PDF
- XLSX
- PPTX
- CSV

Archives
- ZIP
- GZ
- TAR

Output

The script outputs a list of all files that were moved, as well as a list of known and unknown file formats.
