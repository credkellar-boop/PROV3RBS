# PROV3RBS

> An open-source hub for 915 curated proverbs, engineered for seamless collaboration. Featuring real-time messaging and integrated video study rooms, it enables distributed teams to share wisdom. Built for scholars, this secure, high-performance ecosystem provides the optimal environment for global peer-to-peer learning and deep intellectual growth.

---

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
