import os
os.system("cls")


print("Bem vindo ao pokemon falsificado da shoppe!")
print("Você deseja iniciar o jogo?")

# Menu inicial
inicio = int(input("1- Iniciar  2- Fechar\n"))

if inicio == 1:
    print("\nPerfeito! Agora, escolha seu pokemon inicial!")
    
    seu_pokemon = int(input("1- Charmander  2- Squirtle  3- Bulbasaur\n"))
    
    
    if seu_pokemon == 1:
        nome_jogador = "Charmander"
        print("Você escolheu o Charmander!")
    elif seu_pokemon == 2:
        nome_jogador = "Squirtle"
        print("Você escolheu o Squirtle!")
    elif seu_pokemon == 3:
        nome_jogador = "Bulbasaur"
        print("Você escolheu o Bulbasaur!")
    else:
        nome_jogador = "Pokemon desconhecido"
        print("Você não digitou um pokemon válido!")
        print("Reiniciando o jogo...")
       

    # ====================== BATALHA ======================
    if seu_pokemon in [1, 2, 3]:        
        print("\nA batalha começa!!")
        
        # Status iniciais
        hp_jogador = 100
        atk_jogador = 10
        hp_oponente = 100
        atk_oponente = 10
        
        print(f"\nStatus do seu {nome_jogador}:")
        print(f" HP: {hp_jogador}   ATK: {atk_jogador}")
        print(f"Status do oponente:")
        print(f" HP: {hp_oponente}   ATK: {atk_oponente}")
        
        # Variável de controle da batalha
        batalha_continua = True
        
        while batalha_continua:
            # Vez do Jogador
            movimento = int(input("\nEscolha sua ação:\n1: Atacar\n2: Curar\n3: Fugir\n"))
            
            if movimento == 1:          # ATACAR
                print(f"\nVocê usou Atacar! {nome_jogador} deu 10 de dano no oponente!")
                hp_oponente -= atk_jogador
                print(f"Vida atual do oponente: HP {hp_oponente}")
                
            elif movimento == 2:        # CURAR
                if hp_jogador >= 100:
                    print("Seu HP está cheio, você não pode curar.")
                else:
                    cura = 20
                    hp_jogador += cura
                    if hp_jogador > 100:
                        hp_jogador = 100
                    print(f"Você usou Curar! Recuperou {cura} de HP.")
                    print(f"Vida atual do seu {nome_jogador}: HP {hp_jogador}")
                
            elif movimento == 3:        # FUGIR
                print("\nVocê foge da luta.......")
                print("COVARDE!!!")
                print("Finalizando programa...")
                batalha_continua = False
                
            else:                       # Movimento inválido
                print("Movimento inválido! Tente novamente.")
                
            
            
            if batalha_continua:
                if hp_oponente <= 0:
                    print(f"\nParabéns! Seu {nome_jogador} venceu a batalha!")
                    batalha_continua = False
                
                else:
                    # ==================== VEZ DO OPONENTE ====================
                    print("\nÉ a vez do oponente!")
                    print("O oponente usou Atacar! Ele deu 10 de dano no seu pokemon!")
                    hp_jogador -= atk_oponente
                    print(f"Vida atual do seu {nome_jogador}: HP {hp_jogador}")
                    
                    
                    if hp_jogador <= 0:
                        print("\nVocê foi derrotado...")
                        batalha_continua = False

    
    else:
        print("\nComo você não escolheu um Pokémon válido, o jogo não pode continuar.")

elif inicio == 2:
    print("Fechando o jogo...")
else:
    print("Opção inválida! Fechando o programa.")

print("\nFim do jogo!")

