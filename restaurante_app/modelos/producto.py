class Producto:
    def __init__(self, codigo, nombre, categoria, precio,):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        
        
    @staticmethod
    def validar_texto(valor, campo):
        # Reutiliza una validacion basica para datos obligatorios.
        if not valor or not valor.strip():
            raise ValueError(f"El campo {campo} no puede estar vacio.")

        return valor.strip()

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = self.validar_texto(valor, "codigo")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = self.validar_texto(valor, "nombre")

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        self._categoria = self.validar_texto(valor, "categoria")
        
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, valor):
        try:
            valor_float = float(valor)
            if valor_float < 0:
                raise ValueError("El precio no puede ser negativo")
            self._precio = valor_float
        except (ValueError, TypeError):
            raise ValueError("El precio debe ser un numero válido")    
        
            