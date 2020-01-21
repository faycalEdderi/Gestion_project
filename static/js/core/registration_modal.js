$().ready(function() { 
    
    $("#display_modal").click(function(){

        let is_empty = '';
        let email = $("#id_email").val();
        let last_name = $("#id_last_name").val();
        let first_name = $("#id_first_name").val();
        let poste = $("#id_poste option:selected").text();
        let role = $("#id_role").val();

        let modal_head = '<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true"> <div class="modal-dialog" role="document"><div class="modal-content"><div class="modal-header"><h5 class="modal-title" id="exampleModalLabel">Veuillez verifier les informations</h5><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button></div><div class="modal-body">' ;

        let modal_body = '<p>nom : ' +  last_name + '</p>' +  '<p>prénom : ' +  first_name+ '<p>email : ' +  email+ '</p>' + '</p>' + '<p>poste : ' +  poste+ '</p>' + '<p>poste : ' +  role+ '</p>' ;
        
        let modal_footer = '</div><div class="modal-footer"><button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button> <button form="valid_register"  class="btn btn-primary" type="submit"> Valider </button></div></div></div></div>';
        
        switch(is_empty){
                    
                    case last_name:
                            alert(' Veuillez entrer un nom.')
                        break;
                    case first_name:
                            alert(' Veuillez entrer un prénom.')
                        break;
                    case email:
                            alert('Veuillez entrer une adresse mail.')
                        break;
                case role:
                            alert('Veuillez selectionner un role.')
                        break;
                    
                    default:
                    document.getElementById("affich_modal").innerHTML = modal_head + modal_body + modal_footer  ;
                }
        });
        
});  



    



   
  
  

