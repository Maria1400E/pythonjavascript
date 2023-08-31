/*Ejecuta una sentencia si una condición específicada es evaluada como verdadera. 
Si la condición es evaluada como falsa, otra sentencia puede ser ejecutada.*/

const edad = 18;

if (edad >= 18) {
  console.log("Nick es un adulto.");
} else {
  console.log("Nick es un niño.");
}

const edad1 = 18;

if (edad1 < 18) {
  console.log("Alice es menor de 18 años.");
} else if (edad1 >= 18 && edad1 <= 21) {
  console.log("Alice tiene entre 18 y 21 años de edad.");
} else {
  console.log("Alice tiene mas de 21 años.");
}


