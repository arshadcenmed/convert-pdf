import streamlit as st
from utils import extract_text_from_pdf

def convert_pdf_to_txt(pdf_file):
    """
    Converts a PDF file to a TXT file.

    Parameters:
    pdf_file (UploadedFile): The PDF file uploaded by the user.

    Returns:
    None: Writes the TXT file to the disk.
    """
    # Extract text from PDF
    extracted_text = extract_text_from_pdf(pdf_file)

    # Save text to TXT file
    txt_file = pdf_file.name.replace('.pdf', '.txt')
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(extracted_text)

    # Provide download link to the user
    with open(txt_file, "rb") as f:
        st.download_button(label="Download TXT",
                           data=f,
                           file_name=txt_file,
                           mime="text/plain")
