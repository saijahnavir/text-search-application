
# Text-search-application

This project implements keyword search algorithms (Knuth-Morris-Pratt, Boyer-Moore, and Rabin-Karp) for searching keywords in large documents. It provides a web interface built with Flask that allows users to upload documents and search for specified keywords.

## Features

- Upload `.txt`, `.pdf`, or `.docx` files.
- Search for keywords in the uploaded document.
- Compare the performance of different search algorithms:
  - Knuth-Morris-Pratt (KMP)
  - Boyer-Moore
  - Rabin-Karp
- Display algorithm performance (execution time and memory usage).
- Display a preview of matched lines from the document.
- Highlights keywords in the preview lines.

## Installation

### Requirements
- Python 3.x
- Flask
- Required libraries for reading PDF and DOCX files:
  - `PyPDF2` (for PDF extraction)
  - `python-docx` (for DOCX extraction)
  
### Steps to run the project locally

1. Clone the repository:
   ```bash
   git clone https://github.com/saijahnavir/text-search-application.git
   cd text-search-application
   ```
2. Set up a virtual environment:
    ```bash
    python -m venv venv
    ```
3. Activate the virtual environment : 
 - On windows : 
```bash 
venv\Scripts\activate
```
- On Mac : 
```bash 
source venv/bin/activate
```
4. Install the required dependencies:
```bash 
pip install -r requirements.txt
```
5. Make sure the following files are included in the `requirements.txt`:
```txt
Flask
PyMuPDF
python-docx
```
6. Set up the necessary uploads folder:
```bash 
mkdir uploads
```
7. Run the flask application: 
```bash 
python app.py
```
8. Open your browser and go to http://127.0.0.1:5000/ to access the web interface.
