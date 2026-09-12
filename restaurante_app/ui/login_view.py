import tkinter as tk
from tkinter import ttk


class LoginView(tk.Frame):

    def __init__(self, master, restaurante_servicio, mostrar_main):
        super().__init__(master)
        self.restaurante_servicio = restaurante_servicio
        self.mostrar_main = mostrar_main
        
        self.usuario_entry = None
        self.contraseña_entry = None
        self.mensaje_error = None
        
        self.crear_interfaz()
        self.definir_estilos()
        
    def definir_estilos(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "login.TButton",
            background="#2563eb",
            foreground= "#ffffff",
            font=("Ariel", 11, "bold"),
            padding=(14, 8),
            borderwidth=0,
        )
        estilo.map("login.TButton", background=[("active", "#1d4ed8")])    
        
    def crear_interfaz(self):
        # Construye los componentes visuales del login.
        contenedor = tk.Frame(self, bg="#ffffff", padx=32, pady=28)
        contenedor.place(relx=0.5, rely=0.5, anchor="center")

        titulo = tk.Label(
            contenedor,
            text="Restaurante",
            bg="#ffffff",
            fg="#1f2a44",
            font=("Arial", 22, "bold"),
        )
        titulo.pack(pady=(0, 6))

        subtitulo = tk.Label(
            contenedor,
            text="Inicio de sesion",
            bg="#ffffff",
            fg="#516173",
            font=("Arial", 11),
        )
        subtitulo.pack(pady=(0, 22))

        tk.Label(
            contenedor,
            text="Usuario",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold"),
        ).pack(anchor="w")

        self.usuario_entry = tk.Entry(contenedor, width=30, font=("Arial", 11))
        self.usuario_entry.pack(pady=(4, 14), ipady=4)
        self.usuario_entry.focus()

        tk.Label(
            contenedor,
            text="Contrasena",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold"),
        ).pack(anchor="w")

        self.contraseña_entry = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 11),
            show="*"
        )
        
        self.contraseña_entry.pack(pady=(4, 14), ipady=4)
        self.contraseña_entry.bind("<Return>", lambda evento: self.procesar_login())

        self.mensaje_error = tk.Label(
            contenedor,
            text="",
            bg="#ffffff",
            fg="#b42318",
            font=("Arial", 10),
        )
        self.mensaje_error.pack(pady=(0, 14))

        boton = ttk.Button(
            contenedor,
            text="Iniciar sesion",
            command=self.procesar_login,
            style="Login.TButton",
        )
        boton.pack(fill="x")

    def procesar_login(self):
        
        usuario = self.usuario_entry.get().strip()
        contraseña = self.contraseña_entry.get().strip()

        if not usuario or not contraseña:
            self.mensaje_error.config(text="Ingrese usuario y contraseña.")
            return

        usuario_validado = self.restaurante_servicio.validar_acceso(usuario, contraseña)

        if usuario_validado is None:
            self.mensaje_error.config(text="Credenciales incorrectas.")
            return

        self.mensaje_error.config(text="")
        self.mostrar_main(usuario_validado)
