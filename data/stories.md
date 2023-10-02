## greet
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## account balance 
* greet
  - utter_greet
* account_balance
  - utter_ask_name
  - utter_ask_account_number
  - utter_ask_phone_number
  - action_get_balance
* thanks
  - utter_welcome
  - utter_goodbye

## transaction history 
* greet
  - utter_greet
* transaction_history
  - utter_ask_name
  - utter_ask_account_number
  - utter_ask_phone_number
  - utter_getting_transaction_history
  - action_get_transaction_history
* thanks
  - utter_welcome
  - utter_goodbye

## story 1
* greet
  - utter_greet
* account_balance
  - utter_ask_account_number
  - utter_ask_phone_number
  - action_get_balance
* thanks
  - utter_welcome
  - utter_goodbye