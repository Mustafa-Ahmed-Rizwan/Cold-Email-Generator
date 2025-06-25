import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.exceptions import OutputParserException  # Added import for specific exception
from chains import Chain
from portfolio import Portfolio
from utils import clean_text
import ui_styles  # Import UI styles from separate file

def create_streamlit_app(llm, portfolio, clean_text):
    st.title("Cold Email Generator")
    st.markdown("Enter a job posting URL to generate a tailored cold email.")

    # Improved input section with button alignment
    input_col, button_col = st.columns([8, 1])
    with input_col:
        url_input = st.text_input("Enter a URL: ", key="url_input")
    with button_col:
        st.write("")  # Adds vertical space to align button with input
        submit_button = st.button("Submit", key="submit_button")

    if submit_button and url_input:
        with st.spinner("Processing..."):
            try:
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)
                portfolio.load_portfolio()
                jobs = llm.extract_jobs(data)
                
                for job in jobs:
                    skills = job.get("skills", [])
                    portfolio_urls = portfolio.query_links(skills)
                    email = llm.write_email(job, portfolio_urls)
                    st.code(email, language="markdown")
                    st.success("Email generated successfully!")
            except OutputParserException as e:
                st.error("Please provide a link to a single job posting. Multiple jobs detected.")
            except Exception as e:
                st.error(f"An Error Occurred: {e}")

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Cold Email Generator")
    chain = Chain()
    portfolio = Portfolio(file_path="./sample_portfolio.csv")
    create_streamlit_app(chain, portfolio, clean_text)