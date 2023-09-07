console.log("------PUNTO 1------")
let tam = prompt("Ingrese el tamaño del arreglo: ");
let n = prompt("Ingrese el número multiplo: ")
let vec = [];

function multi(vec){
    for(x = 1; x <= tam; x ++){
        vec.push(x*n);
    }

    return vec;
}
console.log(multi(vec));

console.log("------PUNTO 2------")
let notas = [20,15,12,11,8,4,1];
console.log(notas);
notas.pop();
console.log("Array sin el número menor: " + notas);

let suma2 = notas.reduce((anterior, actual) => anterior + actual, 0);
console.log("Promedio del array: " + suma2/notas.length)

console.log("------PUNTO 3------")
 
a = [1,9,4,25,16];

var iterator = a[Symbol.iterator]();
iterator + ""; 

console.log(iterator.next()); 
console.log(iterator.next()); 
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());

console.log("-------PUNTO 4-------")
const numero = parseInt(prompt("Por favor, ingresa un número entero: "));

if (isNaN(numero)) {
  console.log("Por favor, ingresa un número válido.");
} else {
  for (let i = 1; i <= numero; i++) {
    const linea = "*".repeat(i);
    console.log(linea);
  }
}

console.log("-------PUNTO 5------")
function obtenerEntradaUsuario() {
    return prompt("Escribe algo (o escribe 'salir' para terminar):");
  }
  let entrada = obtenerEntradaUsuario();

  while (entrada.toLowerCase() !== "salir") {
    console.log("Eco: " + entrada);
    entrada = obtenerEntradaUsuario();
  }
console.log("Programa terminado.");

console.log("-----PUNTO 6------")
let fechaNacimiento = prompt("Por favor, ingresa tu fecha de nacimiento (AAAA-MM-DD):");

let fechaNac = new Date(fechaNacimiento);

let fechaActual = new Date();

let edad = fechaActual.getFullYear() - fechaNac.getFullYear();

if (
  fechaActual.getMonth() < fechaNac.getMonth() ||
  (fechaActual.getMonth() === fechaNac.getMonth() && fechaActual.getDate() < fechaNac.getDate())
) {
  edad--; 
}
console.log("Tienes " + edad + " años.");

console.log("-------PUNTO 7-------")
const edad1 = parseInt(prompt("Por favor, ingresa tu edad:"));

const añoActual = new Date().getFullYear();

const añoNacimiento = añoActual - edad1;

console.log("Naciste en el año " + añoNacimiento + ".");


  


