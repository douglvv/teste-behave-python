#language: pt
Funcionalidade: Salvar em csv artilheiros Brasileirão 2022
    '''
    Eu como usuário quero acessar o site do Globo Esporte, acessar a pagina de estatisticas
    do Brasileirão 2022 e salvar os artilheiros em um arquivo csv
    '''

    Cenario: Acessar o Globo Esporte
    Dado acesso a pagina inicial do Globo Esporte
    Quando clico em Menu
    E clico em Tabelas
    E clico em Nacionais
    E clico em Brasileirão série A
    E clico em Estatísticas
    E clico em Mostrar mais
    Então devo salvar os dados em um arquivo csv