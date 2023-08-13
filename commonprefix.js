const strs = ["cir", "car"];
let x = [];
let band = true;
let pref = "";

if (strs.length == 1) return strs[0];

for (let i = 0; i < strs.length; i++) {
  x.push(strs[i].split(""));
  if (!strs[i].length) return "";
}

let letters = [];

for (let i = 0; i < x[0].length; i++) {
  console.log(band);
  for (let j = 0; j < x.length; j++) {
    letters.push(x[j][i]);
  }
  let cnt = 0;
  console.log(letters);
  for (let j = 0; j < letters.length - 1; j++) {
    if (letters[j] == letters[j + 1]) {
      console.log("pasa");
      cnt++;
      if (cnt == letters.length - 1) pref += letters[0];
    } else {
      console.log("no pasa");
      band = false;
      break;
    }
  }
  letters = [];
  if (!band) {
    break;
  }
}

return pref;
