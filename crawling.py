import requests
from bs4 import BeautifulSoup

url = 'https://www.fuelprices.gr/'

response = requests.get(url)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')
     
    links = soup.find_all('a')
    
    print(f"Βρέθηκαν {len(links)} σύνδεσμοι στη σελίδα.")
    
    for link in links:
        print(link.text.strip(), "->", link.get('href'))
        
else:
    print(f"Αποτυχία σύνδεσης. Κωδικός λάθους: {response.status_code}")