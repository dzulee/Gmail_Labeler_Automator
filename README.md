
# 🤖 AI-Powered Gmail Workflow (Zero-Shot Classifier)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-Transformers-orange)](https://huggingface.co/facebook/bart-large-mnli)

An intelligent, autonomous email automation workflow that categorizes unread Gmail messages using Natural Language Processing. Unlike traditional rule-based filters, this project uses the **BART Large MNLI** model to "understand" the context of your emails and label them dynamically.

---

## 🚀 Key Features
* **AI Classification:** Uses HuggingFace Transformers to categorize emails without pre-defined keywords.
* **Dynamic Labeling:** Automatically creates nested Gmail labels (e.g., `Auto/Finance`) if they don't exist.
* **Headless Ready:** Designed to run on local machines via Task Scheduler or in Kaggle environments.
* **Security Focused:** Built with OAuth 2.0 flow and `.gitignore` safety to protect private tokens.
* **Persistence:** Includes a local logging system (`automation_log.txt`) to track AI decisions.

---

## 🛠️ Project Structure
```text
├── automation.py       # Main automation script with AI logic
├── auth.py             # Local authentication script to generate token.json
├── .gitignore          # Prevents sensitive tokens from being pushed to GitHub
├── requirements.txt    # List of necessary Python libraries
└── README.md           # Project documentation
🔧 Setup & Installation
1. Prerequisites
Python 3.8+

A Google Cloud Project with the Gmail API enabled.

credentials.json downloaded from the Google Cloud Console.

2. Installation
Bash
# Clone the repository
git clone [https://github.com/your-username/Gmail_labeler_Automator.git](https://github.com/your-username/Gmail_labeler_Automator.git)
cd Gmail_labeler_Automator

# Create and activate a virtual environment
python -m venv venv

# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
3. Google API Setup
Enable the Gmail API in your Google Cloud Console.

Download your OAuth client credentials.json to the root folder.

Run the local auth script once to generate token.json:

Bash
python auth.py
🤖 Usage
Run the script manually:

Bash
python automation.py
Run as a background service (Windows):

Bash
pythonw automation.pyw
📝 Configuration
Update the MY_LABELS list in automation.py to customize your categories:

Python
MY_LABELS = ["Auto/Work", "Auto/Finance", "Auto/Travel", "Auto/Social"]
🛡️ Security Note
This project uses .gitignore to ensure that credentials.json and token.json are never uploaded to GitHub. Always keep these files private as they grant full access to your Gmail account.

📄 License
MIT License - feel free to use and modify for your own workflows!
