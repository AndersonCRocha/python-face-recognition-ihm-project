Feature: Desbloquear porta para visitantes que estão no aguardo

  Scenario: a porta é aberta para um visitante que está esperando a liberação
    Given o ambiente foi configurado corretamente
    When a foto jane-01.jfif for capturada
    Then a pessoa deverá ser reconhecida
    Then ela deverá ser classificada como visitante
    Then a porta será aberta e o visitante estará com entrada permitida