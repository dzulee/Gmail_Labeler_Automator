# 🤖 AI-Powered Gmail Workflow (Zero-Shot Classifier)

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
## 🛠️ Installation

## 1. **Clone the repo:**
     ```bash
     git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
     cd your-repo-name
## 2. **Setup Virtual Environment:**
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    pip install -r requirements.txt

## 🔧 Setup & Installation
1. Prerequisites
Python 3.8+

A Google Cloud Project with the Gmail API enabled.

credentials.json downloaded from the Google Cloud Console.

2. Installation
   # Clone the repository
    git clone [https://github.com/yourusername/gmail-ai-classifier.git](https://github.com/yourusername/gmail-ai-classifier.git)
    cd gmail-ai-classifier

    # Create and activate a virtual environment
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    
    # Install dependencies
    pip install -r requirements.txt


### 3. **Google API Setup:**

    Enable the Gmail API in Google Cloud Console.
    
    Download credentials.json to the root folder.
    
    Run a local auth script once to generate token.json.

### 4. 🚀 Usage
      Run the script manually:
      
      Bash
      python automation.py
      Or run as a background service:
      
      Bash
      pythonw automation.pyw
### 5. 📝 Configuration
    Update the MY_LABELS list in automation.py to customize your categories:
    
    Python
    MY_LABELS = ["Auto/Work", "Auto/Finance", "Auto/Travel"]
    
    ---

### 6. Generate a `requirements.txt`
GitHub users expect this file so they know what to install. Run this in your terminal:
    ```bash
    pip freeze > requirements.txt

### 🛡️ Security Note
This project uses .gitignore to ensure that credentials.json and token.json are never uploaded to GitHub. Always keep these files private as they grant access to your Gmail account.
---

### 🛡️ Final Check: Your `.gitignore`
Make sure you have a file named `.gitignore` in the same folder. If you don't, GitHub will accidentally upload your private keys. Use this content:

```text
# Local credentials
credentials.json
token.json

# Environment
venv/
__pycache__/
.cache/

# Logs
automation_log.txt

📄 License
MIT License - feel free to use and modify for your own workflows!
