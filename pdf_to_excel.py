import pandas as pd
import streamlit as st
from utils import extract_text_from_pdf

def convert_pdf_to_excel(pdf_file):
    """
    Converts a PDF file to an Excel file.

    Parameters:
    pdf_file (UploadedFile): The PDF file uploaded by the user.

    Returns:
    None: Writes the Excel file to the disk.
    """
    # Extract text from PDF
    extracted_text = extract_text_from_pdf(pdf_file)

    # Convert extracted text to DataFrame
    df = pd.DataFrame([extracted_text], columns=['Text'])

    # Save DataFrame to Excel
    excel_file = pdf_file.name.replace('.pdf', '.xlsx')
    df.to_excel(excel_file, index=False)

    # Provide download link to the user
    with open(excel_file, "rb") as f:
        st.download_button(label="Download Excel",
                           data=f,
                           file_name=excel_file,
                           mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
