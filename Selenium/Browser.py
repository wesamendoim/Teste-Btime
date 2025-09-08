from selenium import webdriver#Variavel que fará toda a interação com o Selenium

try:
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

except Exception as e:
    print(e)
