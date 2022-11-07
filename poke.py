import requests
import os

url="https://pokeapi.co/api/v2"

generation = f"{url}/generation"
ability    = f"{url}/ability"
shape      = f"{url}/pokemon-shape"
habitat    = f"{url}/pokemon-habitat"
type       = f"{url}/type"

print("\n ********* MENU PRTINCIPAL ********* \n")
print("1.- Listar pokemons por generacion")
print("2.- Listar pokemons por forma")
print("3.- Listar pokemons por habilidad")
print("4.- Listar pokemons por habitat")
print("5.- Listar pokemons por tipo")

opcion =int(input("Elija la opcion que desee mostrar :"))

if opcion == 1:
        generation_url = requests.get(generation).json()
        gen = generation_url["results"]
        gen_lista=[""]
        for num,i in enumerate(gen, start =1):
                print(f"{num}: {i['name']}")
                gen_lista.append(i['name'])

        opcion1 = int(input("Elija una opcion (1, 2,..., 8) :"))
        print('***************************************************')
        print('*************POKEMONES LEGENDARIOS*****************')
        print('***************************************************')
        if opcion1==1:
         g1 = requests.get(f"{generation}/{opcion1}").json()
         for num,i in enumerate(g1['pokemon_species'], start =1):
                 print(f"{'Pokémon'} {num}: {i['name']}")
        elif opcion1 == 2:
                g2 = requests.get(f"{generation}/{opcion1}").json()
                for num, i in enumerate(g2['pokemon_species'], start=1):
                    print(f"{'Pokémon'} {num}: {i['name']}")
        elif opcion1 == 3:
                g3 = requests.get(f"{generation}/{opcion1}").json()
                for num, i in enumerate(g3['pokemon_species'], start=1):
                    print(f"{'Pokémon'} {num}: {i['name']}")
        elif opcion1 == 4:
                g4 = requests.get(f"{generation}/{opcion1}").json()
                for num, i in enumerate(g4['pokemon_species'], start=1):
                    print(f"{'Pokémon'} {num}: {i['name']}")
        elif opcion1 == 5:
                g5 = requests.get(f"{generation}/{opcion1}").json()
                for num, i in enumerate(g5['pokemon_species'], start=1):
                    print(f"{'Pokémon'} {num}: {i['name']}")
        elif opcion1 == 6:
                g6 = requests.get(f"{generation}/{opcion1}").json()
                for num, i in enumerate(g6['pokemon_species'], start=1):
                    print(f"{'Pokémon'} {num}: {i['name']}")
        elif opcion1 == 7:
                g7 = requests.get(f"{generation}/{opcion1}").json()
                for num, i in enumerate(g7['pokemon_species'], start=1):
                    print(f"{'Pokémon'} {num}: {i['name']}")
        elif opcion1 == 8:
                g8 = requests.get(f"{generation}/{opcion1}").json()
                for num, i in enumerate(g8['pokemon_species'], start=1):
                    print(f"{'Pokémon'} {num}: {i['name']}")


if opcion ==2:
  print('******************************************************')
  print('*************POKEMONES SEGÚN SU HABILIDAD*************')
  print('******************************************************')
  shap_url = requests.get(f"{shape}/{opcion}").json()
  shap = shap_url['pokemon_species']
  for num, i in enumerate(shap, start=1):
         print(f" {num}: {i['name']}")

if opcion==3:
  ability_url = requests.get(ability).json()
  abi = ability_url["results"]
  print('**************************************************')
  print('*************POKEMONES SEGÚN SU FORMA*************')
  print('**************************************************')

  for num,i in enumerate(abi, start = 1):
         print(f"{'Pokémon'} {num}: {i['name']}")

if opcion ==4:
  print('**************************************************')
  print('*************POKEMONES SEGÚN SU HABITAT*************')
  print('**************************************************')
  hab_url = requests.get(habitat).json()
  hab = hab_url["results"]
  for num,i in enumerate(hab, start = 1):
         print(f"{'Pokémon'} {num}: {i['name']}")
if opcion ==5 :
  tip_url = requests.get(type).json()
  tip = tip_url["results"]
  for num, i in enumerate(tip, start=1):
         print(f"{num}: {i['name']}")
