from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    
import time
import pandas as pd

#Variavel que fará toda a interação com o Selenium
def driverBrowser(driver):
    match driver:
        case "chrome":
            driver = webdriver.Chrome()
        case "firefox":
            driver = webdriver.Firefox()   
        case "edge":
            driver = webdriver.Edge()   
        case _:
            print("Navegador não suportado")
    return driver

try:
    #Utitlizar o Edge pois é padrão do Windows
    driver = driverBrowser("edge")

    #Abrindo de teste o Google
    driver.get("https://www.espn.com.br/")

    #Colocando a janela em tela cheia
    driver.maximize_window()

    #Esperar a pagina carregar
    driver.implicitly_wait(20) #Esperar 20 segundos para carregar a página

    #Esperar o elemento estar presente na página
    WebDriverWait(driver, 10).until(EC.presence_2of_element_located((By.XPATH, '/html/body/div[5]/section/section/div/section[1]/article[2]/div/ul/li[3]/a')))   

 # Clicar no link do Brasileirão
    link_brasileirao = driver.find_element(By.XPATH, '/html/body/div[5]/section/section/div/section[1]/article[2]/div/ul/li[3]/a')
    if link_brasileirao.is_displayed():
        link_brasileirao.click()
        time.sleep(10)  # esperar carregar

    tabela_brasileirao = driver.find_element(By.XPATH, '/html/body/div[5]/section/section/div/section[2]/article/footer/a')
    if tabela_brasileirao.is_displayed():
        tabela_brasileirao.click()  
        time.sleep(10)  # esperar carregar

    tabela_completa = driver.find_element(By.XPATH, '//*[@id="fittPageContainer"]/div[2]/div[2]/div/div/section/div/section/section/div[1]/div')
    if tabela_completa.is_displayed():
        tabela_completa.click()
        time.sleep(15)

    #Capturando o HTML todo da pagina
    html = driver.page_source
    #Lendo o conteudo da pagina com pandas
    tables = pd.read_html(html)
    #juntando as tabelas capturadas
    df = pd.concat([tables[0], tables[1]], axis=1)
    print(df)
    #Gravando a tabela em CSV   
    df.to_csv("Excel(arquivocsv)\\tabela_brasileirao_V1.csv", index=False, sep=";", encoding="utf-8-sig")

except Exception as e:
    print("Erro ao encontrar o elemento: ", e)
finally:
    #Fechar o navegador
    driver.quit()