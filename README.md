# 📝 Text Analysis & Phone Masking Tool

A **Python tool** to extract **emails** ✉️ and **phone numbers** 📞 from text, PDF, and DOCX files, analyze their positions (line & column), and generate a masked version of phone numbers for privacy 🔒.

---

## ✨ Features

- 🔹 Extract **emails** and **phone numbers** from `.txt`, `.pdf`, and `.docx` files.
- 🔹 Calculate **line number (Ln)** and **column number (Col)** for each extracted item.
- 🔹 Mask phone numbers by replacing the **last 6 digits** with `*` while preserving the text layout.
- 🔹 Generate two output files:
  - `analysis_output.txt` → Detailed report with **Word**, **Type**, **Line**, and **Column**.
  - `masked_output.txt` → Original text with **partially masked phone numbers**.
- 🔹 Supports **international phone numbers** with country code validation 🌍.



Project Structure

├── main.py            # Main script to run the application
├── file_loader.py     # Handles reading TXT, PDF, DOCX files
├── extractors.py      # Extract emails and phone numbers
├── analyzer.py        # Calculate line and column positions
├── writers.py         # Write output reports and masked text
└── README.md


# WORD ANALYSIS Sample 

<img width="831" height="423" alt="image" src="https://github.com/user-attachments/assets/4af146bd-8237-412d-8d44-3e0602c050db" />


# Masked Text File
<img width="712" height="317" alt="image" src="https://github.com/user-attachments/assets/f18b84e1-7743-449b-a8e9-e5394816608d" />



