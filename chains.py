import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
load_dotenv()

# Optional: Check if the key is loaded
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY not found in environment variables. Please check your .env file.")

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
                        model="llama-3.3-70b-versatile",
                        temperature=0,
                        max_tokens=None,
                        timeout=None,
                        max_retries=2)
    
    
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template("""
                I will give you scraped text from the job posting. 
                Your job is to extract the job details & requirements in a JSON format containing the following keys: 'role', 'experience', 'skills', and 'description'. 
                Only return valid JSON. No preamble, please.
                Here is the scraped text: {page_data}
                """)    
        
        chain_extract = prompt_extract | self.llm
        response = chain_extract.invoke(input={"page_data" : cleaned_text})
        
        try:
            json_parser = JsonOutputParser()
            response = json_parser.parse(response.content)
        except OutputParserException:
            raise OutputParserException("Content too big, unable to parse jobs.")
        
        return response if isinstance(response, list) else [response]


    def write_email(self, job_description, portfolio_urls):
        prompt_email = PromptTemplate.from_template(
                """
                Your Role: Your name is Mustafa, a motivated student at FAST NUCES Karachi with a strong passion for technology and hands-on experience in IT projects. You are eager to apply your skills and contribute to innovative solutions in the industry.

Your Job: Write a compelling cold email to potential employers regarding job openings they have advertised. Craft an engaging email hook to spark interest and initiate a conversation about a potential internship or entry-level opportunity. Highlight your relevant skills and include the most pertinent portfolio URLs (provided below) to demonstrate your capabilities and enthusiasm to learn and grow.

I will now provide you with the Job description and the portfolio URLs: JOB DESCRIPTION: {job_description}

PORTFOLIO URLS: {portfolio_urls}
                """)
        
        chain_email = prompt_email | self.llm
        response = chain_email.invoke({"job_description": str(job_description), "portfolio_urls": portfolio_urls})

        return response.content
        