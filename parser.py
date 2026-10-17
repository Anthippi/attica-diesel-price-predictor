import pandas as pd
import re

with open('raw_data.txt', 'r', encoding='utf-8') as file:
    text = file.read()

pattern = r"Τιμή:\s*([\d,]+|---)\s*Προϊόν:\s*(.*?)\s*Σήμα:\s*(.*?)\s*Διεύθυνση:\s*(.*?)\s*Ημερ\.\s*/\s*Ώρα δήλωσης:\s*(.*?)(?=\s*Τιμή:|$)"

matches = re.findall(pattern, text, re.DOTALL)

print(f"Εντοπίστηκαν {len(matches)} πιθανές εγγραφές στο κείμενο.")

parsed_data = []


for match in matches:
    price_str = match[0].strip()
    
    if price_str == '---':
        continue
        
    try:

        clean_price = float(price_str.replace(',', '.'))
        
        parsed_data.append({
            'Τιμή': clean_price,
            'Προϊόν': match[1].strip(),
            'Εταιρεία': match[2].strip(),
            'Διεύθυνση': match[3].strip(),
            'Ημερομηνία': match[4].strip()
        })
    except ValueError:
        continue 


df = pd.DataFrame(parsed_data)

if not df.empty:
    df.to_csv('real_fuel_prices.csv', index=False, encoding='utf-8-sig')
    print(f"Επιτυχία! Αποθηκεύτηκαν {len(df)} καθαρές εγγραφές στο CSV.")
    print("\nΔείγμα δεδομένων:")
    print(df.head())
else:
    print("Αποτυχία: Δεν βρέθηκαν δεδομένα. Έλεγξε ότι το raw_data.txt έχει όντως το κείμενο μέσα.")