from romanas import arabigo_a_romano, romano_a_arabigo, RomanError

class RomanNumber():
    def __init__(self, entrada):
        if isinstance(entrada, str):
            self.arabigo = romano_a_arabigo(entrada)
            self.romano = entrada
        elif isinstance(entrada, int):
            self.romano = arabigo_a_romano(entrada)
            self.arabigo = entrada
        else:
            raise TypeError('La entrada tienes que ser entero')
        
        