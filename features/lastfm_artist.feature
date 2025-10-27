Feature: Buscar un artista en latt.fm y validar la fecha de su ultimo lanzamiento
    Scenario: Validar la fecha del ultimo release de Myke Towers
        Given  el usuario está en el home page de last.fm
        When el usuario busca el artista "Myke Towers"
        And presiona el link del primer resultado
        Then la fecha del ultimo release debe ser "27 September 2025"