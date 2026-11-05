import json
import os
import keyboard
import time

red = "\033[091m"
green = "\033[092m"
yellow = "\033[093m"
blue = "\033[094m"
reset = "\033[0m"

FILENAME = "personal_financial_records.json"

def load_records(records):
    if os.path.exists(FILENAME):
        if os.path.getsize(FILENAME) > 0:
            with open(FILENAME, "r", encoding="utf-8") as f:
                return json.load(f)
            
def save_records(records):
    with open(FILENAME, "w", encoding="utf-8") as f:
        return json.dump(records, f, ensure_ascii=False, indent=4)

records = []

while True:
    os.system("cls")
    print("==== EXPENSE TRACKER ====")
    print("1. Enter a record")
    print("=" * 28)