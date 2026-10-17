import pandas as pd


df = pd.read_csv('cleaned_fuel_prices.csv')

df['Ώρα'] = df['Ημερομηνία'].str.split(' ').str[1].str.split(':').str[0].astype(int)

def extract_municipality(address):
    if '-' in address:
        area = address.split('-')[-1].strip()
    else:
        area = address.split(' ')[-1].strip()
        
    if area.isdigit():
        return "ΑΓΝΩΣΤΟ"
    return area

df['Περιοχή'] = df['Διεύθυνση'].apply(extract_municipality)

premium_keywords = 'V-Power|Ultimate|Avio|ACTION|Crystal|xtra4|D-FORCE|Evo'

df['Είναι_Premium'] = df['Προϊόν'].str.contains(premium_keywords, case=False, na=False)

df['Ημέρα'] = df['Ημερομηνία'].str.split(',').str[0]

highway_keywords = 'ΛΕΩΦ|Λ\.|Ε\.Ο\.|ΧΛΜ'
df['Σε_Λεωφόρο'] = df['Διεύθυνση'].str.contains(highway_keywords, case=False, na=False)

df.to_csv('ml_ready_fuel_prices.csv', index=False, encoding='utf-8-sig')

print("Η Μηχανική Χαρακτηριστικών ολοκληρώθηκε!\n")
print("Δείγμα των νέων στηλών:")
print(df[['Διεύθυνση', 'Περιοχή', 'Ημερομηνία', 'Ώρα']].head(10))