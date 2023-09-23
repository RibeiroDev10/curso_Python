class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor


    @property # fazendo com que um método getter, seja chamado como atributo na instancia do objeto
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta