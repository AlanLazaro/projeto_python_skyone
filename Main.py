class Pessoa:
    def __init__(self, nome, fone):
        self.nome = nome
        self.fone = fone

    def exibir(self):
        print(f'-> {self.nome} - {self.fone}')

class Colaborador(Pessoa):
    def __init__(self, nome, fone, squad=None):
        super().__init__(nome, fone)
        self.squad = squad

    def incluir_squad(self, squad):
        self.squad =squad

class Dev(Colaborador):
    def __init__(self, nome, fone, cargo, squad=None):
        super().__init__(nome, fone, squad)
        self.cargo = cargo

    def exibir(self):
        super().exibir()
        print(f'Cargo de {self.cargo} na squad {self.squad.nome}\n')

class Squad:
    def __init__(self, nome, techlead=None, devs=None):
        self.nome = nome
        self.devs = []
        self.techlead = techlead

    def incluir_dev(self, dev):
        self.devs.append(dev)

    def incluir_techlead(self, techlead):
       self.techlead = techlead

print('\n'+'-='*5 + ' Sky.One Solutions ' + '-='*5)
print('Bem vindo ao sistema de cadastro de squads!\n')

squads = []
while True:

    nome_squad = input('\nNome da Squad: ')
    nome_techlead = input('Nome do teachlead da Squad: ')
    fone_techlead = input('Telefone do techlead: ')

    squad = Squad(nome_squad)
    techlead = Colaborador(nome_techlead, fone_techlead)
    squad.incluir_techlead(techlead)
    techlead.incluir_squad(squad)

    squads.append(squad)

    while True:
        nome_dev = input('\nNome do desenvolvedor: ')
        fone_dev = input('Telefone do desenvolvedor: ')
        cargo_dev = input('Cargo do desenvolvedor: ')

        dev = Dev(nome_dev, fone_dev, cargo_dev)
        dev.incluir_squad(squad)

        squad.incluir_dev(dev)

        option = input('\nDeseja adicionar mais uma Desenvolvedor [S/N]: ')
        if option in 'Nn':
            break

    option = input('\nDeseja adicionar mais uma squad [S/N]: ')
    if option in 'Nn':
        break

for squad in squads:
    print('\n'+'.'*17 + squad.nome + '.'*17)
    print(f'TechLead: {squad.techlead.nome}')
    print('\n        ----- Devs do Squad -----')

    for dev in squad.devs:
        dev.exibir()
    print('.'*17 + squad.nome + '.'*17)

print('-='*5 + ' Sky.One Solutions ' + '-='*5)