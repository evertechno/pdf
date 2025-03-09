import PyPDF2
import streamlit as st
from io import BytesIO

# Function to merge PDFs
def merge_pdfs(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    output_pdf = BytesIO()
    merger.write(output_pdf)
    output_pdf.seek(0)
    return output_pdf

# Streamlit app
def app():
    st.title("PDF Merger Tool")
    
    st.markdown("Upload multiple PDF files to merge them into one.")
    
    uploaded_files = st.file_uploader("Choose PDF files", type=["pdf"], accept_multiple_files=True)

    if uploaded_files:
        st.write(f"Number of PDFs selected: {len(uploaded_files)}")
        
        # Display each file name
        for file in uploaded_files:
            st.write(file.name)

        # Button to merge PDFs
        if st.button("Merge PDFs"):
            # Call the merge function
            merged_pdf = merge_pdfs(uploaded_files)

            # Allow the user to download the merged PDF
            st.download_button(
                label="Download Merged PDF",
                data=merged_pdf,
                file_name="merged_output.pdf",
                mime="application/pdf"
            )

if __name__ == "__main__":
    app()
