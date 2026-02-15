import time
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from transformers import pipeline

# --- CONFIGURATION ---
TOKEN_PATH = 'token.json'  
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
MY_LABELS = ["Auto/Work", "Auto/Finance", "Auto/Travel", "Auto/Social"]

# Load Auth & Service
creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
service = build('gmail', 'v1', credentials=creds)

# Load AI Model (This stays in memory while the script runs)
print("Loading AI model...")
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def get_or_create_label(label_name):
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    for l in labels:
        if l['name'].lower() == label_name.lower():
            return l['id']
    
    label_body = {'name': label_name, 'labelListVisibility': 'labelShow', 'messageListVisibility': 'show'}
    new_label = service.users().labels().create(userId='me', body=label_body).execute()
    return new_label['id']

def process_emails():
    print(f"Checking for unread emails at {time.strftime('%H:%M:%S')}...")
    
    # 1. Fetch emails FIRST
    query = "is:unread newer_than:1d"
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])

    # 2. Log the result NOW that 'messages' is defined
    with open("automation_log.txt", "a") as f:
        f.write(f"[{time.ctime()}] Check performed. Found {len(messages)} unread emails.\n")

    if not messages:
        print("No unread emails found.")
        return

    for msg in messages:
        details = service.users().messages().get(userId='me', id=msg['id']).execute()
        snippet = details.get('snippet', '')
        
        prediction = classifier(snippet, MY_LABELS)
        best_label = prediction['labels'][0]
        confidence = prediction['scores'][0]
        
        print(f"Found: {snippet[:50]}...")
        if confidence > 0.6:
            label_id = get_or_create_label(best_label)
            service.users().messages().modify(
                userId='me', 
                id=msg['id'], 
                body={'addLabelIds': [label_id], 'removeLabelIds': ['UNREAD']}
            ).execute()
            print(f"Action: Labeled as {best_label}")
    
    print("Batch complete.")

if __name__ == "__main__":
    print("Automation Started. Press Ctrl+C to stop.")
    while True:
        try:
            process_emails()
        except Exception as e:
            print(f"Error occurred: {e}")
        
        # Sleep for 10 minutes
        time.sleep(600)

     