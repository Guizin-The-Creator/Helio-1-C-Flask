from model.NotaConverter import NotaConverter

class NotaController:
    def __init__(self):
        self._nota_converter = NotaConverter()

    def validar_notas(self):
        if self._nota_converter.nota1 is None or self._nota_converter.nota2 is None:
            raise ValueError("Ambas as notas devem ser fornecidas.")

    def calcular_media(self):
        self.validar_notas()
        return self._nota_converter.calcular_media()

    # Getters e Setters
    @property
    def nota_converter(self):
        return self._nota_converter

    @nota_converter.setter
    def nota_converter(self, valor):
        self._nota_converter = valor
