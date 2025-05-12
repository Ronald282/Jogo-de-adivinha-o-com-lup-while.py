nom = 0 

while nom < 3:
    per = int(input("Tente adivinhar o numero?😉"))
    nom += 1

    if per == 420:
        print(f"Meus parabens! Você acertou🎉 era o numero (420) 👌😁")
        break

    else:
        print("Ummm não era esse o numero 😕, Tente outra vez👍")
     
    
else:
    print("Que pena o limite de 3 tentativas foi atigido mais sorte na proxima😔 ")
    
