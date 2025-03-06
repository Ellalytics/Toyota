import requests
import streamlit as st
from tempfile import NamedTemporaryFile
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import PyPDF2


# Method to generate chunks
def get_text_chunks_langchain(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=1)
    chunks = text_splitter.split_text(text)
    docs = [x for x in chunks]
    return docs

def process_pdf(file_path):
    # PDF processing
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_pages = pdf_reader.pages

        # Create chunks for each shoe detail page
        details = []
        for page_num, page in enumerate(pdf_pages, start=1):
            page_text = page.extract_text()
            # Split the text into lines and remove any empty lines
            lines = [line.strip() for line in page_text.splitlines() if line.strip()]

            # Join lines into a continuous text
            consolidated_text = ' '.join(lines)
            details.append(consolidated_text)

            # PDF reading is done

        # Generate chunks for each shoe detail
        chunks = []
        for detail in details:
            chunks = get_text_chunks_langchain(detail)
            chunks.append(chunks)

        return chunks

def load_file(pdf_file_path):
    with st.spinner('Loading PDF content. Please wait around a minute...'):
        content = process_pdf(pdf_file_path)

    if content:
        with st.container(height=600, border=False):
            col_left, col_right = st.columns(2)
            with col_left:
                image_path = "https://raw.githubusercontent.com/Samuelchazy/Educative.io/19d3100db50749489689a5c21029c3499722b254/images/Toyota_3.jpg"
                st.image(image_path, use_container_width=True)
                image_path = "https://raw.githubusercontent.com/Samuelchazy/Educative.io/19d3100db50749489689a5c21029c3499722b254/images/Toyota_4.jpg"
                st.image(image_path, use_container_width=True)
            with col_right:
                image_path = "https://raw.githubusercontent.com/Samuelchazy/Educative.io/19d3100db50749489689a5c21029c3499722b254/images/Toyota_5.jpg"
                st.image(image_path, use_container_width=True)

                image_path = "https://raw.githubusercontent.com/Samuelchazy/Educative.io/19d3100db50749489689a5c21029c3499722b254/images/Toyota_6.jpg"
                st.image(image_path, use_container_width=True)
        return content
    else:
        st.error('User Manuel not found')
        return None


# ####################### Function for loading and caching the content of the PDF file #######################
# @st.cache_data
# def load_pdf_content(user_manuel_url):
#
#     # Download the PDF from the URL and save it temporarily
#     with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
#         response = requests.get(user_manuel_url)
#         tmp_file.write(response.content)
#         tmp_file_path = tmp_file.name
#
#     # Load the PDF content using PyPDFLoader
#     pdf_loader = PyPDFLoader(tmp_file_path)
#     pdf_reader = pdf_loader.load()
#
#     # Extract and format the content
#     content = [(page.page_content.replace('\n', '\n\n')
#                 if page.page_content else '...') for page in pdf_reader]
#     print(content)
#     return content
#
# ###########################################################################################################
# ########################### Function for displaying the PDF file and the images ###########################
# ###########################################################################################################
# def load_file():
#
#     user_manuel_url = "Toyota-Highlander.pdf"
#     with st.spinner('Loading PDF content. Please wait around a minute...'):
#         content = load_pdf_content(user_manuel_url)
#
#     if content:
#
#         with st.container(height=600, border=False):
#             col_left, col_right = st.columns(2)
#
#             ###################################### Display the images #####################################
#             with col_left:
#                 image_path = "https://raw.githubusercontent.com/Samuelchazy/Educative.io/19d3100db50749489689a5c21029c3499722b254/images/Toyota_3.jpg"
#                 st.image(image_path, use_container_width=True)
#
#                 image_path = "https://raw.githubusercontent.com/Samuelchazy/Educative.io/19d3100db50749489689a5c21029c3499722b254/images/Toyota_4.jpg"
#                 st.image(image_path, use_container_width=True)
#
#             with col_right:
#                 image_path = "https://raw.githubusercontent.com/Samuelchazy/Educative.io/19d3100db50749489689a5c21029c3499722b254/images/Toyota_5.jpg"
#                 st.image(image_path, use_container_width=True)
#
#                 image_path = "https://raw.githubusercontent.com/Samuelchazy/Educative.io/19d3100db50749489689a5c21029c3499722b254/images/Toyota_6.jpg"
#                 st.image(image_path, use_container_width=True)
#
#         return content
#
#     else:
#         st.error('User Manuel not found')
#         return None
