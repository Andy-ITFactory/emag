Feature: Emag cart feature

    Background:
      Given home: I am a user on emag.ro Home page
      When home: I search after "iphone"
      When search: I add product to basket "iPhone 11"
      When search: I click Vezi detalii cos

    @cart1
    Scenario: Test cart total sum functionality
      Then cart: I verify that total price is correct "2.769,98"


    @cart2
    Scenario: Test cart remove product functionality
      When cart: I click sterge link
      Then cart: I verify empty cart message is displayed




