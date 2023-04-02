from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep 
import json
import os


class autentique:
    def iniciar(self):
        self.senha()
        self.configuracoes_selenium()
        self.autentique_login()
        self.autentique_navegar()
        pass
    def senha(self):
        with open("login_autentique.json", encoding='utf-8') as meu_json: # Importar dados de um arquivo config com usernames e passwords
            dados = json.load(meu_json)
            self.email = dados["email"]
            self.senha = dados["password"]
            print('Dados do settings.json lidos com sucesso!')

    def configuracoes_selenium(self):

        options = webdriver.ChromeOptions()

        # options.add_argument('--disable-gpu')
        # options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--start-maximized')
        # options.add_argument('--disable-setuid-sandbox')


        preferences = {"download.default_directory" : f'{os.getcwd()}\\relatorios', 'profile.default_content_setting_values.automatic_downloads': 1}
        options.add_experimental_option("prefs", preferences)
        servico = Service(ChromeDriverManager().install())
        self.navegar = webdriver.Chrome(service=servico, chrome_options=options)
    def autentique_login(self):
        pagina = self.navegar
        pagina.get('https://painel.autentique.com.br/entrar')
        sleep(5)
        pagina.find_element('xpath',' /html/body/app-root/app-auth-login/app-auth-container/div/div/form/label[1]/input' ).send_keys(self.email)
        pagina.find_element('xpath',' /html/body/app-root/app-auth-login/app-auth-container/div/div/form/label[2]/input' ).send_keys(self.senha)
        pagina.find_element('xpath',' /html/body/app-root/app-auth-login/app-auth-container/div/div/form/div/button' ).click()
        sleep(5)
    def autentique_navegar(self):
        pagina = self.navegar
        pagina.find_element('xpath', '/html/body/app-root/app-documents-home/app-documents-list/div[1]/app-taxonomy/aside/app-documents-taxonomy/div[1]/button').click()
        sleep(4)
        pagina.find_element('xpath', '/html/body/app-root/app-documents-new/div/section/div[4]/div[2]/div/div[2]').click()
        sleep(5)

start = autentique()
start.iniciar()