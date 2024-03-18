import streamlit as st
from pdf_to_csv import convert_pdf_to_csv
from pdf_to_txt import convert_pdf_to_txt
from pdf_to_excel import convert_pdf_to_excel

def main():
    st.title("PDF Converter App")
    
    # Upload PDF
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        # Options for conversion
        convert_option = st.selectbox("Convert to:", ["CSV", "TXT", "Excel"])
        
        # Convert button
        if st.button("Convert"):
            if convert_option == "CSV":
                try:
                    convert_pdf_to_csv(uploaded_file)
                    st.success("Converted to CSV successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            
            elif convert_option == "TXT":
                try:
                    convert_pdf_to_txt(uploaded_file)
                    st.success("Converted to TXT successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            
            elif convert_option == "Excel":
                try:
                    convert_pdf_to_excel(uploaded_file)
                    st.success("Converted to Excel successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
