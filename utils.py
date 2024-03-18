import PyPDF2

def extract_text_from_pdf(pdf_file):
    """
    Extracts all text from a PDF file.

    Parameters:
    pdf_file (UploadedFile): The PDF file uploaded by the user.

    Returns:
    str: All text extracted from the PDF file.
    """
    # Initialize a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Initialize a text placeholder
    all_text = ""
    
    # Iterate through each page in the PDF
    for page in pdf_reader.pages:
        # Extract text from page
        all_text += page.extract_text() + "\n"  # Add a newline character after each page's text
    
    return all_text
