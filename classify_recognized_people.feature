Feature: Classificar as pessoas reconhecidas em Inquilinos ou visitantes

  Scenario: Uma pessoa reconhecida será classificada como inquilino
    Given o ambiente foi configurado corretamente
    When a foto mary-01.jpg for capturada
    Then a pessoa deverá ser reconhecida
    Then ela deverá ser classificada como inquilino

  Scenario: Uma pessoa reconhecida será classificada como visitante
    Given o ambiente foi configurado corretamente
    When a foto jane-01.jfif for capturada
    Then a pessoa deverá ser reconhecida
    Then ela deverá ser classificada como visitante