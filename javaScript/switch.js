var fecha = new Date();
var dia = fecha.getDay();
var traduccion = "";

switch(dia){
	case 0:
		traduccion = "domingo";
		break;
	case 1:
		traduccion = "lunes";
		break;			
	case 2:
		traduccion = "martes";
		break;			
	case 3:
		traduccion = "miércoles";
		break;			
	case 4:
		traduccion = "jueves";
		break;			
	case 5:
		traduccion = "viernes";
		break;			
	case 6:	
		traduccion = "sábado";
		break;	
	default:
		traduccion = "error";					
}
document.write("<p>hoy es " + traduccion +"</p>");