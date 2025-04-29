import pandas as pd
import spacy


nlp = spacy.load("en_core_web_sm")


import fitz  # pymupdf

def extract_text_from_pdf(file_bytes):
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

def extract_skills(resume_text, skills_list):
    extracted_skills = []
    for skill in skills_list:
        if skill.lower() in resume_text.lower():
            extracted_skills.append(skill)
    return extracted_skills

def load_job_roles(file_path):
    return pd.read_csv(file_path)

def match_skills_to_jobs(extracted_skills, job_roles_df):
    matched_jobs = []
    for index, row in job_roles_df.iterrows():
        job_skills = set(row['Skills'].split(', '))
        if job_skills.intersection(extracted_skills):
            matched_jobs.append((row['Job Role'], job_skills))
    return matched_jobs

def suggest_missing_skills(extracted_skills, matched_jobs):
    missing_skills = {}
    for job, skills in matched_jobs:
        missing = skills - extracted_skills
        if missing:
            missing_skills[job] = missing
    return missing_skills