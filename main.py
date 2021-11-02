import os
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

lets_go = True
while lets_go == True:
    browser = webdriver.Chrome('/Users/zeynep/Downloads/chromedriver')
    browser.get('https://sede.administracionespublicas.gob.es/something/')

    police = browser.find_element_by_id('tramiteGrupo[0]')
    drop = Select(police)
    drop.select_by_value('4000')
    time.sleep(2)
    aceptar = browser.find_element_by_id('btnAceptar')
    aceptar.click()
    time.sleep(2)

    browser.execute_script('window.scrollBy(0,1000)', '')
    entrar = browser.find_element_by_id('btnEntrar')
    entrar.click()
    time.sleep(2)

    #radioButton
    browser.find_element_by_id('rdbTipoDocPas').click()
    time.sleep(2)
    passport = browser.find_element_by_id('txtIdCitado')
    passport.send_keys('EXXXXXXXX')
    time.sleep(2)
    name = browser.find_element_by_id('txtDesCitado')
    name.send_keys('NAME SURNAME')
    time.sleep(2)
    browser.execute_script('window.scrollBy(0,1000)', '')
    enviar = browser.find_element_by_id('btnEnviar')
    enviar.click()
    time.sleep(2)

    solicitarCita = browser.find_element_by_id('btnEnviar')
    solicitarCita.click()

    no_appointments = browser.page_source.find('En este momento no hay citas disponibles.')

    time.sleep(2)

    if no_appointments:
        browser.close()
        time.sleep(20)

    else:
        os.system("say 'Hey, appointments are available'")
        time.sleep(1)
        os.system("say 'Hey, appointments are available'")
        time.sleep(1)
        os.system("say 'Hey, appointments are available'")
        time.sleep(1)
        os.system("say 'Hey, appointments are available'")
        lets_go = False





