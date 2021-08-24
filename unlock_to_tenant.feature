Feature: Desbloquear porta para inquilinos que estão no aguardo

  Scenario: a porta é aberta para um inquilino que está esperando a liberação
    Given o ambiente foi configurado corretamente
    When a foto mary-01.jpg for capturada
    Then a pessoa deverá ser reconhecida
    Then ela deverá ser classificada como inquilino
    Then a porta será aberta e o inquilino estará com entrada permitida