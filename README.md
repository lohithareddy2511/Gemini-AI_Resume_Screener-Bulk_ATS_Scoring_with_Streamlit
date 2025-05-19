# Gemini-AI_Resume_Screener-Bulk_ATS_Scoring_with_Streamlit

A powerful and intelligent web app built with **Streamlit** that allows recruiters and HR professionals to **upload multiple resumes** in PDF format and automatically **analyze, score, and rank candidates** based on a provided job description. The app uses **Google Gemini AI** to extract meaningful insights and simulate an advanced **ATS (Applicant Tracking System)** analysis — saving hours of manual screening time.

> ✅ **Advantageous for hiring managers and recruiters** — streamlines candidate screening and improves hiring efficiency.

## 🚀 Features

* 🔍 Analyze up to **100 resumes** at once
* 🤖 Leverages **Google Gemini 1.5 Flash** for intelligent analysis
* 📈 Provides **Match Percentage**, **Keyword Matching**, **Skill Gap Analysis**, and **Recommendations**
* 📊 Auto-generated **ranked table** of candidates based on job fit
* 📄 Supports **PDF resumes**
* 🧠 Uses **OPEA™-style modular logic** and integrates future extensibility for HR tech stacks

## 🧰 Tech Stack

* **Python 3.9+**
* [Streamlit](https://streamlit.io/)
* [Google Generative AI (Gemini)](https://ai.google.dev/)
* [pdf2image](https://pypi.org/project/pdf2image/)
* [Pillow (PIL)](https://pypi.org/project/Pillow/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* **Poppler for Windows** (PDF rendering)

## 🖼 Demo



## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/ats-resume-analyzer.git
cd ats-resume-analyzer
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
   Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

5. **Install Poppler (for PDF rendering)**

* Download from: [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)
* Extract and update the path in the script:

```python
poppler_path = r"C:\Program Files (x86)\poppler-xx.xx\Library\bin"
```

## 🚦 Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Enter the **job description** in the text area.

3. Upload multiple **PDF resumes** (up to 100).

4. Click **"Analyze All Resumes and Rank Candidates"** to process and view results.

## 📊 Output Format

Each candidate analysis includes:

* 🔹 **Match Percentage:** e.g., 85%
* 🔹 **Matched Keywords**
* 🔹 **Missing Keywords**
* 🔹 **Skill Gap Analysis**
* 🔹 **Recommendations**

## 📁 Project Structure

```
ats-resume-analyzer/
│
├── app.py                # Main Streamlit application
├── .env                  # Environment variables (not checked in)
├── requirements.txt      # Python dependencies
├── README.md             # You're here!
```

## 🧠 Future Enhancements

* 🗃 Export reports to CSV/PDF
* 🧬 Add multilingual support
* 💬 Integrate chatbot interface for recruiters
* 🧠 Extend with skill clustering and industry taxonomy using OPEA™-like microservices


## 🙋‍♂️ Acknowledgments

* [Google Generative AI](https://ai.google.dev/)
* [Streamlit](https://streamlit.io/)
* [Intel OPEA™ Concept](https://www.intel.com) — inspiration for modular AI integration.
