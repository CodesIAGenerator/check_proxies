from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def verificar_proxy(proxy):
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=http://{}'.format(proxy))

    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.google.com/')
        driver.quit()
        return True
    except:
        return False

# Leer proxies desde el archivo
with open('http_proxies.txt', 'r') as file:
    proxies = file.read().splitlines()

proxies_ok = []

# Verificar las proxies
for proxy in proxies:
    if verificar_proxy(proxy):
        proxies_ok.append(proxy)

# Imprimir las proxies funcionales en el archivo 'proxies_ok.txt'
with open('proxies_ok.txt', 'w') as file:
    for proxy in proxies_ok:
        file.write(proxy + '\n')

print('Proxies funcionales guardadas en proxies_ok.txt')
