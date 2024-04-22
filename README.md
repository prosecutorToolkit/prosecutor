<p align="center">
    <img src="https://raw.githubusercontent.com/prosecutorToolkit/prosecutor/main/logo.jpg?token=GHSAT0AAAAAACQ5O5MTX6WGUBGEH5WPOTSMZRG5WWQ" width="200">
</p>

# About
Prosecutor Toolkit is a comprehensive program designed to assist in prosecution investigations. This software has a wide range of tools that facilitate the analysis of the information collected in the investigations.

The program originated from the need to analyze in a short period of time a large number of files extracted with Cellebrite UFED from the devices seized from a defendant in the "Declarant 1" case, at the Federal Prosecutor's Office No. 1 of La Plata.

Faced with this situation, a code was developed that efficiently traverses directories and collects relevant information using OCR algorithms (Deep folder scan functionality). Search results are presented in formats supported by different applications, such as CSV, XLSX, DOCX, and PDF.

In addition, the IP and URL scanning tool has been added to quickly obtain relevant information for computer investigations and multiple tools to download files and forensically extract its data. The application also has an antivirus function that detects malware and a screen scanner function that allows quick and efficient text extraction, useful for office work.

Prosecutor Toolkit can be of great help in investigations by the prosecutor, the police and the judge, saving valuable time for the investigator and contributing to the success of his task.

______________________
## For Linux devices
*For Windows and MacOS is under development*
______________________
# Tools:
    Deep folder scan 🔎
    Create reports from database 🖨
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
    3. sudo apt install python3.10-venv python3-virtualenv scrot xclip python3-tk tesseract-ocr libtesseract-dev -y
    4. virtualenv prosecutorenv
    5. source prosecutorenv/bin/activate
    6. pip3 install -r requirements.txt
    7. python3 prosecutor.py

## Launch Prosecutor:
    1. cd prosecutor
    2. source prosecutorenv/bin/activate
    3. python3 prosecutor.py


______________________
***Name: Prosecutor Toolkit |   Vertion: 1.0    |   Date and place of creation: 18/06/2022, La Plata - Argentina    |   First commit: 29/04/2023    |   Author: Tobías Rímoli   |   Contact: Tobiasrimoli@protonmail.com***
