import json
import os

red = "\033[091m"
green = "\033[092m"
yellow = "\033[093m"
blue = "\033[094m"
reset = "\033[0m"

FILENAME = "personal_financial_records.json"

def load_records():
    if os.path.exists(FILENAME):
        if os.path.getsize(FILENAME) > 0:
            with open(FILENAME, "r", encoding="utf-8") as f:
                return json.load(f)
    return []
            
def save_records(records):
    with open(FILENAME, "w", encoding="utf-8") as f:
        return json.dump(records, f, ensure_ascii=False, indent=4)

records = load_records()

while True:
    os.system("cls")
    
    print("==== EXPENSE TRACKER ====")
    print("1. Enter a record")
    print("=" * 28)
    
    choice = input("Enter the function you want to use: ").strip()
    
    if choice == '1':
        while True:
            date = input("Enter the date you buy this item: ")
            
            if not date:
                print(f"{red}Input cannot be blank!{reset}")
                continue
            
            elif date.isdigit() and len(date) == 4:
                day = int(date[2:])
                month = date[:2]
                
                days_in_month = {
                    "01": 31, "02": 28, "03": 31, "04": 30,
                    "05": 31, "06": 30, "07": 31, "08": 31,
                    "09": 30, "10": 31, "11": 30, "12": 31
                }
                
                if month in days_in_month:
                    max_day = days_in_month[month]
                    
                    if 1 <= day <= max_day:
                        break
                    
                    else:
                        print(f"{red}Invalid day!{reset}")
                        continue
                else:
                    print(f"{red}Invalid month!{reset}")
                    continue
            else:
                print(f"{red}Invalid format! Please enter exactly 4 digits.{reset}")
                continue
               
        while True:
            item = input("Enter item you purchased: ").strip()
            
            if not item:
                print(f"{red}Input cannot be blank!{reset}")
                continue
            
            elif item.isalpha():
                break
            
            else:
                print(f"{red}Please enter a valid word!{reset}")
                
        while True:
            expense = input("Enter your expense: ").strip()
            
            if not expense:
                print(f"{red}Input cannot be blank!{reset}")
                
            elif expense.isdigit():
                break
            
            else:
                print(f"{red}Please enter a valid number!{reset}")
                continue
        
        r = {}
        r['date'] = date
        r['item'] = item
        r['expense'] = expense
        records.append(r)
        
        save_records(records)