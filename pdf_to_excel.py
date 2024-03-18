import pdfplumber
import pandas as pd
import streamlit as st

def convert_pdf_to_excel(pdf_file):
    """
    Converts a PDF file to an Excel file using pdfplumber to extract text.

    Parameters:
    pdf_file (UploadedFile): The PDF file uploaded by the user.

    Returns:
    None: Writes the Excel file to the disk.
    """
    # Initialize a list to hold all extracted text
    text_list = []

    # Use pdfplumber to open and read the PDF file
    with pdfplumber.open(pdf_file) as pdf:
        # Extract text from each page
        for page in pdf.pages:
            text = page.extract_text()
            # For simplicity, we're just appending the text of each page into a list
            # You might need to process the text into a structured format
            text_list.append(text if text else "Page was blank")
    
    # Convert the list of text into a DataFrame
    # This example assumes each item in the list is a row for simplicity
    # You might need to further process the text to fit your specific needs
    df = pd.DataFrame(text_list, columns=["ExtractedText"])

    # Save DataFrame to Excel
    excel_file = "output.xlsx"
    df.to_excel(excel_file, index=False)

    # Provide download link to the user
    with open(excel_file, "rb") as f:
        st.download_button(label="Download Excel",
                           data=f,
                           file_name=excel_file,
                           mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
