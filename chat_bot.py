import random

classic = {
        "60s": "The Beatles, The Rolling Stones, The Who, The Doors, Cream, The Jimi Hendrix Experience",
        "70s": "Led Zeppelin, Pink Floyd, Queen, AC/DC, Aerosmith, Lynyrd Skynyrd, Rush, Kiss",
        "80s": "Van Halen, Guns N' Roses, Bon Jovi, Def Leppard, Scorpions, U2, Journey",
        "90s": "Nirvana, Pearl Jam, Red Hot Chili Peppers, Foo Fighters, Alice in Chains, Soundgarden, Radiohead, Oasis, The Smashing Pumpkins"
    }

metal = {
        "nu": "Linkin Park, Korn, Limp Bizkit, Slipknot, System of a Down",
        "heavy": "Iron Maiden, Black Sabbath, Judas Priest, Metallica, Megadeth"
    }

def chat():
    txt = input("You: ").strip().lower()
    if "hi" in txt or "hello" in txt:
        print("Me: Hello!! Whats your name?")
        name = str(input("You: ")).strip().title()  
        print(f"Me: Its a pleasure to meet you, {name}!!")
        return name
    
    else: 
        print("Me: Wdym?")
        return None

def humor_chat(name): 
    if name is None:
        print("Me: I don't know you")
        return
    while True:
        humor = str(input("Me: How's your humor today? \nYou: ")).strip().lower()
        if "good" in humor or "great" in humor:
            answer = ["Thats great", "Awesome"]
            print(f"Me: {random.choice(answer)}!!")
            break

        elif "bad" in humor or "not so well" in humor:
            print(f"Me: Ohhh i see {name}, hope u get better!!")
            break

        else:
            print("Me: Wdym?")

def music_chat(name):
    if name is None:
        print("Me: I don't know you")
        return

    # Pergunta inicial
    music_type = input(f"Me: What's your kind of music {name}? Classic or metal \nYou: ").strip().lower()

    while True:  # Loop principal
        if "classic" in music_type:
            while True:
                print("Me: Hm alright, from which year?")
                year = input("You: ").strip().lower()
                if "60" in year:
                    print(f"Me: Ohhh I see, here are some icons if you like {name}!! {classic['60s']}")
                elif "70" in year:
                    print(f"Me: Ohhh I see, here are some icons if you like {name}!! {classic['70s']}")
                elif "80" in year:
                    print(f"Me: Ohhh I see, here are some icons if you like {name}!! {classic['80s']}")
                elif "90" in year:
                    print(f"Me: Ohhh I see, here are some icons if you like {name}!! {classic['90s']}")
                else:
                    print("Me: The year does not match, try again!")
                    continue  

                # Perguntar se quer outra recomendação ou mudar de gênero
                while True:
                    confirm = input("Me: Is there any other year you'd like to know or do you want to switch to metal? (yes/metal/no)\nYou: ").strip().lower()
                    if "yes" in confirm:
                        break  
                    elif "metal" in confirm:
                        music_type = "metal"
                        break  
                    elif "no" in confirm:  # Se o usuário disser "no", encerra tudo
                        print(f"Me: Ok {name}!! Hope you liked the recommendations!!")
                        return  
                    else:
                        print("Me: I didn't get that, try again!")

                if music_type == "metal":
                    break  

        elif "metal" in music_type:
            while True:
                print("Me: Hm alright, from which type, nu metal or heavy metal??")
                type = input("You: ").strip().lower()
                if "nu" in type:
                    print(f"Me: Ahhh that's great!! Got some bands for you if you are interested!! {metal['nu']}")
                elif "heavy" in type:
                    print(f"Me: Ahhh that's great!! Got some bands for you if you are interested!! {metal['heavy']}")
                else:
                    print("Me: This does not match, try again!")
                    continue  

                # Perguntar se quer outra recomendação ou mudar de gênero
                while True:
                    confirm = input("Me: Is there any other type you'd like to know or do you want to switch to classic? (yes/classic/no)\nYou: ").strip().lower()
                    if "yes" in confirm:
                        break  
                    elif "classic" in confirm:
                        music_type = "classic"
                        break  
                    elif "no" in confirm:  # Se o usuário disser "no", encerra tudo
                        print(f"Me: Ok {name}!! Hope you liked the recommendations!!")
                        return  
                    else:
                        print("Me: I didn't get that, try again!")

                if music_type == "classic":
                    break  

        else: 
            print("Me: I can't recommend you that, try again.")
            break  


def bye_chat(name):
    pleasure = str(input("You: ")).strip().lower()
    if "thank you" in pleasure or "thanks" in pleasure:
        bye = input(f"Me: You are welcome {name}!! This was a great chat!! \nYou: ")
        if "bye" in bye or "see you":
            print("Me: Goodbye!! :D")
            
        
        else:
            print("Me: How rude!! >:(")

    else:
        print("wdym?")
        return

name = chat()
humor_chat(name)
music_chat(name)
bye_chat(name)
