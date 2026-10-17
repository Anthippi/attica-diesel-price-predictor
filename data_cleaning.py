import pandas as pd


df = pd.read_csv('real_fuel_prices.csv')

df['Διεύθυνση'] = df['Διεύθυνση'].str.split('\n').str[0].str.strip()

df['Ημερομηνία'] = df['Ημερομηνία'].str.split(',').str[-1].str.strip()

df = df.drop_duplicates()

df.to_csv('cleaned_fuel_prices.csv', index=False, encoding='utf-8-sig')

print(f"Έμειναν {len(df)} μοναδικές και καθαρές εγγραφές.")
print("Δείτε το τελικό αποτέλεσμα:")
print(df.head())