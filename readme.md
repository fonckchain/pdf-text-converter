<p align="center">
  <img width="180" src="./public/python-logo.png" alt="Python">
  <h1 align="center">PDF to Text Conversion</h1>
  <p align="center">This project contains a Python script that converts PDF files to text files</p>
</p>

## Description

The script scans specified directories for PDF files. For each PDF file, it extracts the text content and saves it as a new text file in a specified output directory.

## Getting Started

### Dependencies

- Python 3.7 or higher
- pdfminer.six

### Installing

1. Clone the repository to your local machine.
2. Install the required Python package: `pip install pdfminer.six`

### Using the Script

1. Open the Python script (`pdf_to_text.py`) in a text editor.
2. Modify the `directories` list with the paths to the directories containing your PDF files.
3. Modify the `output_dir` variable with the path to the directory where you want to save the text files.
4. Run the script: `python pdf_to_text.py`

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
