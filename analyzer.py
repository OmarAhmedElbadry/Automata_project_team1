# analyzer.py (لحساب Ln/Col)
import re

class Analyzer:

    @staticmethod
    def analyze(text, emails, phones):

        results = []
        # كلهم عندهم نفس ال keys
        patterns = emails + phones

        # 1. حساب مؤشرات بداية كل سطر جديد في النص الأصلي
        line_start_indices = [m.end() for m in re.finditer(r'[\n\r]', text)]
        line_start_indices.insert(0, 0)
        #  بيتأكد اخر حرف ف ال text موجود ف ال line_start_indices؟
        if line_start_indices[-1] != len(text):
            line_start_indices.append(len(text))

        for item in patterns:

            #{
             #   "value": "example@gmail.com",
              #  "start": 45,
               # "end": 63
            #}

            start = item["start"]

            line_number = None
            column_number = None

            # 2. تحديد رقم السطر (Ln)
            for idx in range(len(line_start_indices) - 1):
                start_of_line = line_start_indices[idx]
                end_of_line = line_start_indices[idx + 1]

                # لو بداية الكلمة (start) موجود بين بداية السطر الحالي ونهاية السطر ده بقى الكلمة موجودة هنا
                if start_of_line <= start < end_of_line:
                    line_number = idx + 1  # رقم السطر (يبدأ من 1)

                    # 3. تحديد رقم العمود (Col)
                    column_number = start - start_of_line + 1
                    break

            if line_number is None:
                line_number = "Error/Index Out of Bounds"
                column_number = "Error/Index Out of Bounds"

            results.append({
                "word": item["value"],
                "type": "Email" if item["value"].find('@') != -1 else "PhoneNumber",
                "ln": line_number,
                "col": column_number
            })

        return results