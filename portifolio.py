import streamlit as st
import time

# Set page configuration at the very top
st.set_page_config(page_title="My Digital Footprint – Showcasing My Journey", page_icon="📌", layout="wide")

# Apply custom styling
st.markdown("""
    <style>
        .main {background-color: #f5f7fa;}
        .stSidebar {background-color: #2E4053; color: white;}
        .stTitle {color: #1F618D;}
        .stSubheader {color: #283747;}
        .stButton > button {background-color: #1F618D; color: white; border-radius: 10px;}
        .stProgress {background-color: #D5D8DC;}
        .stExpander {transition: all 0.3s ease-in-out;}
        
        /* Fade-in effect */
        .fade-in {opacity: 0; transition: opacity 1s ease-in-out;}
        .fade-in.visible {opacity: 1;}
        
        /* Hover effect for project cards */
        .hover-effect:hover {transform: scale(1.05); transition: 0.3s;}
        
        /* Scroll animations */
        .scroll-animate {opacity: 0; transform: translateY(50px); transition: opacity 0.6s ease-out, transform 0.6s ease-out;}
        .scroll-animate.visible {opacity: 1; transform: translateY(0);}
    </style>
""", unsafe_allow_html=True)

# Streamlit app title
st.title("🎓 Welcome to the Student Portfolio App")
st.write("Explore student achievements and projects.")

# Sidebar navigation
st.sidebar.title("📌 Navigation")
st.sidebar.markdown("---")
page = st.sidebar.radio("Go To:", ["Home", "Projects", "Skills", "Settings", "Contact", "Testimonials"])

# Initialize session state variables if they don't exist
if 'name' not in st.session_state:
    st.session_state.name = "Denyse NYIRATUZA"
if 'location' not in st.session_state:
    st.session_state.location = "Musanze-Rwanda" 
if 'bio' not in st.session_state:
    st.session_state.bio = "I am a passionate AI engineer!"

# Home section
if page == "Home":
    st.title("🧑‍🎓 Student Profile")
    st.image("little.jpg", width=150, caption="Default image")
 
    # Display profile details
    st.subheader("📌 Personal Details")
    st.markdown(f"📍 Location:** {st.session_state.location}")
    
    # About Me (Short introduction)
    st.subheader("🔹 About Me")
    st.write(st.session_state.bio)

    # If "Customize Profile" is clicked, allow editing
    if st.session_state.get('editing_profile', False):
        st.session_state.name = st.text_input("Name:", st.session_state.name)
        st.session_state.location = st.text_input("Location:", st.session_state.location)
        st.session_state.bio = st.text_area("Short introduction about myself:", st.session_state.bio)

        # Save and update profile
        if st.button("Save Profile Changes"):
            st.success("✅ Profile updated successfully!")
    
    # Show 'Customize Profile' button
    if st.button("Customize Profile"):
        st.session_state.editing_profile = True
    else:
        st.session_state.editing_profile = False

    # Resume download button
    with open("resume.pdf", "rb") as file:
        resume_bytes = file.read()
    st.download_button(label="📄 Download Resume", data=resume_bytes, file_name="resume.pdf", mime="application/pdf")
    
    st.markdown("---")


# Projects section
elif page == "Projects":
    st.title("💻 My Projects")
    
    # Project Filtering System
    category = st.selectbox("Filter projects by category:", ["All", "Year 1 Project", "Group Projects", "Dissertation"])
    
    project_data = {
        "Year 1 Project": {
            "📊 Data Analysis Project": {
                "type": "Individual",
                "description": ".",
               
            }
        },
        "Year 2 Project": {
            "🤖 AI Chatbot": {
                "type": "Group",
                "description": "Together with my  collegues we developed a site where you can view our profile & what we have developed together.",
                "link": "https://github.com/tuza421/YEAR-II-C"
            }
        },
        "Year 3 Project": {
            "🌐  Ines Website": {
                "type": "Group",
                "description": "Designed and developed a website for ASA Ines RUHENGERI Adventist Church.",
                "link": "https://github.com/tuza421/ines-website"
            }
        },
        "Dissertation": {
            "Developing e-health Platform to enhance healthcare literacy, providing rural communities with essential knowledge on prevention, treatment and wellness": {
                "type": "Individual",
                "description": "Designed and developed healthcare literacy platform.",
                "link": "https://github.com/tuza421/healthcare-literacy-platform"
            }
        }
    }
    
    # Display the projects based on the category filter
    if category == "All":
        filtered_projects = {k: v for cat in project_data.values() for k, v in cat.items()}
    else:
        filtered_projects = project_data.get(category, {})
    
    for project, details in filtered_projects.items():
        with st.expander(project, expanded=False):
            time.sleep(0.1)  # Smooth transition
            st.write(f"Type: {details['type']}")
            st.write(f"Description: {details['description']}")
            if details.get("link"):
                st.markdown(f"[Link to Code]({details['link']})")
    
    st.markdown("---")
    
    # Student Testimonials
    st.subheader("🗣 Student Testimonials")
    testimonials = [
        "Denyse is a brilliant problem solver! Her final year project was truly innovative. – Mr. Clement",
        "Denyse's dedication to AI is inspiring. She never stops learning! – Lecturer. SHIMIRWA Aline Valerie",
        "A great team mentor and developer. Denyse delivers high-quality projects. – Teammate M.Judy"
    ]
    for testimonial in testimonials:
        st.write(f"🗨 {testimonial}")
    
    st.markdown("---")
    
    # Timeline of Academic & Project Milestones
    st.subheader("⏳ Timeline of Academic & Project Milestones")
    milestones = [
        "✅ Year 2023: Web Design project completed",
        "🏆 Year 2024: Hackathon participation in Kigali",
        "💼 08/07/2025: IBM Learning",
        "📖 Year 2025: Dissertation submission"
    ]
    for milestone in milestones:
        st.write(f"- {milestone}")

# Skills section
elif page == "Skills":
    st.title("⚡ Skills and Achievements")
    
    st.subheader("Programming Skills")
    skill_python = st.slider("Python", 0, 100, 90)
    st.progress(skill_python)
    
    skill_js = st.slider("JavaScript", 0, 100, 75)
    st.progress(skill_js)
    
    skill_AI = st.slider("Artificial Intelligence", 0, 100, 65)
    st.progress(skill_AI)

    skill_MachineLearning = st.slider("Machine Learning", 0, 100, 75)
    st.progress(skill_MachineLearning)

    skill_React = st.slider("React Js", 0, 100, 75)
    st.progress(skill_React)


    
    st.subheader("🏆 Certifications & Achievements")
    st.write("✔ Completed AI & ML in Business Certification")
    st.write("✔ Certified AI in Research and Course Preparation for Education")

# Contact section
elif page == "Contact":
    st.title("📬 Contact Me")
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your message")
        
        submitted = st.form_submit_button("Send Message")
        if submitted:
            if name and email and message:
                st.success("✅ Message sent successfully!")
                # Displaying the message after submission
                st.write(f"Name: {name}")
                st.write(f"Email: {email}")
                st.write(f"Message: {message}")
            else:
                st.error("⚠ Please fill in all fields before submitting.")

    # Contact Information Links
    st.markdown("📧 Email:** denysetuza@gmail.com")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/denyse-nyiratuza-545020355/)")
    st.markdown("[📂 GitHub](https://github.com/tuza421)")
    st.markdown("[📂 Instagram](https://www.instagram.com/tuza__1/)")


# Settings section
elif page == "Settings":
    st.title("⚙ Settings")

    # Theme Customization (Light/Dark Mode)
    theme = st.selectbox("Choose Theme", ["Light", "Dark"])
    if theme == "Dark":
        st.markdown("""
            <style>
                .main {background-color: #2E2E2E; color: white;}
                .stSidebar {background-color: #1E1E1E; color: white;}
                .stButton > button {background-color: #1F618D; color: white; border-radius: 10px;}
                .stExpander {background-color: #2E2E2E; color: white;}
                .stProgress {background-color: #D5D8DC;}
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                .main {background-color: #f5f7fa; color: black;}
                .stSidebar {background-color: #2E4053; color: white;}
                .stButton > button {background-color: #1F618D; color: white; border-radius: 10px;}
                .stExpander {background-color: #f5f7fa; color: black;}
                .stProgress {background-color: #D5D8DC;}
            </style>
        """, unsafe_allow_html=True)

# Student Testimonials Section
if page == "Testimonials":
    st.title("🗣 Student Testimonials")
    
    # Display example testimonial
    st.subheader("💬Testimonial:")
    st.write("Denyse is a brilliant problem solver! His final year project is truly innovative. – Mclement")
    
    st.markdown("---")
    
    # Allow classmates or mentors to leave testimonials
    st.subheader("✍ Leave a Testimonial")
    
    with st.form("testimonial_form"):
        name = st.text_input("Your Name")
        relationship = st.selectbox("Your Relationship", ["Classmate", "Mentor", "Teammate", "Other"])
        testimonial_message = st.text_area("Your Testimonial")
        
        submitted = st.form_submit_button("Submit Testimonial")
        if submitted:
            if name and testimonial_message:
                st.success(f"✅ Thank you, {name}! Your testimonial has been submitted.")
                # Display the testimonial after submission
                st.write(f"🗨 {testimonial_message} — {name} ({relationship})")
            else:
                st.error("⚠ Please fill in all fields before submitting.")