$().ready(function() { 
    
    //Par defaut toutes les liste de poste sont caché
    $("#equipe_liv").hide();
    $("#equipe_responsable").hide();
    
/* Page de création de compte : 
 * Lorque le champs select du poste est modifié une liste de poste s'affiche
 * en fonction de la valeur
 */
    $("#id_role").change(function(){
        let poste = $("#id_role option:selected").text();


        switch(poste){
            case 'PILOTE D\'ACTIVITÉ':
                    $("#equipe_liv").show();
                    $("#equipe_responsable").hide();
                break;
            case 'CH.EXECUTION':
                    $("#equipe_responsable").show();
                    $("#equipe_liv").hide();
                break;
            
            default:
                    $("#equipe_liv").hide();
                    $("#equipe_responsable").hide();
        }
    });

// suppression de l'alerte après 3 secondes
// durée en millisecondes
window.setTimeout( () => $('.alert').fadeOut('slow'), 3000 );


let email = $("#id_email").val()

$("#display_modal").click(function(){

    alert("lol");
});
   
});  
    



   
  
  

