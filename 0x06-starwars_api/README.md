# Star wars API 
## Description
This is a simple API that allows you to get information about the Star Wars universe. It is a RESTful API that provides information about the characters, planets, starships, vehicles and species of the Star Wars universe. The API is based on the data from the Star Wars API (https://swapi.dev/). The API is built using the Django REST framework and is deployed on Heroku. The API is available at https://star-wars-api-2021.herokuapp.com/. The API has the following endpoints:
- /characters/
- /characters/{id}/
- /planets/
- /planets/{id}/
- /starships/
- /starships/{id}/
- /vehicles/
- /vehicles/{id}/
- /species/
- /species/{id}/
## How to use the API
To use the API, you can send a GET request to the desired endpoint. For example, to get information about the characters, you can send a GET request to the /characters/ endpoint. You can also get information about a specific character by sending a GET request to the /characters/{id}/ endpoint, where {id} is the id of the character. Similarly, you can get information about the planets, starships, vehicles and species by sending a GET request to the corresponding endpoints.
## Example
To get information about the characters, you can send a GET request to the /characters/ endpoint. For example, you can use the following curl command:
``` curl https://star-wars-api-2021.herokuapp.com/characters/ ```
This will return a list of characters in the Star Wars universe.
To get information about a specific character, you can send a GET request to the /characters/{id}/ endpoint. For example, you can use the following curl command:

## Run the example scripts
### JS: ``` npm i && ./0-starwars_characters.js```
### TS: install deno 2.0 and ``` deno run 0-starwars_characters.ts```

## Author
EL Abassi Abderrazaq
