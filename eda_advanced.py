import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ml_ready_fuel_prices.csv')

df['Τύπος_Εταιρείας'] = df['Εταιρεία'].apply(lambda x: 'ΑΝΕΞΑΡΤΗΤΟ' if 'ΑΝΕΞΑΡΤΗΤΟ' in str(x).upper() else 'ΜΕΓΑΛΗ/ΠΟΛΥΕΘΝΙΚΗ')

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
sns.set_theme(style="whitegrid")

df_areas = df[df['Περιοχή'] != 'ΑΓΝΩΣΤΟ']
area_prices = df_areas.groupby('Περιοχή')['Τιμή'].mean().sort_values()
top_bottom_areas = pd.concat([area_prices.head(5), area_prices.tail(5)])
sns.barplot(x=top_bottom_areas.values, y=top_bottom_areas.index, ax=axes[0,0], palette="coolwarm")
axes[0,0].set_title("Οι 5 Φθηνότερες vs 5 Ακριβότερες Περιοχές")
axes[0,0].set_xlim(1.8, 2.3)


sns.boxplot(x='Σε_Λεωφόρο', y='Τιμή', data=df, ax=axes[0,1], palette="Set2")
axes[0,1].set_title("Τιμές: Συνοικιακά vs Σε Λεωφόρο")
axes[0,1].set_xticklabels(['Όχι (Συνοικιακό)', 'Ναι (Λεωφόρος)'])


sns.boxplot(x='Τύπος_Εταιρείας', y='Τιμή', data=df, ax=axes[1,0], palette="Pastel1")
axes[1,0].set_title("Διακύμανση: Ανεξάρτητα vs Μεγάλα Σήματα")


day_order = ['Δευ', 'Τρι', 'Τετ', 'Πεμ', 'Παρ', 'Σαβ', 'Κυρ']
df_days = df[df['Ημέρα'].isin(day_order)]
sns.pointplot(x='Ημέρα', y='Τιμή', data=df_days, order=day_order, ax=axes[1,1], color='purple')
axes[1,1].set_title("Διακύμανση Μέσης Τιμής μέσα στην Εβδομάδα")

plt.tight_layout()
plt.show()