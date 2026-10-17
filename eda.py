import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ml_ready_fuel_prices.csv')

sns.set_theme(style="whitegrid")

# Γράφημα 1: Πώς κατανέμονται οι τιμές συνολικά;
plt.figure(figsize=(10, 6))
sns.histplot(df['Τιμή'], bins=30, kde=True, color='royalblue')
plt.title('Κατανομή Τιμών Diesel στην Αττική', fontsize=14)
plt.xlabel('Τιμή (€)', fontsize=12)
plt.ylabel('Αριθμός Πρατηρίων', fontsize=12)
plt.show()

# Γράφημα 2: Ποια εταιρεία είναι η πιο φθηνή/ακριβή;
plt.figure(figsize=(12, 8))
avg_price_by_brand = df.groupby('Εταιρεία')['Τιμή'].mean().sort_values(ascending=False)

sns.barplot(x=avg_price_by_brand.values, y=avg_price_by_brand.index, palette='viridis')
plt.title('Μέση Τιμή Diesel ανά Εταιρεία', fontsize=14)
plt.xlabel('Μέση Τιμή (€)', fontsize=12)
plt.ylabel('Εταιρεία', fontsize=12)

plt.tight_layout() 
plt.show()

# Γράφημα 3: Απλό vs Premium Diesel
plt.figure(figsize=(8, 6))
# Φτιάχνουμε barplot που υπολογίζει αυτόματα τη μέση τιμή
sns.barplot(x='Είναι_Premium', y='Τιμή', data=df, errorbar=None, palette='coolwarm')

plt.title('Σύγκριση Τιμής: Απλό vs Premium Diesel', fontsize=14)
plt.xlabel('Είναι Premium;', fontsize=12)
plt.ylabel('Μέση Τιμή (€)', fontsize=12)
plt.xticks([0, 1], ['Όχι (Απλό)', 'Ναι (Premium)'])
plt.ylim(1.5, 2.5) # Προσαρμόζουμε τον άξονα Υ για να φαίνεται καλύτερα η διαφορά

plt.show()

# Γράφημα 4: Μέση Τιμή ανά Εταιρεία (Μόνο για Απλό Diesel)
plt.figure(figsize=(12, 7))

simple_diesel = df[df['Είναι_Premium'] == False]

avg_price_by_brand = simple_diesel.groupby('Εταιρεία')['Τιμή'].mean().sort_values(ascending=False)

sns.barplot(x=avg_price_by_brand.values, y=avg_price_by_brand.index, palette='viridis')
plt.title('Μέση Τιμή Απλού Diesel ανά Εταιρεία στην Αττική', fontsize=14)
plt.xlabel('Μέση Τιμή (€)', fontsize=12)
plt.ylabel('Εταιρεία', fontsize=12)
plt.xlim(1.8, 2.3)
plt.tight_layout()
plt.show()