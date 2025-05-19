from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
import pandas as pd
from PIL import Image
import pdf2image
import google.generativeai as genai

# Configure API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set Poppler Path
poppler_path = r"C:\Program Files (x86)\poppler-24.08.0\Library\bin"  # Update this path

# Function to get response from Gemini AI
def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text

# Function to process uploaded PDFs
def process_pdf(uploaded_file):
    try:
        images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=poppler_path)
        first_page = images[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format="JPEG")
        img_byte_arr = img_byte_arr.getvalue()

        return [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode(),
            }
        ]
    except Exception as e:
        st.error(f"❌ Error processing PDF {uploaded_file.name}: {e}")
        return None

# Streamlit App Configuration
st.set_page_config(page_title="ATS Resume Expert", page_icon="📄", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: #007bff;'>📑 ATS Resume Analyzer</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='text-align: center; color: gray;'>Bulk Resume Screening for Hiring</h3>",
    unsafe_allow_html=True,
)

st.divider()

# Job Description Input
job_description = st.text_area("📋 Paste Job Description Here:", key="input", height=150)

# Multiple Resume Upload
uploaded_files = st.file_uploader(
    "📂 Upload Resumes (PDF) - Up to 100 Files",
    type=["pdf"],
    accept_multiple_files=True,
)

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} Resumes Uploaded Successfully!")

# Button to analyze all resumes
if st.button("📊 Analyze All Resumes and Rank Candidates"):

    if not uploaded_files:
        st.warning("⚠️ Please upload at least one resume.")
    elif not job_description:
        st.warning("⚠️ Please enter the job description.")
    else:
        st.info("⏳ Processing resumes... This may take a few minutes.")

        results = []

        for file in uploaded_files:
            pdf_content = process_pdf(file)
            if pdf_content:
                response = get_gemini_response(job_description, pdf_content, """
                You are an advanced ATS system analyzing resumes for job fit. 
                Provide a **Match Percentage (0%-100%)** and key insights.
                Your output should strictly follow this format:

                🔹 **Match Percentage:** _(XX%)_
                🔹 **Matched Keywords:** _(List key terms found)_
                🔹 **Missing Keywords:** _(List key terms missing)_
                🔹 **Skill Gap Analysis:** _(Mention missing qualifications/skills)_
                🔹 **Recommendations:** _(Suggestions to improve resume alignment)_
                """)

                # Extracting percentage from response
                match_percentage = 0
                try:
                    match_percentage = int(
                        [s for s in response.split() if "%" in s][0].replace("%", "")
                    )
                except:
                    pass

                results.append(
                    {
                        "Candidate Name": file.name.replace(".pdf", ""),
                        "Match Score": match_percentage,
                        "Analysis": response,
                    }
                )

        # Sort results by Match Percentage (Highest First)
        results = sorted(results, key=lambda x: x["Match Score"], reverse=True)

        # Display results in a table
        st.markdown("<h3 style='color: #007bff;'>📋 Ranked Candidates:</h3>", unsafe_allow_html=True)

        df = pd.DataFrame(results, columns=["Candidate Name", "Match Score"])
        st.dataframe(df, height=500, width=800)

        # Expandable sections for detailed analysis
        for res in results:
            with st.expander(f"📄 {res['Candidate Name']} - {res['Match Score']}% Match"):
                st.markdown(f"<div style='padding:10px; background-color:#f4f4f4; border-left:5px solid #007bff;'>{res['Analysis']}</div>", unsafe_allow_html=True)
