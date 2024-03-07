import time

def identificar_interruptores():
    # Ligue o primeiro interruptor
    print("Ligando o primeiro interruptor...")
    time.sleep(2)  # Espera 2 segundos (simulando tempo de espera)
    
    # Desligue o primeiro interruptor e ligue o segundo interruptor
    print("Desligando o primeiro interruptor e ligando o segundo interruptor...")
    time.sleep(2)  # Espera 2 segundos (simulando tempo de espera)
    
    # Verifique o estado das lâmpadas
    estado_lampada1 = input("A lâmpada 1 está acesa? (s/n): ")
    estado_lampada2 = input("A lâmpada 2 está acesa? (s/n): ")
    estado_lampada3 = input("A lâmpada 3 está acesa? (s/n): ")
    
    # Determine qual interruptor controla cada lâmpada
    if estado_lampada1 == "s":
        print("O primeiro interruptor controla a lâmpada 1.")
    elif estado_lampada2 == "s":
        print("O segundo interruptor controla a lâmpada 1.")
    else:
        print("O terceiro interruptor controla a lâmpada 1.")
        
    if estado_lampada2 == "s":
        print("O segundo interruptor controla a lâmpada 2.")
    elif estado_lampada3 == "s":
        print("O terceiro interruptor controla a lâmpada 2.")
    else:
        print("O primeiro interruptor controla a lâmpada 2.")
        
    if estado_lampada3 == "s":
        print("O terceiro interruptor controla a lâmpada 3.")
    elif estado_lampada1 == "s":
        print("O primeiro interruptor controla a lâmpada 3.")
    else:
        print("O segundo interruptor controla a lâmpada 3.")

# Chamada da função para identificar os interruptores
identificar_interruptores()