#!/bin/zsh

file_path="pokemon_list.txt"

# API URL
api="https://pokeapi.co/api/v2/pokemon-species/"

while IFS= read -r row
do
    curl -s "$api$row" -o pokemons/$row.json
    sleep 2

done < "$file_path"
