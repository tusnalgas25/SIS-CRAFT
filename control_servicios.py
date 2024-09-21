import tkinter as tk
import subprocess
import os
import time
import webbrowser

# Ruta a XAMPP (ajusta la ruta si está en otro lugar)
xampp_path = 'C:/xampp/'

# Funciones para manejar los servicios de XAMPP
def start_xampp_service(service):
    if service == 'Apache':
        subprocess.run([xampp_path + 'xampp_start.exe'])
    elif service == 'MySQL':
        subprocess.run([xampp_path + 'mysql_start.bat'])

def stop_xampp_service(service):
    if service == 'Apache':
        subprocess.run([xampp_path + 'xampp_stop.exe'])
    elif service == 'MySQL':
        subprocess.run([xampp_path + 'mysql_stop.bat'])

# Función para ejecutar PHP Artisan Serve y NPM Run Dev
def run_php_artisan_npm():
    # Cambia el directorio al proyecto Laravel
    os.chdir('C:/xampp/htdocs/gestion-soporte')

    # Iniciar el servidor Laravel con Artisan
    subprocess.Popen(['php', 'artisan', 'serve'])

    # Iniciar npm run dev en un proceso separado
    subprocess.Popen(['npm', 'run', 'dev'])

    # Esperar 10 segundos antes de abrir el navegador
    time.sleep(10)

    # Abrir el navegador en la dirección 127.0.0.1:8000
    webbrowser.open('http://127.0.0.1:8000')

# Crear la ventana principal para controlar XAMPP
def xampp_control_window():
    xampp_window = tk.Tk()
    xampp_window.title("Control de Servicios XAMPP")
    
    tk.Label(xampp_window, text="Control de Apache y MySQL en XAMPP").pack()
    tk.Button(xampp_window, text="Iniciar Apache y MySQL", command=lambda: start_xampp_service('Apache')).pack(pady=5)
    tk.Button(xampp_window, text="Detener Apache y MySQL", command=lambda: stop_xampp_service('Apache')).pack(pady=5)
    
    xampp_window.mainloop()

# Crear la ventana para ejecutar PHP Artisan Serve y NPM Run Dev
def artisan_serve_window():
    artisan_window = tk.Tk()
    artisan_window.title("PHP Artisan Serve y NPM Run Dev")

    tk.Button(artisan_window, text="Ejecutar PHP Artisan Serve y NPM Run Dev", command=run_php_artisan_npm).pack(pady=5)

    artisan_window.mainloop()

# Crear la ventana de control principal
root = tk.Tk()
root.title("Control de Sistema Laravel")

tk.Button(root, text="Abrir Control de XAMPP", command=xampp_control_window).pack(pady=10)
tk.Button(root, text="Abrir PHP Artisan Serve y NPM Run Dev", command=artisan_serve_window).pack(pady=10)

root.mainloop()
