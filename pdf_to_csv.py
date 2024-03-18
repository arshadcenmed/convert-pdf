import PyPDF2
import pandas as pd
import io
from utils import extract_text_from_pdf
import streamlit as st

def convert_pdf_to_csv(pdf_file):
    """
    Converts a PDF file to a CSV file.

    Parameters:
    pdf_file (UploadedFile): The PDF file uploaded by the user.

    Returns:
    None: Writes the CSV file to the disk.
    """
    # Initialize a text placeholder
    all_text = []

    # Extract text from PDF
    extracted_text = extract_text_from_pdf(pdf_file)
    all_text.append(extracted_text)

    # Convert list of text to DataFrame
    df = pd.DataFrame(all_text, columns=['Text'])

    # Save DataFrame to CSV
    csv_file = pdf_file.name.replace('.pdf', '.csv')
    df.to_csv(csv_file, index=False)

    # Provide download link to the user
    with open(csv_file, "rb") as f:
        st.download_button(label="Download CSV",
                           data=f,
                           file_name=csv_file,
                           mime="text/csv")

