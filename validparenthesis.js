const s = "()[]{}";
const parejas = [];
let band;

// compruebo que no sea impar la secuencia
if (s.length % 2 != 0) band = false;

// la separo en parejas
for (let i = 0; i < s.length; i += 2) {
  parejas.push(s.slice(i, i + 2));
}

console.log(parejas);
console.log(band);
