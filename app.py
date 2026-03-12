import re
import PyPDF2
import streamlit as s

s.title("PDF DATA  extractor")


upload_file = s.file_uploader("Upload File", type = ["pdf"])

options= s.multiselect("select data to extract",["phone number","OTP","Pincode","Money","Country"])

if upload_file:
    pdf_reader = PyPDF2.PdfReader(upload_file)

    text = ""
    for page in pdf_reader.pages:
        text = text+page.extract_text()

    results = {}

    if "phone number" in options:
        phone_pattern = r'\+?\d{10,13}'
        results["phone numbers"] = re.findall(phone_pattern,text)

    if "OTP" in options:
        otp_pattern = r'\b\d{4,6}\b'
        results["OTP"] = re.findall(otp_pattern,text)
    if "Pincode" in options:
        pincode_pattern = r'\b\d{6}\b'
        results ["pincode"] = re.findall(pincode_pattern,text)
    if "Money" in options:
        money_pattern = r'#\s?\d+|\$\s?\d+'
        results["money"] = re.findall(money_pattern,text)

    if "Country" in options:
        countries = ["India","USA","Germany","France","Japan"]
        found = [c for c in countries if c in text]
        results["Countries"] = found
    s.write(results)






