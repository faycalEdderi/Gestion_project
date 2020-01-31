 '''
amelioration de creation de UO a voir


            def find_object(nom_objet, id_class):
                nom_objet.objects.get(id = id_class)

            id_array = [
                type_uo_id ,
                niveau_uo_id ,
                projet_id,
                fonction_id ,
                satut_uo_id ,
                etat_uo_id ,
                plateform_id,
                catalogue_id,
                lot_id,
            ]

            uo_attributes = [
                typeuo,
                niveauo,
                projet,
                fonction,
                statutuo,
                etatuo,
                plateforme,
                catalogue,
                lot,
            ]

            class_array = [
                Typeuo,
                Niveauuo,
                Projet,
                Fonction,
                Statutuo,
                Etatuo,
                Plateforme,
                CatalogueUo,
                Lot
            ]

            i=0
            objet = Uo()
            while i < len(id_array):
                for objet in class_array:

                    selected_object = find_object(objet, id_array[i])
                    uo_attributes[i] = selected_object
                    print("attribut : ", uo_attributes[i] )
                    i += 1

            
            for attr, value in objet.__dict__.items():
                print(attr)
           
            '''
