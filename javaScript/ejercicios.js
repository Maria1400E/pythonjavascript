/*function mkDate(dia,mes,año){
    return {
        day: dia,
        month: mes,
        year: año,
        isValid: function() {
            if (
              this.day >= 1 && this.day <= 31 &&
              this.month >= 1 && this.month <= 12 &&
              this.year >= 1970 && this.year < 3000
            ) {
              return true;
            }
            return false;
          },
          printDate: function() {
            if (this.isValid()) {
              document.write(`${this.day}/${this.month}/${this.year}<br/>`);
            } else {
              document.write("Fecha inválida");
            }
          }
    };
}


const validDate = mkDate(10, 8, 2023);
validDate.printDate(); // Salida: 10/8/2023

const invalidDate = mkDate(32, 13, 2025);
invalidDate.printDate(); // Salida: Fecha inválida

//PUNTO 5

var numeros = new Array(10);
numeros = [2,4,3,7,1,21,9,25,10,12];
var pares = numeros.filter( (val) => val%2==0);
var impares = numeros.filter( (val) => val%2!=0);
console.log(pares);
console.log(impares);

//PUNTO 6
var num = new Array(10);
num = [5,4,7,2,12,21,34,27,10,35];
var par = num.filter( (val) => val%2==0);
var impar = num.filter( (val) => val%2!=0);
var sumaP = par.reduce((anterior, actual) => anterior + actual, 0);
const sumaI = impar.reduce((anterior, actual) => anterior + actual, 0);
console.log(sumaP);
console.log(sumaI);

//PUNTO 7
let calificaciones = {
  nombre: "Juan",
  ingles: 9,
  programacion: 8,
  html:7
};
let sumCalifi = calificaciones.ingles + calificaciones.programacion + calificaciones.html;
let promedio = sumCalifi/3;
console.log('El estudiante',calificaciones.nombre,'tiene un promedio de ',promedio);

//PUNTO 8
var vestido, dato;
vestido = {
   precio: 0,
   descuento: 0,
   neto: function(){ 
         return this.precio*(1 - this.descuento/100)
    }
}
vestido.precio = parseInt(prompt("Precio bruto "));
vestido.descuento = parseInt(prompt("Precio bruto "));
console.log("El precio neto es "+vestido.neto()+"$");

//PUNTO 10
let cadena = prompt("Escriba un texto");
let texto = cadena.split("");
let resultado = texto.join("-");
console.log(resultado);

//PUNTO 11

let cadena = prompt("Escriba una textoque contenga parentesis")

if (cadena.includes('(')) {
    
    var cadenaTemp= cadena.split('(');
    
    cadena = cadenaTemp[1]; 
    
    if (cadena.includes(')')) {
         
        var cadenaTemp= cadena.split(')');
        
        cadena = cadenaTemp[0];
    }
}
console.log(cadena);

//PUNTOS

let  cadena = prompt("Escriba un texto")

function reverseString(str){
  let desorCad = str.split("");
  return desorCad.reverse().join("");
}

document.write(reverseString(cadena));

//PUNTO 13

function esPalindromo(texto) {
  texto = texto.replace(/\s/g, '').toLowerCase();
  
  return texto === texto.split('').reverse().join('');
  }
  
  const textoUsuario = prompt("Ingresa un texto para verificar si es un palíndromo:");
  
  if (esPalindromo(textoUsuario)) {
  console.log("El texto es un palíndromo.");
  } else {
  console.log("El texto no es un palíndromo.");
  }*/