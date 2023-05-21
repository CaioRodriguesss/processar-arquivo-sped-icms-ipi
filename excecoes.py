##### CONJUNTO DE CLASSES DERIVADAS DA CLASSE EXCEPTION INERENTES AO PROGRAMA #####

# Excessão lançada ao tentar processar sem nenhum arquivo selecionado.
class NenhumArquivoSelecionado(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        print(self.msg)

# Excessão lançada ao tentar processar um arquivo .TXT que não é um arquivo SPED.
class NaoEumArquivoSpedValido(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        print(self.msg)

# Excessão lançada ao tentar processar um arquivo SPED com o programa sem o código de autenticação.
class ArquivoNaoAutenticado(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        print(self.msg)

# Excessão lançada ao tentar validar uma senha que não coincide com o código hash da senha armazenado no banco para o mês atual.
class SenhaDiferenteDoHash(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        print(self.msg)

# Execessão lançada ao tentar validar uma senha em branco
class SenhaEmBranco(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        print(self.msg)

# Excessão para ser lançada caso o mês e o ano atual estejam menores do que o mês e o ano do último processamento.
class MesOuAnoMenoresDoQueUltimoProcessamento(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        print(self.msg)
