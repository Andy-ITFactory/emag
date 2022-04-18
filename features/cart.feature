Feature: Emag cart feature

    Background:
      Given home: I am a user on emag.ro Home page
      When home: I search after "iPhone 11, 64GB, Black"
      When products: I add product to basket "Telefon mobil Apple iPhone 11, 64GB, Black"
      When products: I click Vezi detalii cos

    @cart1
    Scenario: Test cart total sum functionality
      Then cart: I verify that total price is correct "2.669,99"


    @cart2
    Scenario: Test cart remove product functionality
      When cart: I click sterge link
      Then cart: I verify empty cart message is displayed




