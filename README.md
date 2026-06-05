# 🎓 CampusGuard AI Pro

## AI-Powered Multi-Agent Platform for Academic Assistance and News Verification

CampusGuard AI Pro is an intelligent multi-agent platform designed to help students manage academic information efficiently while also verifying the credibility of online news content.

Built using Flask, Groq LLM, and Llama 3.3 70B, the platform combines academic notice analysis, personalized study planning, and AI-powered news credibility detection into a single system.

---

## 🚀 Key Features

### 🎓 Academic Agent

The Academic Agent helps students stay organized and prepared by:

* 📄 Analyzing academic notices automatically
* 📅 Extracting important dates and deadlines
* ⚠️ Detecting academic risks and alerts
* 🎯 Generating student readiness scores
* ✅ Creating action-item checklists
* 🤖 Answering questions about uploaded notices
* 📚 Generating personalized study plans
* 📖 Providing study recommendations

---

### 📰 NewsGuard AI

The NewsGuard Agent helps users identify potentially misleading information by:

* 📰 Analyzing news headlines and articles
* 🎯 Generating credibility/trust scores
* ⚠️ Detecting misinformation indicators
* 🔍 Identifying red flags in news content
* ✅ Providing final credibility verdicts
* 📌 Recommending fact-checking actions
* 🌐 Suggesting trusted verification sources

---

## 🛠️ Technology Stack

### Frontend

* HTML5
* CSS3

### Backend

* Python
* Flask

### Artificial Intelligence

* Groq API
* Llama 3.3 70B Versatile

### Document Processing

* PyPDF

---

## 📂 Project Structure

```text
fake-news-detector/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── news.html
│
├── static/
│   └── style.css
│
├── screenshots/
│   ├── home.png
│   ├── analysis.png
│   ├── ask_ai.png
│   ├── study_plan_result.png
│   └── NewsGuardResult.png
│
└── uploads/
```

---

## 📸 Screenshots

### Home Dashboard

![Home](screenshots/home.png)

### Academic Notice Analysis

![Analysis](screenshots/analysis.png)

### Personalized Study Plan

![Study Plan](screenshots/study_plan_result.png)

### NewsGuard AI

![NewsGuard](screenshots/NewsGuardResult.png)

### AI Academic Assistant

![CampusGuard AI](screenshots/ask_ai.png)

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Syedabdulazeez-021/CampusGuard-AI-Pro.git

cd CampusGuard-AI-Pro
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🎯 Use Cases

### Academic Notice Analysis

Students can upload official college notices and automatically obtain:

* Executive summaries
* Important dates
* Deadlines
* Risk alerts
* Action items
* Readiness scores

### AI Academic Assistant

Students can ask questions related to uploaded notices and receive intelligent responses.

### Personalized Study Planning

The system generates customized study schedules based on examination information and deadlines.

### News Credibility Verification

Users can paste news articles or headlines and receive:

* Trust score
* Risk assessment
* Credibility analysis
* Fact-check recommendations
* Verification resources

---

## 🔮 Future Enhancements

* OCR support for scanned notices
* Calendar integration
* Automated reminder system
* Multi-language support
* Real-time fact-check APIs
* Mobile application
* Student performance analytics

---

## 👨‍💻 Developed By

**Abdul Azeez**

AI-Powered Student Productivity and Information Verification Platform

Built using Flask + Groq + Llama 3.3 70B
