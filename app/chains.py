from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
import os

load_dotenv()


class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0.3,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.3-70b-versatile"
        )

    def extract_jobs(self, cleaned_text):
        """Extract job roles and skills from JD"""
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM JOB POSTING:
            {job_description}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Extract the job postings and return them in JSON format containing the
            following keys: `role`, `experience`, `skills`, `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"job_description": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links, tone="Professional"):
        """Generate cold email based on job and portfolio links"""
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Akshay Prabhe, a 4th Year AIDS Engineering Student.
            Write a {tone} cold email to the hiring manager regarding the job described above.

            Mention that you have experience with: {skills}
            Also include 2-3 most relevant portfolio links from this list: {link_list}

            Keep it under 150 words. Be confident but not arrogant.
            Start with a subject line.
            End with "Best regards, Akshay Prabhe"

            ### EMAIL (NO PREAMBLE):
            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({
            "job_description": str(job),
            "link_list": ", ".join(links),
            "skills": ", ".join(job.get('skills', [])),
            "tone": tone
        })
        return res.content