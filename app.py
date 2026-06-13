
        import streamlit as st

        st.set_page_config(page_title="AI Resume Builder", layout="wide")
        st.title("AI Resume & Portfolio Builder")

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
            education = st.text_area("Education")
            skills = st.text_area("Skills (comma separated)")

        with col2:
            projects = st.text_area("Projects")
            experience = st.text_area("Experience")
            achievements = st.text_area("Achievements")
            objective = st.text_area("Career Objective")

        if st.button("Generate Resume"):
            resume = f'''
# {name}

## Career Objective
{objective}

## Education
{education}

## Skills
{skills}

## Experience
{experience}

## Projects
{projects}

## Achievements
{achievements}

Contact: {email} | {phone}
'''
            st.markdown(resume)
            st.download_button("Download Resume", resume, "resume.md")

        st.sidebar.header("Portfolio Tips")
        st.sidebar.write("Add GitHub, LinkedIn and project links.")
