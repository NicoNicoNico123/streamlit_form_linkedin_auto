import streamlit as st
from function import add_field_personal, remove_field_by_label_personal, add_responsibility, remove_last_responsibility, add_skill, remove_last_skill

# Initialize session state for dynamic fields in Personal Information
if 'dynamic_fields_personal' not in st.session_state:
    st.session_state.dynamic_fields_personal = []

# Initialize session state for dynamic fields in Key Responsibilities
if 'responsibilities' not in st.session_state:
    st.session_state.responsibilities = ["Led development of real-time trading algorithm, improving transaction speed by 40%"]

# Initialize session state for dynamic fields in skill sliders
if 'skills_acquired' not in st.session_state:
    st.session_state.skills_acquired = []


# Streamlit tabs
tabs = st.tabs(["Personal Information", "Education Details", "Experience Details"])

# Personal Information Form
with tabs[0]:
    st.header("Personal Information")
 
    # Start of the form
    with st.form(key="personal_information_form"):
        name = st.text_input("Name", "Enter your first name")
        surname = st.text_input("Surname", "Enter your last name")
        date_of_birth = st.text_input("Date of Birth", "Enter your date of birth (DD/MM/YYYY)")
        country = st.text_input("Country", "Enter your country")
        city = st.text_input("City", "Enter your city")
        address = st.text_input("Address", "Enter your address")
        
        # Display dynamic fields for Personal Information
        for i, field in enumerate(st.session_state.dynamic_fields_personal):
            st.text_input(field['label'], field.get('value', ''), key=f"personal_{field['label']}_{i}")
        
        # Form submission button
        submitted = st.form_submit_button("Save Personal Information")
        if submitted:
            st.success("Personal information saved successfully!")

    # Columns for buttons
    cols = st.columns(2)
    with cols[0]:
        st.text_input("Enter label for new field:", key="new_field_label")
        st.button("Add Field", on_click=add_field_personal)
    with cols[1]:
        st.text_input("Enter label of field to remove:", key="remove_field_label")
        st.button("Remove Field", on_click=remove_field_by_label_personal)

# Education Details Form
with tabs[1]:
    st.header("Education Details")
    with st.form(key="education_form"):
        degree = st.text_input("Degree", "Enter your highest degree (e.g., Bachelor's, Master's)")
        university = st.text_input("University", "Enter the name of your university")
        gpa = st.text_input("GPA", "Enter your GPA")
        graduation_year = st.text_input("Graduation Year", "Enter your graduation year")
        field_of_study = st.text_input("Field of Study", "Enter your field of study")
        
        submitted = st.form_submit_button("Save Education Details")
        if submitted:
            st.success("Education details saved successfully!")

# Experience Details Form
with tabs[2]:
    st.header("Experience Details")
    with st.form(key="experience_form"):
        position = st.text_input("Position", "Enter your current or most recent job title")
        company = st.text_input("Company", "Enter the name of your company")
        employment_period = st.text_input("Employment Period", "Enter your employment period (e.g., 2018-2023)")
        location = st.text_input("Location", "Enter the location of your job")
        industry = st.text_input("Industry", "Enter the industry of your job")
        
        st.subheader("Key Responsibilities")
        responsibility1 = st.text_input("Responsibility 1", "Led development of real-time trading algorithm, improving transaction speed by 40%")

        # Display dynamic responsibilities
        for i, responsibility in enumerate(st.session_state.responsibilities):
            st.text_input(f"Responsibility {i+2}", responsibility, key=f"responsibility_{i+2}")
        
        cols = st.columns(2)
        with cols[0]:
            st.form_submit_button("Add Responsibility", on_click=add_responsibility)
        with cols[1]:
            st.form_submit_button("Remove Last Responsibility", on_click=remove_last_responsibility)

        st.subheader("Skills Acquired")

        # Display dynamic Skills Acquired sliders with adjustable labels
        for i, skill in enumerate(st.session_state.skills_acquired):
            skill['value'] = st.slider(skill['label'], 1, 5, skill['value'], key=f"skill_slider_{i}")

        # Input for new skill label
        st.text_input("Enter skill label:", key="new_skill_label")

        cols = st.columns(2)
        with cols[0]:
            st.form_submit_button("Add Skill", on_click=add_skill)
        with cols[1]:
            st.form_submit_button("Remove Last Skill", on_click=remove_last_skill)

        
        submitted = st.form_submit_button("Save Experience Details")
        if submitted:
            st.success("Experience details saved successfully!")
