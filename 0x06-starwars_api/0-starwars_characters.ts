/// <reference path="./types.d.ts" />

import axios from 'axios';
import { StarWars, Options } from './types.d.ts';

const options: Options = {
    uri: 'https://swapi.dev/api/films/1/',
    json: true,
}

axios.get(options.uri)
.then((response) => {
    const starWars: StarWars = response.data;
    //const characters = starWars.characters;
    extractInOrder(starWars, 0);
    console.log(starWars);
}).catch((error) => {
    console.error(error);
})

const extractInOrder = (actors: StarWars, id: number) => {
    if (actors.characters.length === id) {
        return;
    }
    axios.get(actors.characters[id])
    .then((response) => {
        console.log(response.data.name);
        extractInOrder(actors, id + 1);
    }).catch((error) => {
        console.error(error);
    })
}
