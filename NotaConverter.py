class NotaConverter:
    def __init__(self):
        self._nota1 = None
        self._nota2 = None

    # Método para calcular a média das notas
    def calcular_media(self):
        if self._nota1 is not None and self._nota2 is not None:
            return (self._nota1 + self._nota2) / 2
        else:
            return None

    # Getters e Setters para as notas
    @property
    def nota1(self):
        return self._nota1

    @nota1.setter
    def nota1(self, value):
        if value < 0 or value > 10:
            raise ValueError("A nota deve estar entre 0 e 10.")
        self._nota1 = value

    @property
    def nota2(self):
        return self._nota2

    @nota2.setter
    def nota2(self, value):
        if value < 0 or value > 10:
            raise ValueError("A nota deve estar entre 0 e 10.")
        self._nota2 = value
