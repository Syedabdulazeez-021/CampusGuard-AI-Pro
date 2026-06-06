from flask import Flask, render_template, request, session
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = "campusguard_secret"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_pdf():

    file = request.files["pdf"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    reader = PdfReader(filepath)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    session["notice_text"] = text

    prompt = f"""
You are CampusGuard AI Pro.

You are a Responsible AI Academic Assistant.

Analyze the academic notice and generate the response in EXACTLY this format.

🎯 STUDENT READINESS SCORE
(Score out of 100)

🔍 SCORE EXPLANATION
(Explain why this score was assigned)

📌 EXECUTIVE SUMMARY

📅 IMPORTANT DATES

⏰ DEADLINES

⚠ RISK ALERTS

✅ ACTION ITEMS

📖 STUDY RECOMMENDATIONS

🎯 QUICK CHECKLIST

🛡 RESPONSIBLE AI NOTICE
(State that students should verify critical information from official college sources.)

NOTICE:

{text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.choices[0].message.content

    return render_template(
        "index.html",
        result=result
    )


@app.route("/ask", methods=["POST"])
def ask_question():

    question = request.form["question"]

    notice_text = session.get("notice_text", "")

    if not notice_text:
        return render_template(
            "index.html",
            answer="Please upload a PDF notice first."
        )

    prompt = f"""
You are CampusGuard AI Pro.

You are an intelligent academic assistant.

NOTICE:

{notice_text}

Rules:

1. Answer ONLY from the uploaded notice.
2. Highlight dates clearly.
3. Suggest actions when relevant.
4. Be concise and useful.
5. If the answer is not present, say:
   "This information is not available in the uploaded notice."

Student Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    return render_template(
        "index.html",
        answer=answer
    )


@app.route("/studyplan", methods=["POST"])
def study_plan():

    notice_text = session.get("notice_text", "")

    if not notice_text:
        return render_template(
            "index.html",
            answer="Please upload a PDF first."
        )

    prompt = f"""
You are CampusGuard AI Pro.

Using the academic notice below, generate:

📚 PERSONALIZED STUDY PLAN

Include:

1. Exam Timeline
2. Daily Study Schedule
3. Priority Subjects
4. Revision Strategy
5. Last Week Preparation Plan

Notice:

{notice_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    plan = response.choices[0].message.content

    return render_template(
        "index.html",
        answer=plan
    )

@app.route("/news")
def news_page():
    return render_template("news.html")


@app.route("/analyze_news", methods=["POST"])
def analyze_news():

    news_text = request.form["news_text"]

    prompt = f"""
You are NewsGuard AI.

You are a Responsible AI News Verification Agent.

Analyze the following news article or headline.

Generate the response in EXACTLY this format.

🎯 TRUST SCORE (0-100)

📈 CONFIDENCE SCORE
(How confident the AI is in this assessment)

⚠ RISK LEVEL
(Low / Medium / High)

📰 NEWS SUMMARY

🔍 RED FLAGS DETECTED

📊 CREDIBILITY ANALYSIS

🧠 WHY THIS RESULT?
(Explain the evidence and reasoning used)

📂 EVIDENCE USED
(List specific indicators found in the news)

🏛 SOURCE RELIABILITY ASSESSMENT
(Classify source reliability if possible)

✅ FINAL VERDICT
(Likely Genuine / Potentially Misleading / Needs Verification)

📌 FACT-CHECK RECOMMENDATIONS

🌐 RELIABLE SOURCES TO VERIFY

🛡 RESPONSIBLE AI NOTICE
(State that users should independently verify important claims and not rely solely on AI analysis.)

NEWS:

{news_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.choices[0].message.content

    return render_template(
        "news.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=False)