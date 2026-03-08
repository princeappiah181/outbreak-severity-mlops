import re
import numpy as np

HIGH_RISK_PHRASES = [
    "international spread",
    "public health emergency",
    "rapid increase",
    "serious public health risk",
]

def extract_death_count(text: str) -> int:
    text = text.lower()
    match = re.search(r"(\d+)\s+deaths?", text)
    return int(match.group(1)) if match else 0

def extract_case_count(text: str) -> int:
    text = text.lower()
    match = re.search(r"(\d+)\s+cases?", text)
    return int(match.group(1)) if match else 0

def extract_phrase_flag(text: str) -> int:
    text = text.lower()
    return int(any(phrase in text for phrase in HIGH_RISK_PHRASES))

def extract_structured_features(text: str):
    death_count = extract_death_count(text)
    case_count = extract_case_count(text)
    phrase_flag = extract_phrase_flag(text)

    log_deaths = float(np.log1p(death_count))
    log_cases = float(np.log1p(case_count))

    return [log_deaths, log_cases, phrase_flag]