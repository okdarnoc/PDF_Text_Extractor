# Contributing to PDF Text Extractor

First off, thank you for considering contributing to PDF Text Extractor! It's people like you that make this tool better for everyone.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct:
- Be respectful and inclusive
- Welcome newcomers and encourage diverse perspectives
- Focus on what is best for the community
- Show empathy towards other community members

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (sample PDFs if possible)
- **Describe the behavior you observed and what you expected**
- **Include screenshots** if relevant
- **Specify your environment** (OS, Python version, PyPDF2 version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the proposed feature
- **Explain why this enhancement would be useful**
- **List any similar features** in other tools
- **Provide examples** of how it would work

### Pull Requests

1. **Fork the repo** and create your branch from `main`
2. **Follow the coding style** (PEP 8 for Python)
3. **Add tests** if you're adding functionality
4. **Update documentation** as needed
5. **Write clear commit messages**
6. **Submit your pull request**

## Development Setup

1. Clone your fork:
```bash
git clone https://github.com/yourusername/pdf-text-extractor.git
cd pdf-text-extractor
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use docstrings for all functions and classes

### Documentation

- Update README.md if you change functionality
- Add docstrings to new functions:
```python
def new_function(param1, param2):
    """
    Brief description of what the function does.
    
    Args:
        param1 (type): Description of param1
        param2 (type): Description of param2
        
    Returns:
        type: Description of return value
    """
    pass
```

### Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests after the first line

Examples:
```
Add batch processing feature

- Implement recursive directory scanning
- Add progress tracking
- Update documentation
Fixes #123
```

## Testing

Before submitting a pull request:

1. Test your changes with various PDF files
2. Verify that existing functionality still works
3. Test edge cases (empty PDFs, large files, corrupted files)
4. Run the script with different options

## Areas for Contribution

Here are some areas where contributions would be especially welcome:

### High Priority
- OCR support for scanned PDFs
- Performance optimization for large files
- Better error messages
- Unit tests

### Medium Priority
- GUI interface
- Additional output formats (JSON, CSV)
- Text analysis features
- Cloud storage integration

### Documentation
- Tutorial videos
- More usage examples
- Troubleshooting guide
- API documentation

## Questions?

Feel free to open an issue with your question, or reach out to the maintainers directly.

## Recognition

Contributors will be recognized in the README.md file. Thank you for your contributions!

---

**Happy Coding! 🎉**
