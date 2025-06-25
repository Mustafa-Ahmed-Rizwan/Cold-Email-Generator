# Cold Email Generator

## Overview

The Cold Email Generator is a Streamlit-based web application designed to assist individuals in crafting personalized cold emails for job applications. By inputting a job posting URL, the tool extracts job details, matches relevant skills from a portfolio, and generates a tailored email to pitch to potential employers.

## Features

- **Job Details Extraction**: Automatically parses job postings to extract roles, skills, experience, and descriptions.
- **Custom Email Generation**: Creates compelling cold emails with a student perspective, highlighting enthusiasm and relevant portfolio projects.
- **Portfolio Integration**: Utilizes a portfolio database to suggest relevant project links based on job skills.
- **User-Friendly Interface**: Features a modern, responsive UI with error handling for multiple job postings.

## Installation

### Prerequisites

- Python 3.8 or higher
- Required Python packages (install via `pip`):
  - `streamlit`
  - `langchain_community`
  - `langchain_groq`
  - `chromadb`
  - `python-dotenv`

### Setup

1. It is recommended to set up a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
2. Clone the repository:

   ```bash
   git clone <repository-url>
   cd cold-email-generator
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Set up your `.env` file with your Groq API key:

   ```
   GROQ_API_KEY=your_api_key_here
   ```
5. Ensure the `sample_portfolio.csv` file is in the project directory.

## Usage

1. Run the application:

   ```bash
   streamlit run main.py
   ```
2. Enter a valid job posting URL in the input field.
3. Click "Submit" to generate a cold email based on the job details.
4. Review the generated email and copy it for use.

## Project Structure

- `main.py`: Main application logic and Streamlit interface.
- `chains.py`: Contains the LLM chain for job extraction and email generation.
- `portfolio.py`: Manages the portfolio database using ChromaDB.
- `utils.py`: Utility functions for text cleaning.
- `ui_styles.py`: Custom CSS styles for the Streamlit UI.
- `sample_portfolio.csv`: Sample portfolio data with skills and project URLs.
- `testing/`: Directory for test files.
- `vectorstore/`, `vectorstore2/`: Directories for vector store data.
- `.gitignore`: Git ignore file.
- `.pypile`, `.pypilelock`: Build and lock files for project management.
- `README.md`: Project documentation.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any enhancements or bug fixes.