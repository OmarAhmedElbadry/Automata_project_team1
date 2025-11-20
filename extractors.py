# extractors.py

import re
import phonenumbers
from email_validator import validate_email

# اكود الدول المسموح بيها
VALID_COUNTRY_CODES = {
    "20", "971", "966", "1", "44", "49", "33", "39", "34", "81", "82", "90"
}

# أرقام مزيفة معروفة
FAKE_NUMBERS = [
    "1234567890", "1111111111", "2222222222", "3333333333",
    "4444444444", "5555555555", "6666666666",
    "7777777777", "8888888888", "9999999999"
]


def is_valid_human_number(num_obj, formatted):

    # فلتر لرفض الأرقام الوهمية والتحقق من كود الدولة


    clean_num = formatted.replace("+", "")

    if len(clean_num) < 10 or len(clean_num) > 15:
        return False

    for fake in FAKE_NUMBERS:
        if fake in clean_num:
            return False

    country_code = str(num_obj.country_code)
    if country_code not in VALID_COUNTRY_CODES:
        return False

    return True


class Extractors:
    EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    @staticmethod
    def extract_emails(text):
        matches = list(re.finditer(Extractors.EMAIL_REGEX, text))
        results = []

        for m in matches:
            try:
                valid = validate_email(m.group(), check_deliverability=False).email
                results.append({
                    "value": valid,
                    "start": m.start(),
                    "end": m.end()
                })
            except:
                pass

        return results

    @staticmethod
    def extract_phones(text):
        results = []
        found_matches = set()

        for match in phonenumbers.PhoneNumberMatcher(text, "ZZ"):
            num = match.number

            if phonenumbers.is_valid_number(num):
                try:
                    formatted = phonenumbers.format_number(
                        num, phonenumbers.PhoneNumberFormat.E164
                    )
                except:
                    continue

                if formatted in found_matches:
                    continue

                if not is_valid_human_number(num, formatted):
                    continue

                results.append({
                    "value": formatted,
                    "start": match.start,
                    "end": match.end
                })
                found_matches.add(formatted)

        return results