"""
PDF Text Extractor
==================
A Python utility to extract text from PDF files with support for:
- Single file extraction
- Batch processing
- Page range selection
- Multiple output formats
- Progress tracking
"""

import PyPDF2
import os
import sys
from pathlib import Path
from datetime import datetime


class PDFTextExtractor:
    """Main class for PDF text extraction operations"""
    
    def __init__(self):
        self.processed_files = 0
        self.failed_files = 0
        
    def extract_text_from_pdf(self, pdf_path, output_format='txt', page_range=None):
        """
        Extract text from PDF and save to file
        
        Args:
            pdf_path (str): Path to the PDF file
            output_format (str): Output format ('txt', 'md', or 'both')
            page_range (tuple): Optional (start_page, end_page) tuple
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                total_pages = len(pdf_reader.pages)
                
                # Determine page range
                if page_range:
                    start_page, end_page = page_range
                    start_page = max(0, start_page)
                    end_page = min(total_pages, end_page)
                else:
                    start_page, end_page = 0, total_pages
                
                # Extract text from specified pages
                text = ""
                for page_num in range(start_page, end_page):
                    page = pdf_reader.pages[page_num]
                    page_text = page.extract_text()
                    text += f"\n{'='*60}\n"
                    text += f"PAGE {page_num + 1}\n"
                    text += f"{'='*60}\n\n"
                    text += page_text + "\n"
                
                # Get file information
                directory = os.path.dirname(pdf_path) or '.'
                filename = os.path.splitext(os.path.basename(pdf_path))[0]
                
                # Add metadata
                metadata = self._generate_metadata(pdf_path, total_pages, start_page, end_page)
                full_text = metadata + "\n\n" + text
                
                # Save to file(s)
                saved_files = []
                if output_format in ['txt', 'both']:
                    txt_path = os.path.join(directory, f"{filename}.txt")
                    self._save_file(txt_path, full_text)
                    saved_files.append(txt_path)
                
                if output_format in ['md', 'both']:
                    md_path = os.path.join(directory, f"{filename}.md")
                    md_text = self._format_as_markdown(filename, full_text, total_pages)
                    self._save_file(md_path, md_text)
                    saved_files.append(md_path)
                
                print(f"✓ Text extracted successfully from: {os.path.basename(pdf_path)}")
                print(f"  Pages processed: {start_page + 1} to {end_page}")
                for saved_file in saved_files:
                    print(f"  ✓ Saved to: {saved_file}")
                
                self.processed_files += 1
                return True
                
        except FileNotFoundError:
            print(f"✗ Error: PDF file not found: {pdf_path}")
            self.failed_files += 1
            return False
        except Exception as e:
            print(f"✗ Error processing {pdf_path}: {e}")
            self.failed_files += 1
            return False
    
    def batch_extract(self, directory, output_format='txt', recursive=False):
        """
        Extract text from all PDFs in a directory
        
        Args:
            directory (str): Directory containing PDF files
            output_format (str): Output format ('txt', 'md', or 'both')
            recursive (bool): Search subdirectories if True
        """
        if recursive:
            pdf_files = list(Path(directory).rglob('*.pdf'))
        else:
            pdf_files = list(Path(directory).glob('*.pdf'))
        
        if not pdf_files:
            print(f"No PDF files found in {directory}")
            return
        
        print(f"\nFound {len(pdf_files)} PDF file(s)")
        print("="*60)
        
        for i, pdf_path in enumerate(pdf_files, 1):
            print(f"\n[{i}/{len(pdf_files)}] Processing: {pdf_path.name}")
            self.extract_text_from_pdf(str(pdf_path), output_format)
        
        print("\n" + "="*60)
        print(f"Batch processing complete!")
        print(f"  ✓ Successfully processed: {self.processed_files}")
        if self.failed_files > 0:
            print(f"  ✗ Failed: {self.failed_files}")
    
    def _generate_metadata(self, pdf_path, total_pages, start_page, end_page):
        """Generate metadata header for extracted text"""
        metadata = [
            "PDF TEXT EXTRACTION METADATA",
            "="*60,
            f"Source File: {os.path.basename(pdf_path)}",
            f"Extraction Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Total Pages in PDF: {total_pages}",
            f"Pages Extracted: {start_page + 1} to {end_page}",
            "="*60
        ]
        return "\n".join(metadata)
    
    def _format_as_markdown(self, filename, text, total_pages):
        """Format extracted text as markdown"""
        md_text = f"# {filename}\n\n"
        md_text += f"**Total Pages:** {total_pages}  \n"
        md_text += f"**Extracted:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n\n"
        md_text += "---\n\n"
        md_text += text
        return md_text
    
    def _save_file(self, path, content):
        """Save content to file with UTF-8 encoding"""
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)


def print_banner():
    """Print application banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════╗
    ║          PDF TEXT EXTRACTOR                              ║
    ║          Extract text from PDF files                     ║
    ╚══════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_menu():
    """Print main menu"""
    menu = """
    SELECT MODE:
    1. Extract single PDF file
    2. Batch extract (current directory)
    3. Batch extract (specify directory)
    4. Batch extract (recursive - includes subdirectories)
    5. Exit
    """
    print(menu)


def get_page_range():
    """Prompt user for page range"""
    choice = input("\nExtract specific pages? (y/n): ").strip().lower()
    if choice == 'y':
        try:
            start = int(input("Start page (1-indexed): ")) - 1
            end = int(input("End page (1-indexed): "))
            return (start, end)
        except ValueError:
            print("Invalid input. Extracting all pages.")
            return None
    return None


def get_output_format():
    """Prompt user for output format"""
    print("\nOutput format:")
    print("1. TXT (plain text)")
    print("2. MD (markdown)")
    print("3. Both")
    
    choice = input("Select format (1-3) [default: 1]: ").strip()
    
    formats = {'1': 'txt', '2': 'md', '3': 'both'}
    return formats.get(choice, 'txt')


def main():
    """Main program loop"""
    print_banner()
    extractor = PDFTextExtractor()
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            # Single file extraction
            pdf_path = input("\nEnter the path to your PDF file: ").strip().strip('"').strip("'")
            
            if not os.path.exists(pdf_path):
                print("✗ Error: File not found.")
                continue
            
            if not pdf_path.lower().endswith('.pdf'):
                print("✗ Error: File must be a PDF.")
                continue
            
            output_format = get_output_format()
            page_range = get_page_range()
            
            print("\nProcessing...")
            extractor.extract_text_from_pdf(pdf_path, output_format, page_range)
            
        elif choice == '2':
            # Batch extract current directory
            output_format = get_output_format()
            print("\nProcessing current directory...")
            extractor.batch_extract('.', output_format, recursive=False)
            
        elif choice == '3':
            # Batch extract specified directory
            directory = input("\nEnter directory path: ").strip().strip('"').strip("'")
            
            if not os.path.isdir(directory):
                print("✗ Error: Directory not found.")
                continue
            
            output_format = get_output_format()
            extractor.batch_extract(directory, output_format, recursive=False)
            
        elif choice == '4':
            # Recursive batch extract
            directory = input("\nEnter directory path: ").strip().strip('"').strip("'")
            
            if not os.path.isdir(directory):
                print("✗ Error: Directory not found.")
                continue
            
            output_format = get_output_format()
            print("\nSearching subdirectories...")
            extractor.batch_extract(directory, output_format, recursive=True)
            
        elif choice == '5':
            print("\nThank you for using PDF Text Extractor!")
            sys.exit(0)
            
        else:
            print("✗ Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")
        print("\n" * 2)


if __name__ == "__main__":
    main()
