from splinter import Browser
import time

cpf = '[cpf]'

for x in range(1, 999):
    with Browser('chrome') as browser:
        url = "http://2vialocacao.suprisoft.com.br/2viaAlug.ASP?SIGLA=art&ORIGEM=http://www.suprisoft.com.br&EMPRESA=Habitarte%20Neg%F3cios%20Imobili%E1riosLtda.&IMAGEMORIGEM=http://www.suprisoft.com.br/img/cliente_online/logohabit.gif"
        browser.visit(url)
        with browser.get_iframe(1) as iframe:
            iframe.find_by_xpath('//*[@id="TABLE2"]/tbody/tr/td[3]/input').first
            iframe.find_by_name('Cod_Imov').first.fill(str(x).zfill(4))
            iframe.fill('cpf', cpf)
            button = iframe.find_by_name('btnEntrar')
            button.click()
            time.sleep(1)
            if browser.is_text_not_present('Doc inexistente'):
                print("Found!")
                print(x)
            else:
                print("Not found.")