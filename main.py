import re
import phonenumbers
from email_validator import validate_email
import os
import PyPDF2
from docx import Document
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select a file (TXT, PDF, or DOCX)",
    filetypes=[
        ("All supported files", "*.txt *.pdf *.docx"),
        ("Text files", "*.txt"),
        ("PDF files", "*.pdf"),
        ("Word files", "*.docx"),
        ("All files", "*.*")
    ]
)

if not file_path:
    print("No file selected. Exiting.")
    exit()

if not os.path.isfile(file_path):
    print("Invalid file path or file not found.")
    exit()

file_extension = os.path.splitext(file_path)[1].lower()
text = ""

if file_extension == ".txt":
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    print("TXT file loaded successfully.")

elif file_extension == ".pdf":
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += (page.extract_text() or "") + "\n"
    print("PDF file loaded successfully.")

elif file_extension == ".docx":
    doc = Document(file_path)
    for para in doc.paragraphs:
        text += para.text + "\n"
    print("Word file loaded successfully.")

else:
    print(f"Unsupported file type '{file_extension}'.")
    exit()

email_pattern = r"[a-zA-Z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
emails = re.findall(email_pattern, text)
print("\nFound emails:", emails)

valid_emails = []
for e in emails:
    result = validate_email(e, check_deliverability=False)
    valid_emails.append(result.email)

print("✅ Valid emails:", valid_emails)

print("\n Found phone numbers:")
phone_numbers = []
for match in phonenumbers.PhoneNumberMatcher(text, None):
    num = match.number
    if phonenumbers.is_valid_number(num):
        formatted = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.E164)
        phone_numbers.append(formatted)
        print("•", formatted)
    else:
        print("• Invalid number:", phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.INTERNATIONAL))

data = {"emails": valid_emails, "phones": phone_numbers}
print("\nSummary:", data)