# Automação HDI
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
from selenium.common.exceptions import TimeoutException 

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
tempoPausaComputador.sleep(4)
meuNavegador.find_element(By.ID, "layout_7").click()

# Clicar em Relatórios Assessorias
tempoPausaComputador.sleep(4)
meuNavegador.find_element(By.XPATH, "//*[@id='item_5']/div[4]/ul/li[2]/a").click()   

# Espera até o elemento estar presente e visível
# Esperar a página carregar completamente
WebDriverWait(meuNavegador, 15).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

# Rolando para baixo na página
# Rolando para baixo em etapas
meuNavegador.execute_script("window.scrollBy(0, 300);")  # Rola 300 pixels para baixo

tempoPausaComputador.sleep(15)

try:
    # Esperar e alternar para o primeiro iframe
    iframe1 = WebDriverWait(meuNavegador, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='iframe_funcionalidade']"))
    )
    meuNavegador.switch_to.frame(iframe1)
    print("Alternado para o primeiro iframe")

    # Agora, no primeiro iframe, esperar o segundo iframe
    iframe2 = WebDriverWait(meuNavegador, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='report-container']/iframe"))
    )
    meuNavegador.switch_to.frame(iframe2)
    print("Alternado para o segundo iframe")

    paths = WebDriverWait(meuNavegador, 5).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "path"))
    )
    

    elemento = paths[64]  # Acessando o elemento pelo índice
    elemento.click()

    tempoPausaComputador.sleep(4)
    meuNavegador.find_element(By.XPATH, "//*[@id='pvExplorationHost']/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[11]/transform/div/div[3]/div/div/visual-modern/div/div/div[2]/div/div").click()
    
    

except TimeoutException as e:
    print(f"Erro ao encontrar o iframe ou o elemento path: {e}")

# Voltar ao conteúdo principal após a interação
meuNavegador.switch_to.default_content()




# Antes de qualquer coisa preciso verificar a data, se a data for diferente da data atual -1 dia, o programa deve ser fechado.
# O programa só deve rodar se a data corresponder ao dia de ontem.

# Com a data confirmada o programa deve limpar todos os filtros
# Se a data de ontem dor dia 01 o programa deve entender que ele tem que mudar o mes pro mes atual no filtro
# Após limpar os filtros e tratar as datas o programa deve adicionar o filtro do mes e ano atual




input("Pressione Enter para fechar o navegador...")
meuNavegador.quit()
