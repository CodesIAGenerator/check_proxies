import time
from tkinter import Tk, Button, messagebox, filedialog, Label, Checkbutton, IntVar
from tkinter.ttk import Progressbar
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ProxiesVerifier:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Verificar Proxies')

        self.boton_seleccionar = Button(self.ventana, text='Seleccionar archivo de proxies', command=self.verificar_proxies)
        self.boton_seleccionar.pack(pady=20)

        self.progress_bar = Progressbar(self.ventana, orient='horizontal', length=300, mode='determinate')
        self.progress_bar.pack(pady=10)

        self.time_label = Label(self.ventana, text='Tiempo restante: 0 minutos')
        self.time_label.pack()

        self.headless_var = IntVar()
        self.check_headless = Checkbutton(self.ventana, text='Hide browser', variable=self.headless_var)
        self.check_headless.pack()

        self.stop_button = Button(self.ventana, text='Detener', command=self.detener_verificacion, state='disabled')
        self.stop_button.pack(pady=10)

        self.proxies_ok = []
        self.total_proxies = 0
        self.start_time = 0
        self.stop_verification = False

    def verificar_proxy(self, proxy, use_headless):
        chrome_options = Options()
        chrome_options.add_argument('--proxy-server=http://{}'.format(proxy))

        if use_headless:
            chrome_options.add_argument('--headless')

        try:
            driver = webdriver.Chrome(options=chrome_options)
            driver.get('https://www.google.com/')
            driver.quit()
            return True
        except:
            return False

    def verificar_proxies(self):
        archivo = filedialog.askopenfilename(filetypes=[('Archivos de texto', '*.txt')])
        if archivo:
            with open(archivo, 'r') as file:
                proxies = file.read().splitlines()

            self.total_proxies = len(proxies)
            self.proxies_ok = []
            self.start_time = time.time()
            self.stop_verification = False
            use_headless = self.headless_var.get()

            self.progress_bar['maximum'] = self.total_proxies

            self.stop_button['state'] = 'normal'
            self.boton_seleccionar['state'] = 'disabled'

            for i, proxy in enumerate(proxies, start=1):
                self.progress_bar['value'] = i
                self.ventana.update()

                if self.stop_verification:
                    break

                if self.verificar_proxy(proxy, use_headless):
                    self.proxies_ok.append(proxy)

                elapsed_time = time.time() - self.start_time
                proxies_remaining = self.total_proxies - i
                time_per_proxy = elapsed_time / i if i > 0 else 0
                remaining_time = proxies_remaining * time_per_proxy

                if remaining_time >= 120:
                    remaining_time = remaining_time / 60  # Convertir a minutos
                    time_format = 'minutos'
                else:
                    time_format = 'segundos'

                self.time_label['text'] = f'Tiempo restante: {remaining_time:.1f} {time_format}'

            self.stop_button['state'] = 'disabled'
            self.boton_seleccionar['state'] = 'normal'

            if self.stop_verification:
                messagebox.showinfo('Verificación de Proxies', 'Verificación detenida por el usuario')
            elif self.proxies_ok:
                messagebox.showinfo('Proxies funcionales', f'Se encontraron {len(self.proxies_ok)} proxies funcionales.')
                messagebox.showinfo('Proxies funcionales', '\n'.join(self.proxies_ok))
            else:
                messagebox.showinfo('Proxies funcionales', 'No se encontraron proxies funcionales.')

    def detener_verificacion(self):
        self.stop_verification = True

    def iniciar(self):
        self.ventana.mainloop()

verifier = ProxiesVerifier()
verifier.iniciar()
