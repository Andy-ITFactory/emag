Feature: Emag login feature

    Background:
      Given home: I am a user on emag.ro Home page

    @login
    Scenario: Click logo button and return to home
      When home: I click on contul meu
      When login: I set my email "abc@email.com"
      When login: I click emag logo
      Then home: I verify home page url


