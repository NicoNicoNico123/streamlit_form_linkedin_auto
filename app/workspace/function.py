import streamlit as st


# Functions for managing dynamic fields
def add_field_personal():
    if st.session_state.new_field_label:
        st.session_state.dynamic_fields_personal.append({'label': st.session_state.new_field_label})
        st.session_state.new_field_label = ""  # Reset input after adding

def remove_field_by_label_personal():
    label_to_remove = st.session_state.remove_field_label

    # Remove the field from the dynamic fields list
    st.session_state.dynamic_fields_personal = [
        field for field in st.session_state.dynamic_fields_personal
        if field['label'] != label_to_remove
    ]

    # Remove the corresponding entry from session state (the textbox state)
    if f"personal_{label_to_remove}" in st.session_state:
        del st.session_state[f"personal_{label_to_remove}"]

    # Optionally, clear the remove_field_label input itself
    st.session_state.remove_field_label = ""

def add_responsibility():
    next_number = len(st.session_state.responsibilities) + 2  # Start from 2 since 1 is hardcoded
    st.session_state.responsibilities.append(f"Responsibility {next_number}")

def remove_last_responsibility():
    if st.session_state.responsibilities:
        st.session_state.responsibilities.pop()


# Function to add a new skill slider
def add_skill():
    new_skill_label = st.session_state.get('new_skill_label', '')
    if new_skill_label:
        st.session_state.skills_acquired.append({
            'label': new_skill_label,
            'value': 3  # Default value for the slider
        })
        # Clear the input field after adding the skill
        st.session_state.new_skill_label = ''

# Function to remove the last skill slider
def remove_last_skill():
    if st.session_state.skills_acquired:
        st.session_state.skills_acquired.pop()