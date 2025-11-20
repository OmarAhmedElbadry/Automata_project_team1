# main.py

import tkinter as tk
from tkinter import filedialog
import re

from file_loader import FileLoader
from extractors import Extractors
from analyzer import Analyzer
from writer import Writer

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select a file",
    filetypes=[
        ("Text, PDF, DOCX", "*.txt *.pdf *.docx"),
        ("All files", "*.*")
    ]
)

if not file_path:
    print("No file selected.")
    exit()

try:
    text = FileLoader.load_file(file_path)
except Exception as e:
    print(f"Error loading file: {e}")
    exit()

emails = Extractors.extract_emails(text)
phones = Extractors.extract_phones(text)

analysis = Analyzer.analyze(text, emails, phones)

# 2. إخفاء الأرقام وإنشاء النص المخفي
masked_text = text

# فرز الأرقام من النهاية إلى البداية لتجنب تغيير المواقع (Indexes)
patterns_to_mask = sorted(phones, key=lambda x: x["start"], reverse=True)

# عدد الأرقام المراد إخفاؤها
MASK_LENGTH = 6

for p in patterns_to_mask:

    start = p["start"]
    end = p["end"]

    # الحصول على النص الأصلي الذي تم مطابقته
    original_text_slice = text[start:end]
    original_length = len(original_text_slice)

    # التحقق من أن النص طويل بما يكفي للإخفاء
    if original_length >= MASK_LENGTH:
        unmasked_part = original_text_slice[:-MASK_LENGTH]
        mask = '*' * MASK_LENGTH

        masked_value = unmasked_part + mask
    else:
        masked_value = '*' * original_length

    masked_text = masked_text[:start] + masked_value + masked_text[end:]

# 3. كتابة ملفات الإخراج
Writer.write_output(analysis)
Writer.write_masked_text(masked_text, "masked_output.txt")