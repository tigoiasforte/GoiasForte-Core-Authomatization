# Automação HDI
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# Espera para garantir que todos os iframes estão carregados
iframes = WebDriverWait(meuNavegador, 15).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "iframe"))
)

# Verifique quantos iframes foram encontrados
print(f"Total de iframes encontrados: {len(iframes)}")

# Certifique-se de que há pelo menos 2 iframes na página
if len(iframes) > 1:
    try:
        # Alterna para o primeiro iframe
        meuNavegador.switch_to.frame(iframes[0])

        # Agora, espera e alterna para o segundo iframe dentro do primeiro
        iframe2 = WebDriverWait(meuNavegador, 15).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='report-container']/iframe"))
        )

        print(f"Total de iframes encontrados segunda parte: {iframe2}")

        meuNavegador.switch_to.frame(iframe2)

        # Agora que estamos dentro do segundo iframe, podemos acessar o elemento desejado
        elemento = WebDriverWait(meuNavegador, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "fill ui-role-button-fill sub-selectable"))
        )

        # Exemplo de interação com o elemento
        print(f"Elemento encontrado: {elemento}")
     
    except Exception as e:
        print(f"Erro ao alternar para o iframe ou encontrar o elemento: {e}")
else:
    print("Não foi possível encontrar os iframes necessários na página.")

# Se necessário, você pode voltar ao contexto principal após interagir
meuNavegador.switch_to.default_content()



# Antes de qualquer coisa preciso verificar a data, se a data for diferente da data atual -1 dia, o programa deve ser fechado.
# O programa só deve rodar se a data corresponder ao dia de ontem.

# Com a data confirmada o programa deve limpar todos os filtros
# Se a data de ontem dor dia 01 o programa deve entender que ele tem que mudar o mes pro mes atual no filtro
# Após limpar os filtros e tratar as datas o programa deve adicionar o filtro do mes e ano atual




input("Pressione Enter para fechar o navegador...")
meuNavegador.quit()
