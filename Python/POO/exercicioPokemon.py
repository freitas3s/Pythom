class Pokemon:
    def __init__(self, nome, fome=0, idade=0, saude=100) -> None:
        self._nome = nome
        self._fome = fome
        self._idade = idade
        self._saude = saude

    def alterar_nome(self, novo_nome):
        self._nome = novo_nome
        print(f'novo nome: {self._nome}')
        return

    def mostrar_status(self):
        print(f'{self._nome}')
        print(f'fome: {self._fome}')
        print(f'saúde: {self._saude}')
        return

    def humor(self):
        fome = self._fome
        saude = self._saude
        if fome <= 25:
            print('estou sem fome')
        if fome > 25 and fome <= 50:
            print('estou com fome')
        if fome > 50 and fome <= 75:
            print('estou com muita fome!!!')
        if fome > 75:
            print('estou faminto')

        if saude >= 75:
            print('e muito saudável ')
        if saude > 25 and saude <= 50:
            print('e saudável')
        if saude > 50 and saude <= 75:
            print('e doente')
        if saude < 75:
            print('e morrendo!!!')
