import pandas as pd
import streamlit as st
from tabula import read_pdf

def convert_pdf_to_excel(pdf_file):
    """
    Converts a PDF file to an Excel file using tabula to extract tables.

    Parameters:
    pdf_file (UploadedFile): The PDF file uploaded by the user.

    Returns:
    None: Writes the Excel file to the disk.
    """
    # Use tabula to read tables from PDF
    df_list = read_pdf(pdf_file, pages='all', multiple_tables=True, lattice=True, stream=True)

    # Assuming you want to concatenate all tables found into a single DataFrame
    df = pd.concat(df_list, ignore_index=True)

    # Save DataFrame to Excel
    excel_file = pdf_file.name.replace('.pdf', '.xlsx')
    df.to_excel(excel_file, index=False)

    # Provide download link to the user
    with open(excel_file, "rb") as f:
        st.download_button(label="Download Excel",
                           data=f,
                           file_name=excel_file,
                           mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
