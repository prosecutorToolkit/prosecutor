<p align="center">
    <img src="https://raw.githubusercontent.com/prosecutorToolkit/prosecutor/main/logo.jpg" width="200">
</p>

# About
Prosecutor Toolkit is a comprehensive program designed to assist in prosecution investigations. This software has a wide range of tools that facilitate the analysis of the information collected in the investigations.

The program originated from the need to analyze in a short period of time a large number of files extracted from the devices seized from a defendant in the framework of the "Declarant 1" case at the Federal Prosecutor's Office No. 1 of La Plata.

Faced with this situation, a code was developed that efficiently traverses directories and collects relevant information using OCR algorithms. Search results are presented in formats supported by different applications, such as CSV, XLSX, DOCX, and PDF.

The Prosecutor Toolkit is also useful for analyzing extractions from Cellebrite UFED devices.

In addition, the IP and URL scanning tool has been added to quickly obtain relevant information for computer investigations and multiple tools to download files and forensically extract its data. The application also has an antivirus function that detects malware and a screen scanner function that allows quick and efficient text extraction, useful for office work.

The Prosecutor Toolkit is a program designed for use on Linux operating systems and can be of great help in investigations by the Prosecutor's Office, saving valuable time for the investigator and contributing to the success of his task.

______________________
## For Linux devices
*For Windows is in development*
______________________
# Tools:
    Deep folder scan 🔎
    Get text of file Ⓐ
    Get text of screen 🖥
    Get hash of file/folder #
    Get metadata of file ␐
    Compress file/folder 🗜
    Get IP/URL data 💻
    Search malware in IP/URL 🦠
    Search malware in file 🦠
    Search executables in file 🦠
    Process and map impacts of phones in cells 📱
    Download forensically a YouTube Video ▷

______________________
# How to start:

## First time:
    1. git clone https://github.com/prosecutorToolkit/prosecutor.git
    2. cd prosecutor
    3. virtualenv prosecutorenv
    4. source prosecutorenv/bin/activate
    5. pip3 install -r requirements.txt
    6. sudo apt-get install python3-tk
    7. python3 prosecutor.py

## Launch Prosecutor:
    1. cd prosecutor
    2. source prosecutorenv/bin/activate
    3. python3 prosecutor.py

______________________
***Name: Prosecutor Toolkit |   Vertion: 1.0    |   Date and place of creation: 18/06/2022, La Plata - Argentina    |   First commit: 29/04/2023    |   Author: Tobías Rímoli   |   Contact: Tobiasrimoli@protonmail.com***