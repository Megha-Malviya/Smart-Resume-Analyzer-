import streamlit as st
from resume_analyzer import extract_text_from_pdf, extract_skills, load_job_roles, match_skills_to_jobs, suggest_missing_skills

# Load job roles database
job_roles_df = load_job_roles('job_roles.csv')

st.title("Smart Resume Analyzer and Job Matcher")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

if uploaded_file is not None:
    # Use the BytesIO to handle the uploaded PDF file
    resume_text = extract_text_from_pdf(uploaded_file.read())

    # Extract skills from the resume
    extracted_skills = extract_skills(resume_text)
    # Match skills to job roles
    matched_jobs = match_skills_to_jobs(extracted_skills, job_roles_df)
    st.subheader("Matched Job Roles:")
    if matched_jobs:
        for job, skills in matched_jobs:
            st.write(f"- {job} (Skills: {', '.join(skills)})")
        # Suggest missing skills
        missing_skills = suggest_missing_skills(extracted_skills, matched_jobs)
        if missing_skills:
            st.subheader("Suggested Skills to Learn:")
            for job, skills in missing_skills.items():
                st.write(f"For {job}, consider learning: {', '.join(skills)}")
    else:
        st.write("No matching job roles found.")
