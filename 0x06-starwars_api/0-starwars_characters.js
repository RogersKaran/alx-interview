#!/usr/bin/env node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data:', response.statusCode);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;
  const characterNames = [];

  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (err, resp, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
  };

  const fetchAllCharacters = async () => {
    for (const characterUrl of characters) {
      try {
        const name = await fetchCharacter(characterUrl);
        characterNames.push(name);
      } catch (err) {
        console.error('Failed to fetch character data:', err);
      }
    }
    characterNames.sort(); // Sort character names alphabetically
    characterNames.forEach(name => console.log(name));
  };

  fetchAllCharacters();
});
