import pdfplumber
import pandas as pd
import streamlit as st

def convert_pdf_to_csv(pdf_file):
    """
    Converts a PDF file to a CSV file using pdfplumber to extract text.

    Parameters:
    pdf_file (UploadedFile): The PDF file uploaded by the user.

    Returns:
    None: Writes the CSV file to the disk.
    """
    # Initialize a list to hold all extracted text
    text_list = []

    # Use pdfplumber to open and read the PDF file
    with pdfplumber.open(pdf_file) as pdf:
        # Extract text from each page
        for page in pdf.pages:
            text = page.extract_text()
            # For simplicity, we're appending the text of each page into a list
            # You might need to process the text into a structured format
            text_list.append(text if text else "Page was blank")
    
    # Convert the list of text into a DataFrame
    df = pd.DataFrame(text_list, columns=['Text'])

    # Save DataFrame to CSV
    csv_file = pdf_file.name.replace('.pdf', '.csv')
    df.to_csv(csv_file, index=False)

    # Provide download link to the user
    with open(csv_file, "rb") as f:
        st.download_button(label="Download CSV",
                           data=f,
                           file_name=csv_file,
                           mime="text/csv")
