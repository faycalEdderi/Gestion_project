
$().ready(function() { 
    
    //Par defaut toutes les liste de poste sont caché
    $("#equipe_liv").hide();
    $("#equipe_responsable").hide();
    
/* Lorque le champs select du poste est modifié une liste de poste s'affiche
 * en fonction de la valeur
 */
    $("#id_poste").change(function(){
        let poste = $("#id_poste option:selected").text();


        switch(poste){
            case 'LIV':
                    $("#equipe_liv").show();
                    $("#equipe_responsable").hide();
                break;
            case 'CH.MIL':
                    $("#equipe_responsable").show();
                    $("#equipe_liv").hide();
                break;
            case 'CH.HIL' :
                    $("#equipe_responsable").show();
                    $("#equipe_liv").hide();
                break;
            case 'CH.IS':
                    $("#equipe_responsable").show();
                    $("#equipe_liv").hide();
                break;
            default:
                    $("#equipe_liv").hide();
                    $("#equipe_responsable").hide();


        }


      /*  if(poste == "LIV"){

            $("#equipe_liv").show();


        }if(poste == "CH.MIL" || poste == "CH.HIL" || poste == "CH.MIL"){

            $("#equipe_responsable").show();
            


        }
        
        else{
            $("#equipe_liv").hide();
            $("#equipe_responsable").hide();

        }*/
    });



    
    
    
    
});  
    



   
  
  

