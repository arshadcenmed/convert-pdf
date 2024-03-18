import fitz  # PyMuPDF
import pandas as pd
import streamlit as st

def convert_pdf_to_csv(pdf_file):
    """
    Converts a PDF file to a CSV file using PyMuPDF to extract text.

    Parameters:
    pdf_file (UploadedFile): The PDF file uploaded by the user.

    Returns:
    None: Writes the CSV file to the disk.
    """
    # Open the PDF file
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    
    # Initialize a text placeholder
    all_text = []

    # Extract text from each page of the PDF
    for page in doc:
        text = page.get_text()
        all_text.append(text)
    
    # Close the document
    doc.close()

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
