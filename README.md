# PDF Text Extractor 📄

A powerful and user-friendly Python utility for extracting text from PDF files. Supports single file processing, batch operations, page range selection, and multiple output formats.

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPDF2](https://img.shields.io/badge/PyPDF2-3.0.0%2B-orange.svg)](https://pypdf2.readthedocs.io/)

## ✨ Features

- 🎯 **Single File Extraction** - Extract text from individual PDF files
- 📦 **Batch Processing** - Process multiple PDFs at once
- 🔄 **Recursive Search** - Scan subdirectories for PDF files
- 📑 **Page Range Selection** - Extract specific page ranges
- 📝 **Multiple Output Formats** - Save as TXT, Markdown, or both
- 📊 **Progress Tracking** - Real-time processing status
- 🏷️ **Metadata Generation** - Automatic metadata headers
- 🎨 **Clean Interface** - Interactive menu-driven CLI
- 🛡️ **Error Handling** - Robust error management and reporting

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Features in Detail](#features-in-detail)
- [Output Formats](#output-formats)
- [Examples](#examples)
- [Requirements](#requirements)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/pdf-text-extractor.git
cd pdf-text-extractor
```

### Step 2: Install Dependencies

```bash
pip install PyPDF2
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

## 🎯 Quick Start

Run the script:

```bash
python pdf_text_extractor.py
```

Follow the interactive menu to:
1. Select extraction mode
2. Choose your PDF file(s)
3. Select output format
4. Get your extracted text!

## 📖 Usage

### Interactive Mode (Recommended)

Simply run the script and follow the prompts:

```bash
python pdf_text_extractor.py
```

### Command-Line Usage

You can also use the PDFTextExtractor class in your own scripts:

```python
from pdf_text_extractor import PDFTextExtractor

# Create extractor instance
extractor = PDFTextExtractor()

# Extract single file
extractor.extract_text_from_pdf('document.pdf', output_format='txt')

# Extract with page range (pages 1-10)
extractor.extract_text_from_pdf('document.pdf', output_format='txt', page_range=(0, 10))

# Batch extract from directory
extractor.batch_extract('/path/to/pdfs', output_format='both', recursive=True)
```

## 🎨 Features in Detail

### 1. Single File Extraction

Extract text from a single PDF file with options for:
- Specific page ranges
- Multiple output formats
- Automatic metadata generation

### 2. Batch Processing

Process multiple PDF files in a directory:
- Non-recursive: Process only PDFs in the specified directory
- Recursive: Include all subdirectories
- Progress tracking for large batches

### 3. Page Range Selection

Extract only the pages you need:
```
Extract specific pages? (y/n): y
Start page (1-indexed): 5
End page (1-indexed): 15
```

### 4. Multiple Output Formats

Choose your preferred format:
- **TXT**: Plain text with page markers
- **MD**: Markdown formatted with headers
- **Both**: Generate both formats simultaneously

## 📄 Output Formats

### Plain Text (.txt)

```
PDF TEXT EXTRACTION METADATA
============================================================
Source File: document.pdf
Extraction Date: 2024-01-15 14:30:00
Total Pages in PDF: 50
Pages Extracted: 1 to 50
============================================================

============================================================
PAGE 1
============================================================

[Page content here...]
```

### Markdown (.md)

```markdown
# document

**Total Pages:** 50  
**Extracted:** 2024-01-15 14:30:00  

---

[Content formatted with markdown...]
```

## 💡 Examples

### Example 1: Extract a Specific Document

```bash
# Run the program
python pdf_text_extractor.py

# Select option 1 (Single file)
# Enter path: /Users/john/Documents/report.pdf
# Select format: 1 (TXT)
# Extract all pages: n
```

### Example 2: Batch Process Research Papers

```bash
# Run the program
python pdf_text_extractor.py

# Select option 4 (Recursive batch)
# Enter directory: /Users/john/Research/Papers
# Select format: 3 (Both TXT and MD)
```

### Example 3: Extract Specific Pages

```bash
# Run the program
python pdf_text_extractor.py

# Select option 1 (Single file)
# Enter path: book.pdf
# Select format: 2 (Markdown)
# Extract specific pages: y
# Start page: 10
# End page: 25
```

### Example 4: Using as a Module

```python
from pdf_text_extractor import PDFTextExtractor

# Initialize
extractor = PDFTextExtractor()

# Extract chapters from a book
extractor.extract_text_from_pdf(
    'my_book.pdf',
    output_format='md',
    page_range=(10, 50)  # Extract pages 11-50
)

# Process all PDFs in a folder
extractor.batch_extract(
    directory='./research_papers',
    output_format='both',
    recursive=True
)

# Check results
print(f"Processed: {extractor.processed_files} files")
print(f"Failed: {extractor.failed_files} files")
```

## 📦 Requirements

Create a `requirements.txt` file:

```
PyPDF2>=3.0.0
```

Install all requirements:

```bash
pip install -r requirements.txt
```

## 🔧 Troubleshooting

### Common Issues

**Issue:** "No module named 'PyPDF2'"
```bash
# Solution: Install PyPDF2
pip install PyPDF2
```

**Issue:** "Permission denied" when saving files
```bash
# Solution: Check file permissions or run with appropriate privileges
chmod 755 pdf_text_extractor.py
```

**Issue:** Extracted text appears garbled
```
# Some PDFs use special encoding or are image-based
# For image-based PDFs, consider using OCR tools like pytesseract
```

**Issue:** "PDF file not found"
```
# Solution: Use absolute paths or check file location
# Example: /home/user/documents/file.pdf
```

### Performance Tips

- For large batches, consider processing in smaller groups
- Use page ranges to extract only needed content
- Image-heavy PDFs may take longer to process

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include error handling for edge cases
- Update README with new features

## 🗺️ Roadmap

Future enhancements planned:

- [ ] OCR support for image-based PDFs
- [ ] GUI interface option
- [ ] Export to additional formats (JSON, CSV)
- [ ] Text analysis features (word count, readability)
- [ ] Cloud storage integration
- [ ] Multi-language support
- [ ] PDF merge before extraction
- [ ] Advanced filtering options

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- [PyPDF2](https://pypdf2.readthedocs.io/) - The PDF manipulation library that makes this possible
- All contributors who help improve this tool

## 📊 Project Stats

- **Language:** Python
- **Dependencies:** PyPDF2
- **License:** MIT
- **Status:** Active Development

---

### 💖 Star this repository if you find it helpful!

### 🐛 Found a bug? [Report it here](https://github.com/yourusername/pdf-text-extractor/issues)

### 💬 Have questions? [Start a discussion](https://github.com/yourusername/pdf-text-extractor/discussions)

---

**Made with ❤️ and Python**
