import streamlit as st
from chains import Chain
from portfolio import Portfolio
from utils import clean_text
from dotenv import load_dotenv
import os

# 1. Load env only once
load_dotenv()
key = os.getenv("GROQ_API_KEY")

# 2. Page Config
st.set_page_config(
    page_title="AI Cold Email Generator",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 3. Custom CSS for pro look
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #2563EB 0%, #9333EA 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #6B7280;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background: linear-gradient(90deg, #2563EB 0%, #1D4ED8 100%);
        color: white;
        font-weight: 600;
        border-radius: 10px;
        padding: 0.7rem 2rem;
        border: none;
        width: 100%;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #1D4ED8 0%, #1E40AF 100%);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }
    .skill-tag {
        display: inline-block;
        background: #DBEAFE;
        color: #1E40AF;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        margin: 0.2rem;
    }
    .email-box {
        background-color: #FFFFFF;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #E5E7EB;
        white-space: pre-wrap;
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    .debug-box {
        background: #FEF3C7;
        border-left: 4px solid #F59E0B;
        padding: 0.8rem;
        border-radius: 6px;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# 4. Header
st.markdown('<p class="main-header">AI Cold Email Generator</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Generate personalized cold emails for Internships & Jobs in 10 seconds</p>',
            unsafe_allow_html=True)

# 5. API Key Status in sidebar
with st.sidebar:
    st.subheader("⚙️ Settings")
    if key:
        st.success(f"GROQ API Key Loaded: {key[:8]}...")
    else:
        st.error("GROQ API Key NOT FOUND")
        st.info("Add GROQ_API_KEY to your .env file")

    tone = st.selectbox("Email Tone", ["Professional", "Friendly", "Direct"])
    st.divider()
    st.caption("Made with ❤️ by Akshay Prabhe")

st.divider()

col1, col2 = st.columns([1, 1.2], gap="large")

# 6. Initialize classes - only once
chain = Chain()
portfolio = Portfolio()  # load_portfolio() removed because we load it in __init__

with col1:
    st.subheader("📄 Step 1: Paste Job Description")
    job_description = st.text_area(
        "Paste the full job description here",
        height=350,
        placeholder="Paste the Backend Engineer JD from LinkedIn/Indeed here..."
    )

    st.subheader("🔗 Step 2: Your Portfolio Links")
    links_input = st.text_input(
        "Add relevant project links separated by comma",
        value="https://github.com/Akshayprabhe/cold-email-generation-tool"
    )
    link_list = [link.strip() for link in links_input.split(",") if link.strip()]

    generate_btn = st.button("⚡ Generate Professional Email", use_container_width=True)

with col2:
    st.subheader("✉️ Step 3: Your Generated Email")

    if generate_btn:
        if not job_description:
            st.warning("Please paste a Job Description first")
        elif not key:
            st.error("GROQ_API_KEY missing. Please add it to .env file")
        else:
            with st.spinner("AI is analyzing JD and writing your email..."):
                try:
                    # Clean text
                    clean_jd = clean_text(job_description)

                    # Extract jobs/skills
                    jobs = chain.extract_jobs(clean_jd)

                    if not jobs:
                        st.error("Could not extract job info. Try a more detailed JD")
                    else:
                        email_content = ""

                        for job in jobs:
                            job_title = job.get('role', 'the role')
                            skills = job.get('skills', [])

                            # NEW FEATURE 1: Show extracted skills
                            if skills:
                                st.markdown("**🎯 Skills Detected:**")
                                skill_html = "".join([f'<span class="skill-tag">{s}</span>' for s in skills])
                                st.markdown(skill_html, unsafe_allow_html=True)
                                st.write("")

                            # Get portfolio links
                            portfolio_links = portfolio.query_links(" ".join(skills)) if skills else []
                            final_links = portfolio_links if portfolio_links else link_list

                            # NEW FEATURE 2: Pass tone to chain
                            email = chain.write_mail(job, final_links, tone)
                            email_content += f"### For: {job_title}\n\n"
                            email_content += email + "\n\n" + "---" + "\n\n"

                        st.markdown(f'<div class="email-box">{email_content}</div>', unsafe_allow_html=True)

                        st.download_button(
                            label="📥 Download Email as .txt",
                            data=email_content,
                            file_name="cold_email.txt",
                            mime="text/plain",
                            use_container_width=True
                        )

                except Exception as e:
                    st.error(f"Error: {e}")
                    st.info("Check if vectorstore folder exists and GROQ API key is valid")
    else:
        st.info("👈 Paste a JD and click 'Generate Professional Email' to see results here")

st.divider()
st.markdown(
    "<p style='text-align: center; color: #6B7280;'>Built by Akshay Prabhe | 4th Year AIDS Engineering Student</p>",
    unsafe_allow_html=True)