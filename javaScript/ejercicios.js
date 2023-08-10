function mkDate(dia,mes,año){
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

