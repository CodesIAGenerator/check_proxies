# Proxies Verifier

Proxies Verifier es una herramienta que te permite verificar la funcionalidad de proxies almacenados en un archivo de texto. Puedes seleccionar el archivo de proxies, elegir si deseas utilizar el modo headless para ocultar el navegador y ver el progreso de verificación mediante una barra de progreso.

## Requisitos

- Python 3.x
- Bibliotecas Python: tkinter, selenium

## Instalación

1. Clona o descarga este repositorio en tu máquina.

2. Instala las bibliotecas requeridas:

```shell
pip install tkinter selenium
```

# Version GUI

1. Ejecuta el archivo con el siguiente comando

```
python check_proxies_gui.py
```

2. Elige el archivos de proxies que debe tener el siguiente formato (IP:PUERTO)

```
192.x.1.1:80
186.x.3.4:8080
```

3. Marca la casilla "Modo headless" si deseas que el navegador se ejecute en modo oculto (opcional).

4. Haz clic en el botón "Verificar proxies" para iniciar el proceso de verificación.

5. Se mostrará una barra de progreso y el tiempo estimado restante.

6. Puedes hacer clic en el botón "Detener" para interrumpir el proceso de verificación en cualquier momento.

7. Una vez finalizada la verificación, se mostrará un mensaje con el número de proxies funcionales encontradas.
   
