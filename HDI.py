# Automação HDI
import os
from dotenv import load_dotenv

# Importamos o Selenium para trabalhar com as paginas da web
from selenium import webdriver as opcoes_selenium_aula
from selenium.webdriver.common.keys import Keys

# Importando a biblioteca do pyautogui para trabalhar com o tempo e teclas teclado
import pyautogui as tempoPausaComputador

# Usando o By para trabalhar com as atualizações mais recentes
from selenium.webdriver.common.by import By

# Carregar variáveis do arquivo .env
load_dotenv()

# Obter as variáveis
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

# Passamos autorização ao acesso as configurações do Chrome
meuNavegador = opcoes_selenium_aula.Chrome()
meuNavegador.get("https://ssoportais3.tokiomarine.com.br/openam/XUI/?realm=TOKIOLFR&goto=http://portalparceiros.tokiomarine.com.br/group/portal-assessoria#login/")

# Aguarda 4 segundos para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

# Encontrar campo de texto de Login
meuNavegador.find_element(By.NAME, "callback_0").send_keys(login)

# Encontrar campo de texto de Password
meuNavegador.find_element(By.NAME, "callback_1").send_keys(password)

# Aguarda 4 segundos para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

# Clicar em Logar
meuNavegador.find_element(By.NAME, "callback_2").click()

# Clicar em EU, ACESSORIA!
meuNavegador.find_element(By.ID, "layout_7").click()

# Clicar em Relatórios Assessorias
meuNavegador.find_element(By.XPATH, "//*[@id=""item_5""]/div[4]/ul/li[2]/a").click()

# Antes de qualquer coisa preciso verificar a data, se a data for diferente da data atual -1 dia, o programa deve ser fechado.
# O programa só deve rodar se a data corresponder ao dia de ontem.

# Com a data confirmada o programa deve limpar todos os filtros
# Se a data de ontem dor dia 01 o programa deve entender que ele tem que mudar o mes pro mes atual no filtro
# Após limpar os filtros e tratar as datas o programa deve adicionar o filtro do mes e ano atual




input("Pressione Enter para fechar o navegador...")
meuNavegador.quit()
