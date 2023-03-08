from core import Aniversariante

# Modelo de estrutura para mandar para o banco:
# aniversariante = Aniversariante(nome='', departamento='', data_nascimento='1990, 1, 1')

aniversariante = [
    Aniversariante(nome='Jose Cesar Coelho', departamento='Centro de Distribuição', data_nascimento='1982, 3, 1'),
    Aniversariante(nome='Paulo Henrique Cirqueira', departamento='Centro de Distribuição', data_nascimento='1982, 3, 3'),
    Aniversariante(nome='Josineide de Almeira Davila', departamento='Centro de Distribuição', data_nascimento='1982, 3, 4'),
    Aniversariante(nome='Regina Rosa Lemes dos Santos', departamento='Zeladoria Escritório', data_nascimento='1982, 3, 5'),
    Aniversariante(nome='Thiago Silva Abrantes', departamento='Gerência Geral', data_nascimento='1982, 3, 10'),
    Aniversariante(nome='Gabriel dos Santos', departamento='Produção Massa', data_nascimento='1982, 3, 10'),
    Aniversariante(nome='Givailson Neves de Almeida', departamento='Produção Textura', data_nascimento='1982, 3, 13'),
    Aniversariante(nome='Benedito Barbosa de Sousa', departamento='Transporte', data_nascimento='1982, 3, 14'),
    Aniversariante(nome='Hanna Layres Lameira Oliveira', departamento='Centro de Distribuição', data_nascimento='1982, 3, 19'),
    Aniversariante(nome='João Pedro de Amora Teixeira', departamento='Comercial', data_nascimento='1982, 3, 19'),
    Aniversariante(nome='Josan Jesuis da Silva', departamento='Transporte', data_nascimento='1982, 3, 19'),
    Aniversariante(nome='Bruno Lindoso Amorim', departamento='Produção Tinta', data_nascimento='1982, 3, 20'),
    Aniversariante(nome='William Pereira dos Santos Caetano', departamento='Produção Massa', data_nascimento='1982, 3, 20'),
    Aniversariante(nome='Antônio Paulo Santos Macedo', departamento='Produção Massa', data_nascimento='1982, 3, 23'),
    Aniversariante(nome='Wictor Xavier Alves dos Santos', departamento='Produção', data_nascimento='1982, 3, 24'),
    Aniversariante(nome='Leandro José Carneiro', departamento='Produção Massa', data_nascimento='1982, 3, 27'),
    Aniversariante(nome='Raimundo de Sousa da Silva Dias', departamento='Produção', data_nascimento='1982, 3, 27'),
    Aniversariante(nome='Abelardo Augusto Nobre de Araújo', departamento='Tecnologia Informação', data_nascimento='1982, 3, 28'),
    Aniversariante(nome='Andrew Vinicius Duarte Ferrari', departamento='Centro de Distribuição', data_nascimento='1982, 3, 28'),
    Aniversariante(nome='Eduardo Francisco Dutra', departamento='Gerência Produção', data_nascimento='1982, 3, 28'),
    Aniversariante(nome='Orneide Lopes Lima', departamento='Centro Distribuição', data_nascimento='1982, 3, 30'),
]

Aniversariante.objects.bulk_create(aniversariante)