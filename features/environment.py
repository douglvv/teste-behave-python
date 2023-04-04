from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def before_all(context):
    print("Começou")
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    context.driver = webdriver.Chrome(options=options)
    context.action = ActionChains(context.driver)

def before_scenario(context, scenario):
    context.driver.maximize_window()
    context.driver.implicitly_wait(15)

def after_scenario(context,scenario):
    print()


def after_all(context):  
    context.driver.quit()

