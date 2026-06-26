# PROV3RBS
<p align="center">
  <img src="1782488010039.png" alt="Profile Image" width="400"/>
</p>

> An open-source hub for 915 curated proverbs, engineered for seamless collaboration. Featuring real-time messaging and integrated video study rooms, it enables distributed teams to share wisdom. Built for scholars, this secure, high-performance ecosystem provides the optimal environment for global peer-to-peer learning and deep intellectual growth.

---

### 📦 Core Programming Languages

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)

### ⚙️ Core Systems

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
![Uvicorn](https://img.shields.io/badge/uvicorn-4051B5?style=for-the-badge&logo=python&logoColor=white)
![WebSockets](https://img.shields.io/badge/WebSockets-010101?style=for-the-badge&logo=google-chrome&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F1F?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### 💻 Platform software & Hardware Architecture

![Ubuntu Linux](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Async IO](https://img.shields.io/badge/Asynchronous-IO-blueviolet?style=for-the-badge&logo=python)

### 🛠️ DevOps, Infrastructure & Build Tools

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/docker%20compose-4196EC?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232088FF.svg?style=for-the-badge&logo=github-actions&logoColor=white)
![GNU Make](https://img.shields.io/badge/GNU%20Make-000000?style=for-the-badge&logo=gnu&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

### ⚡ Low-Level Infrastructure & Performance

![WebRTC](https://img.shields.io/badge/WebRTC-333333?style=for-the-badge&logo=webrtc&logoColor=white)
![Real Time Multiplexing](https://img.shields.io/badge/Multiplexing-Active-success?style=for-the-badge)

### 🛡️ Cybersecurity & Offensive Auditing

![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)
![Dotenv](https://img.shields.io/badge/.ENV-Secure-yellowgreen?style=for-the-badge)

### 🧠 Artificial Intelligence & Quantum

![Structured Dataset](https://img.shields.io/badge/Dataset-915%20Tokens-orange?style=for-the-badge&logo=databricks&logoColor=white)
![NLP Prompt Ready](https://img.shields.io/badge/NLP-LLM%20Ready-lightgrey?style=for-the-badge)

### ☁️ Cloud Providers

![LiveKit Cloud](https://img.shields.io/badge/LiveKit%20Cloud-0052CC?style=for-the-badge&logo=google-cloud&logoColor=white)

### 👥 Client Frameworks

![Vanilla JS ES6](https://img.shields.io/badge/Vanilla%20JS-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![LiveKit Client SDK](https://img.shields.io/badge/LiveKit%20SDK-Client-brightgreen?style=for-the-badge)

## ⚡ Why is PROV3RBS Cool?

* **Modern Tech Stack:** Utilizes **FastAPI** for ultra-fast, asynchronous backend performance, coupled with **WebSockets** for real-time, low-latency chat.
* **Integrated WebRTC:** Incorporates **LiveKit** to bypass the massive overhead of building a video streaming engine from scratch, delivering enterprise-grade video/audio study rooms directly in the browser.
* **Strict Data Integrity:** A CI/CD pipeline enforces a hard rule of exactly 915 entries. This makes the databank highly predictable and stable for programmatic querying.
* **Global Accessibility:** Out-of-the-box localization across 10 languages allows the UI and metadata to adapt dynamically to international users via a simple URL parameter.

---

## 🎯 What Problems Does This Solve?

* **Distributed Learning Isolation:** Remote developers, scholars, or students often study in silos. PROV3RBS provides a dedicated, localized peer-to-peer space to share knowledge and communicate visually without relying on heavy third-party applications.
* **Tool Fatigue:** Instead of toggling between a reference database, a messaging app, and a video client, users have a single, unified micro-SaaS environment tailored specifically for collaborative focus.
* **Data Pipeline Breakages:** The strict automated validation (`tests/validate.py`) prevents accidental data deletion by ensuring the core repository cannot be updated unless the 915-item constraint is perfectly met.

---

## 🚀 How to Use It

1.  **Launch & Localize:** Navigate to the application URL. By appending `/?lang=es` (or any of the 10 supported language codes), the interface seamlessly updates to your preferred language.
2.  **Join a Study Room:** Clicking **"Join Video"** generates a secure JWT token via the backend and connects your camera and microphone to a shared LiveKit WebRTC room.
3.  **Real-Time Collaboration:** Chat in the shared WebSocket terminal to discuss code, exchange ideas, or coordinate study sessions.
4.  **Fetch Wisdom:** Query the `/api/proverb` REST endpoint to pull a random proverb from the 915-entry databank to serve as a daily prompt, discussion topic, or deep-learning training seed.

---

## ⚙️ Installation & Deployment

### 1. Clone & Set Up the Environment
Pull the repository and set up your environment variables. You will need a free account from [LiveKit Cloud](https://livekit.io/) for the WebRTC keys.

```bash
git clone [https://github.com/credkellar-boop/PROV3RBS.git](https://github.com/credkellar-boop/PROV3RBS.git)
cd PROV3RBS
cp .env.example .env
