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

console.log("----PUNTO 3-----")

num = prompt("Ingrese un numero entero");



