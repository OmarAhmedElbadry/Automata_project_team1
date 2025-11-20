# writers.py

class Writer:

    @staticmethod
    def write_output(results, filename="analysis_output.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("WORD ANALYSIS REPORT\n")
            f.write("=====================\n\n")

            for item in results:
                f.write(f"Word: {item['word']}\n")
                f.write(f"Type: {item['type']}\n")
                f.write(f"Line Number (Ln): {item['ln']}\n")
                f.write(f"Column Number (Col): {item['col']}\n")
                f.write("------------------------\n")

        print(f"Analysis file created: {filename}")

    @staticmethod
    def write_masked_text(masked_text, filename="masked_output.txt"):
        """
        تكتب النص الذي تم إخفاء أرقام الهواتف فيه إلى ملف منفصل.
        """
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(masked_text)
            print(f"Masked text file created: {filename}")
        except Exception as e:
            print(f"Error writing masked text file: {e}")