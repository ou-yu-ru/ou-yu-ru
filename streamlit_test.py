import streamlit as st
from pdf2docx import Converter
from io import BytesIO
from tempfile import NamedTemporaryFile

# Streamlit app
st.title("PDF to Word Converter")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    with NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        temp_pdf_path = temp_pdf.name

    with NamedTemporaryFile(delete=False, suffix=".docx") as temp_docx:
        temp_docx_path = temp_docx.name

    # Convert PDF to Word
    st.write("Converting PDF to Word...")
    converter = Converter(temp_pdf_path)
    converter.convert(temp_docx_path, start=0, end=None)
    converter.close()
    st.write("Conversion complete!")

    # Provide download link
    with open(temp_docx_path, "rb") as f:
        st.download_button(
            label="Download Word file",
            data=f,
            file_name="converted.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )


