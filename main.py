from fastapi import FastAPI, Path, HTTPException
from dataclasses import dataclass, asdict
from typing import Union
import json
#===========================================================
with open("pokemons.json", "r", encoding="utf-8") as f :
    contenu = json.load(f)
list_pokemons = {i+1:j for i, j in enumerate(contenu)}
print(list_pokemons[1])
#============================================================
@dataclass
class Pokemon() :
    id: int
    name: str
    types: list[str]
    total: int
    hp: int
    attack: int
    defense: int
    attack_special: int
    defense_special: int
    speed: int
    evolution_id: Union[int, None] = None
#======================================================================================
app = FastAPI()
@app.get("/total_pokemons")
def get_total_pokemons() -> dict:
    return {"total" : len(list_pokemons)}
#==============================================================
@app.get("/list_pokemons")
def get_list_pokemons() -> list[Pokemon] :
    tous = []
    for id in list_pokemons :
        tous.append(Pokemon(**list_pokemons[id]))

    return tous

#===========================================================================================================
@app.get("/pokemon/{id}")
def get_pokemon(id: int = Path(ge=1)) -> Pokemon:
    if id not in list_pokemons :
        raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas dans notre liste.")
    return Pokemon(**list_pokemons[id])
#========================================================================================================
@app.post("/pokemon/")
def create_pokemon(mon_pokemon: Pokemon) -> Pokemon :
    if mon_pokemon.id in list_pokemons :
        raise HTTPException(status_code=404, detail="Ce pokemon existant déja")
    list_pokemons[mon_pokemon.id] = asdict(mon_pokemon)
    return mon_pokemon
#=====================================================================================
@app.put("/pokemon/{id}")
def new(pokemon: Pokemon, id: int = Path(ge=1)) -> Pokemon:
    if id not in list_pokemons :
        raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas")
    list_pokemons[id] = asdict(pokemon)
    return pokemon
#====================================================================================
@app.delete("/pokemon/{id}")
def delete(id: int = Path(ge=1)) -> Pokemon :
    if id not in list_pokemons :
        raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas")
    retour = list_pokemons[id]
    del(list_pokemons[id])
    return retour
#====================================================================================*
@app.get("/types/")
def search() -> set():
    types = set()
    for info in list_pokemons.values() :
        types.update(set(info["types"]))
    return types
#====================================================================================*
@app.get("/pokemon/search/")
def search_pokemon(
    types: Union[str, None] = None,
    evo: Union[str, None] = None,
    totalgt: Union[int, None] = None,
    totallt: Union[int, None] = None,
    sortby: Union[str, None] = None,
    order: Union[str, None] = None
) -> Union[list[Pokemon], None] :

    filtered_list = []
    res = []
    #les types
    if types is not None :
        for pokemon in list_pokemons.values() :
            if set(types.split(",")).issubset(pokemon["types"]) :
                filtered_list.append(pokemon)
    #Les evolutions
    if evo is not None :
        tmp = filtered_list if filtered_list else list_pokemons
        new = []
        for pokemon in tmp :
            if evo.lower() == "true" and "evolution_id" in pokemon :
                new.append(pokemon)
            elif evo.lower() == "false" and "evolution_id" not in pokemon :
                new.append(pokemon)
        filtered_list = new
    #Greater than total
    if totalgt is not None :
        tmp = filtered_list if filtered_list else list_pokemons
        new = []
        for pokemon in tmp :
            if pokemon["total"] >= totalgt :
                new.append(pokemon)
        filtered_list = new
    #Less than total
    if totallt is not None :
        tmp = filtered_list if filtered_list else list_pokemons
        new = []
        for pokemon in tmp :
            if pokemon["total"] <= totallt :
                new.append(pokemon)
        filtered_list = new
    #On gère le tri
    if sortby is not None and sortby in ["id", "name", "total"] :
        filtered_list = filtered_list if filtered_list else list_pokemons
        sorting_order = False
        sorting_order = False if order == "asc" else True

        filtered_list = sorted(filtered_list, key=lambda d: d[sortby], reverse=sorting_order)
    #Reponse
    if filtered_list :
        for pokemon in filtered_list :
            res.append(Pokemon(**pokemon))
        return res
    raise HTTPException(status_code=404, detail="Aucun pokemon ne correspond à vos critères.")