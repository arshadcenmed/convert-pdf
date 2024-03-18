import fitz  # PyMuPDF
import pandas as pd
import streamlit as st

def convert_pdf_to_excel(pdf_file):
    """
    Converts a PDF file to an Excel file using PyMuPDF to extract text.

    Parameters:
    pdf_file (UploadedFile): The PDF file uploaded by the user.

    Returns:
    None: Writes the Excel file to the disk.
    """
    # Open the PDF file
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    
    # Initialize a list to hold all extracted text
    text_list = []

    # Extract text from each page
    for page in doc:
        text = page.get_text()
        # Here you might need to process the text into a structured format
        # For simplicity, we're just appending the text of each page into a list
        text_list.append(text)
    
    # Close the document
    doc.close()

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
