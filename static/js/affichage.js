
$().ready(function() { 

    //Par defaut toutes les liste de poste sont caché
    $("#equipe_liv").hide();
    
/* Lorque le champs select du poste est modifié une liste de poste s'affiche
 * en fonction de la valeur
 */
    $("#id_poste").change(function(){
        let poste = $("#id_poste option:selected").text();
        if(poste == "LIV"){

            $("#equipe_liv").show();


        }else{
            $("#equipe_liv").hide();

        }
    });
    
    
    
});  
    



   
  
  

