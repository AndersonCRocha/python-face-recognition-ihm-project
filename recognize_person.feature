Feature: Reconhecer uma pessoa pela foto

  Scenario: Uma pessoa chega na portaria do condomínio e terá sua face reconhecida por uma câmera
    Given o ambiente foi configurado corretamente
    When a foto mary-01.jpg for capturada
    Then a pessoa deverá ser reconhecida

  Scenario: Uma pessoa chega na portaria do condomínio e não terá sua face reconhecida por uma câmera
    Given o ambiente foi configurado corretamente
    When a foto claire-01.jpg for capturada
    Then a pessoa não deverá ser reconhecida