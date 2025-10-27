Feature: Buscar pelicula verificar nombre y calificacion
    Scenario: Validar nombre de pelicula y su calificacion
        Given el usuario esta en el homepage de imdb.com
        When el usuario busca la pelicula "El origen"
        And presiona el link del primer resultado de pelicula
        Then su calificacion es "8.8"
        And el nombre de la pelicula es "El origen"