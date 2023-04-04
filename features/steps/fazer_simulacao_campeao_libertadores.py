#--------------------- IMPORTS ---------------------------------
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup #pip install bs4
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #importa e cria o objeto EC
import time
from csv import writer
#----------------------------------------------------------------

#---------------------------------------------------------------------
#AÇÕES REPETIDAS DE OUTRO STEP NÃO PRECISA SER IMPLEMENTADO NOVAMENTE
#   Dado acesso a pagina inicial do Globo Esporte
#   Quando clico em Menu
#--------------------------------------------------------------------


@when(u'clico em Libertadores')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'libertadores')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)

@when(u'clico em Simulador')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'simulador')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)

@when(u'clico em Athletico-PR')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id15"]')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)

@when(u'clico em Fortaleza')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="img17"]')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)

@when(u'clico em Palmeiras')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="img20"]')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)

@when(u'clico em Atlético-MG')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="img22"]')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)

@when(u'clico em Deportes Tolima')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="img23"]')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)

@when(u'clico em Corinthians')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="img25"]')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)

@when(u'clico em Colón')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="img28"]')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)

@when(u'clico em River Plate')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="img30"]')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)

@when(u'clico em Athletico-PR 2')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.ID,'id7')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)

@when(u'clico em Palmeiras 2')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.ID,'id9')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)

@when(u'clico em Corinthians 2')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.ID,'id12')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)

@when(u'clico em Colón 2')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.ID,'id13')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)

@when(u'clico em Athletico-PR 3')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.ID,'id3')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)

@when(u'clico em Corinthians 3')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.ID,'id5')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)

@when(u'clico em Athletico-PR 4')
def step_impl(context):
    menu = WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.ID,'id1')))
    context.action.move_to_element(menu).click().perform()
    time.sleep(1)


@then(u'devo salvar uma screenshot da simulação')
def step_impl(context):
    context.driver.save_screenshot('resultado.png')

