#funcao de outro py que abre o whats
#parte comum nos dois códigos, no salva_contatos.py e no salva_conversas.py
from whatsapp_api import WhatsApp
from time import sleep

wp = WhatsApp()
# sleep(20)
print("clique para contnuar")
input()
print("entrou")


#cria contato.txt
with open('contatos.txt','w',encoding='utf-8') as contatos: pass

def salvaUsers():
    all_users = []
    eula = wp.driver.find_elements_by_xpath("//*[@id='pane-side']") 
    for scrl in range(0,1000*10,2500):
        wp.driver.execute_script(f'arguments[0].scrollTop = {scrl}', eula[0])
        usuarios = wp.driver.find_elements_by_class_name('_3Dr46')
        sleep(3)
        try:
            for user in usuarios:
                # print(user.text)
                if user.text in all_users: continue
                all_users.append(user.text)
                with open('contatos.txt','a+',encoding='utf-8') as contatos: 
                    contatos.write(user.text)
                    contatos.write(',\n')
        except:pass

salvaUsers()
wp.driver.quit()