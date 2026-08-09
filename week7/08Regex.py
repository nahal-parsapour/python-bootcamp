# work with Regular Expressions (Regex)
import re

# --------------- Exercise 1 ---------------
sample_text = (
    "Use John called with email john@mail.com and number 09123456789 . "
    "Meeting date is 1403/05/12. Post is 1234567890 , price 2500 USD."
)

# --------------- Exercise 2 ---------------
# 2.1 Extract emails
emails = re.findall(r'\w+@\w+\.\w+', sample_text)
print("Emails: ", emails)

# 2.2 Extract 11-digit mobile numbers starting with 09
mobiles = re.findall(r'09\d{9}', sample_text)
print("Mobiles: ", mobiles)

# 2.3 Extract Persian-style dates (yyyy/mm/dd) & convert to dd-mm-yyyy
dates = re.findall(r'\d{4}/\d{2}/\d{2}', sample_text)
converted_dates = []
for d in dates:
    parts = d.split("/")
    new_format = f"{parts[2]}-{parts[1]}-{parts[0]}"
    converted_dates.append(new_format)

print("Original dates:", dates)
print("Converted dates:", converted_dates)

# Show replacement in text for demo
temp_text = sample_text
for old, new in zip(dates, converted_dates):
    temp_text = temp_text.replace(old, new)
print("Text with converted dates:", temp_text)

# --------------- Exercise 3 ---------------
# Replace all numbers (digits) with [NUM] except those that are part of an email address.
def mask_numbers(text):
    # step1: Find all emails and replace them with a unique placeholder
    email_pattern = r'\w+@\w+\.\w+'
    emails_found = re.findall(email_pattern, text)
    placeholder = "@@@EMAIL@@@"
    temp = text
    for email in emails_found:
        temp = temp.replace(email, placeholder)

    # Step 2: Now replace all sequences of digits with [NUM]
    masked = re.sub(r'\d+', '[NUM]', temp)

    # Step 3: Restore the original emails in place of the placeholder
    for email in emails_found:
        masked = masked.replace(placeholder, email)

    return masked


# Test
masked_text = mask_numbers(sample_text)
print("\nOriginal text:\n", sample_text)
print("\nMasked Numbers text:\n", masked_text)
