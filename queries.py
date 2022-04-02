GET_ANIMAL_BY_ID_QUERY = '''
SELECT
    new_animal.id,
    age_upon_outcome,
    animal_id,
    new_animal.name,
    date_of_birth,
    outcome_month,
    outcome_year,
    animal_type.name as 'type',
    animal_breed.name as 'breed',
    animal_color1.name as 'color1',
    animal_color2.name as 'color2',
    outcome_subtype.name as 'outcome_subtype',
    outcome_type.name as 'outcome_type'
    
FROM new_animal
LEFT JOIN animal_type 
    ON animal_type.id = new_animal.type_id
LEFT JOIN animal_breed
    ON animal_breed.id = new_animal.breed_id
LEFT JOIN animal_color as animal_color1
    ON animal_color1.id = new_animal.color1_id
LEFT JOIN animal_color as animal_color2
    ON animal_color2.id = new_animal.color2_id
LEFT JOIN outcome_subtype
    ON outcome_subtype.id = new_animal.outcome_subtype_id
LEFT JOIN outcome_type
    ON outcome_type.id = new_animal.outcome_type_id
WHERE new_animal.animal_id = :1
'''
