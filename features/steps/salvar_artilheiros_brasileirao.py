# --------------------- IMPORTS ---------------------------------
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup  # pip install bs4
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # importa e cria o objeto EC
import time
from csv import writer
# ----------------------------------------------------------------

url = 'https://ge.globo.com/'

@given(u'acesso a pagina inicial do Globo Esporte')
def step_impl(context):
    context.driver.get(url)
    time.sleep(2)


@when(u'clico em Menu')
def step_impl(context):
    menu = WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="header-produto"]/div[2]/div/div/div[1]/div')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)


@when(u'clico em Tabelas')
def step_impl(context):
    menu = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'tabelas')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)


@when(u'clico em Nacionais')
def step_impl(context):
    menu = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'nacionais')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)


@when(u'clico em Brasileirão série A')
def step_impl(context):
    menu = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'brasileirão série a')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)


@when(u'clico em Estatísticas')
def step_impl(context):
    menu = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'estatísticas')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)


@when(u'clico em Mostrar mais')
def step_impl(context):
    menu = WebDriverWait(context.driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/main/div[3]/div/section[1]/ul/li[1]/section/button')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)


@then(u'devo salvar os dados em um arquivo csv')
def step_impl(context):
    tabela = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/main/div[3]/div/section[1]/ul/li[1]/section/div[2]/div[2]/div')))
    # salva apenas o outerHTML da tabela
    conteudo_html = tabela.get_attribute('outerHTML')
    # converte lista para HTML
    lista = BeautifulSoup(conteudo_html, 'html.parser')

    # Cria o arquivo csv com a lista de artilheiros
    with open('lista_artilheiros.csv', 'w') as arquivo:
        for dados in lista.find_all('figcaption', {'class': 'ranking__celula ranking__celula--figure'}):
            linha = ''
            # encontra o jogador
            for nome in dados.find_all('div', {'class': 'ranking__nome'}):
                linha = nome.text.replace('\n', "")
            # encontra a posicao
            for posicao in dados.find_all('div', {'class': 'ranking__posicao'}):
                linha += '\t'+posicao.text.replace('\n', "")
            # encontra o nº de jogos
            for jogos in dados.find_all('div', {'class': 'ranking__results--item ranking__results--jogos'}):
                linha += '\t'+jogos.text.replace('Jogos:', "")
            # encontra o nº de gols
            for gols in dados.find_all('div', {'class': 'ranking__results--item ranking__results--total'}):
                linha += '\t'+gols.text
            print(linha)
            # escreve os dados armazenados em linha e pula para a próxima linha
            arquivo.write(linha+'\n')
    arquivo.close()
