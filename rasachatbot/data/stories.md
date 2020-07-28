## complete path 1
* greet 
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"valid_location":"true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"valid_cuisine":"true"}
    - utter_ask_budget
*restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_search_restaurants
    - utter_send_mail
*deny
    - utter_goodbye
    - action_slotreset

## complete path 2
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"valid_location":"true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"valid_cuisine":"true"}
    - utter_ask_budget
* restaurant_search{"budget":"More than 700"}
    - slot{"budget":"More than 700"}
    - action_search_restaurants
    - utter_send_mail
* affirm
    - utter_ask_email
* send_email{"email":"test123@gmail.com"}
    - slot{"email":"test123@gmail.com"}
    - action_send_email
    - utter_sentmail
    - action_slotreset

## completepath3
* greet
    - utter_greet
* restaurant_search
    -utter_ask_location
* restaurant_search{"location": "kota"}
    - slot{"location": "kota"}
    - action_check_location
    - slot{"valid_location":"false"}
    - utter_locationNotServiced
* restaurant_search{"location":"delhi"}
    - slot{"location":"delhi"}
    - action_check_location
    - slot{"valid_location":"true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"valid_cuisine":"true"}
    - utter_ask_budget
*restaurant_search{"budget":"More than 700"}
    - slot{"budget":"More than 700"}
    - action_search_restaurants
    - utter_send_mail
*send_email{"email":"dineshkumarjangid@gmail.com"}
    - slot{"email":"dineshkumarjangid@gmail.com"}
    - action_send_email
    - utter_sentmail
    - action_slotreset


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"valid_location": "true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"valid_cuisine":"true"}
    - utter_ask_budget
* greet{"budget": " More than 700"}
    - slot{"budget": " More than 700"}
    - action_search_restaurants
    - utter_send_mail
* affirm
    - utter_ask_email
* send_email{"email": "test1@gmail.co.in"}
    - slot{"email": "test1@gmail.co.in"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_2
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"valid_location": "true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_check_cuisine
    - slot{"valid_cuisine":"true"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs.300 to 700"}
    - slot{"budget": "Rs.300 to 700"}
    - action_search_restaurants
    - utter_send_mail
* affirm
    - utter_ask_email
* send_email{"email": "email123@yahoo.com"}
    - slot{"email": "email123@yahoo.com"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"valid_location": "true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"valid_cuisine":"true"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs.300 to 700"}
    - slot{"budget": "Rs.300 to 700"}
    - action_search_restaurants
    - utter_send_mail
* affirm
    - utter_ask_email
* send_email{"email": "testing_mail@mail.co.uk"}
    - slot{"email": "testing_mail@mail.co.uk"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"location": "Trichy"}
    - slot{"location": "Trichy"}
    - action_check_location
    - slot{"valid_location": "true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"valid_cuisine":"true"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs.300 to 700"}
    - slot{"budget": "Rs.300 to 700"}
    - action_search_restaurants
    - utter_send_mail
* send_email{"email": "testingmail12.am@yahoo.com"}
    - slot{"email": "testingmail12.am@yahoo.com"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"location": "Trichy"}
    - slot{"location": "Trichy"}
    - action_check_location
    - slot{"valid_location": "true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"valid_cuisine":"true"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs.300 to 700"}
    - slot{"budget": "Rs.300 to 700"}
    - action_search_restaurants
    - utter_send_mail
* affirm
    - utter_ask_email
* affirm{"email": "abc@ok.work.in"}
    - slot{"email": "abc@ok.work.in"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"valid_location": "true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_check_cuisine
    - slot{"valid_cuisine": "false"}
    - utter_Invalidcuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs.300 to 700"}
    - slot{"budget": "Rs.300 to 700"}
    - action_search_restaurants
    - utter_send_mail
* send_email{"email": "dinesh@outlook.com"}
    - slot{"email": "dinesh@outlook.com"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai", "location": "chennai"}
    - slot{"cuisine": "thai"}
    - slot{"location": "chennai"}
    - action_check_location
    - slot{"valid_location": "true"}
    - action_check_cuisine
    - slot{"valid_cuisine": "false"}
    - utter_Invalidcuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_send_mail
* send_email{"email": "dineshkumarjangid@gmail.com"}
    - slot{"email": "dineshkumarjangid@gmail.com"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_7a
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian", "location": "Durg Bhilai"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Durg Bhilai"}
    - action_check_location
    - slot{"valid_location": "true"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs.300 to 700"}
    - slot{"budget": "Rs.300 to 700"}
    - action_search_restaurants
    - utter_send_mail
* send_email{"email": "dineshkumarjangid@gmail.com"}
    - slot{"email": "dineshkumarjangid@gmail.com"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_8
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Delhi"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"valid_location": "true"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs.300 to 700"}
    - slot{"budget": "Rs.300 to 700"}
    - action_search_restaurants
    - utter_send_mail
* deny
    - utter_goodbye
    - action_slotreset
    - reset_slots

## interactive_story_9
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"valid_location": "false"}
    - utter_locationNotServiced
* restaurant_search{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
    - action_check_location
    - slot{"valid_location": "true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_send_mail
* send_email{"email": "acb209@gmail.com"}
    - slot{"email": "acb209@gmail.com"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_10
* restaurant_search{"budget": " Lesser than Rs.300"}
    - slot{"budget": " Lesser than Rs.300"}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"valid_location": "true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## interactive_story_11
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"valid_location": "true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - utter_ask_budget
* restaurant_search{"budget": " Rs.300 to 700"}
    - slot{"budget": " Rs.300 to 700"}
    - action_search_restaurants
    - utter_send_mail
* deny
    - utter_goodbye
    - action_slotreset
    - reset_slots

## interactive_story_12
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_check_location
    - slot{"valid_location": "true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs.300 to 700"}
    - slot{"budget": "Rs.300 to 700"}
    - action_search_restaurants
    - utter_send_mail
* deny
    - utter_goodbye

## interactive_story_13
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian", "location": "hyderabad"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "hyderabad"}
    - action_check_location
    - slot{"valid_location": "true"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs.300 to 700"}
    - slot{"budget": "Rs.300 to 700"}
    - action_search_restaurants
    - utter_send_mail
* affirm
    - utter_ask_email
* send_email{"email": "dinesh@outlook.com"}
    - slot{"email": "dinesh@outlook.com"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_14
* restaurant_search{"cuisine": "South Indian", "budget": "More than 700", "location": "goa"}
    - slot{"budget": "More than 700"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "goa"}
    - action_check_location
    - slot{"valid_location": "true"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - action_search_restaurants
    - utter_send_mail
* affirm
    - utter_ask_email
* send_email{"email": "dinesh@outlook.com"}
    - slot{"email": "dinesh@outlook.com"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_15
* restaurant_search{"cuisine": "american", "location": "Pondicherry"}
    - slot{"cuisine": "american"}
    - slot{"location": "Pondicherry"}
    - action_check_location
    - slot{"valid_location": "true"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_send_mail
* deny
    - utter_goodbye
    - action_slotreset
    - reset_slots

## interactive_story_16
* restaurant_search{"cuisine": "mexican", "budget": "More than 700", "location": "mumbai"}
    - slot{"budget": "More than 700"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"valid_location": "true"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - action_search_restaurants
    - utter_send_mail
* send_email{"email": "ahbcdjk@dkj.com"}
    - slot{"email": "ahbcdjk@dkj.com"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_17
* greet
    - utter_greet
* restaurant_search{"budget": "Lesser than Rs.300", "location": "vellore"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"location": "vellore"}
    - action_check_location
    - slot{"valid_location": "true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - action_search_restaurants
    - utter_send_mail
* affirm
    - utter_ask_email
* send_email{"email": "testbot@ugrad.co.in"}
    - slot{"email": "testbot@ugrad.co.in"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_18
* restaurant_search{"location": "Vasai-Virar", "budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"location": "Vasai-Virar"}
    - action_check_location
    - slot{"valid_location": "true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - action_search_restaurants
    - utter_send_mail
* deny
    - utter_goodbye
    - action_slotreset
    - reset_slots

## interactive_story_19
* greet
    - utter_greet
* restaurant_search{"cuisine": "indian"}
    - slot{"cuisine": "indian"}
    - action_check_cuisine
    - slot{"valid_cuisine": "false"}
    - utter_Invalidcuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - utter_ask_location
* restaurant_search{"location": "Shimla"}
    - slot{"location": "Shimla"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs.300 to 700"}
    - slot{"budget": "Rs.300 to 700"}
    - action_search_restaurants
    - utter_send_mail
* affirm
    - utter_ask_email
* send_email{"email": "jdffk.12js@ngjg.co.in"}
    - slot{"email": "jdffk.12js@ngjg.co.in"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_20
* restaurant_search{"location": "gangtok"}
    - slot{"location": "gangtok"}
    - action_check_location
    - slot{"valid_location": "false"}
    - utter_locationNotServiced
* restaurant_search{"location": "mangalore"}
    - slot{"location": "mangalore"}
    - action_check_location
    - slot{"valid_location": "true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs.300 to 700"}
    - slot{"budget": "Rs.300 to 700"}
    - action_search_restaurants
    - utter_send_mail
* affirm
    - utter_ask_email
* send_email{"email": "dinesh@outlook.com"}
    - slot{"email": "dinesh@outlook.com"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_21
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian", "location": "Durg Bhilai"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Durg Bhilai"}
    - action_check_location
    - slot{"valid_location": "true"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs.300 to 700"}
    - slot{"budget": "Rs.300 to 700"}
    - action_search_restaurants
    - utter_send_mail
* send_email{"email": "dineshkumarjangid@gmail.com"}
    - slot{"email": "dineshkumarjangid@gmail.com"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots
* restaurant_search{"cuisine": "Chinese", "location": "Durg Bhilai"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Durg Bhilai"}
    - action_check_location
    - slot{"valid_location": "true"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs.300 to 700"}
    - slot{"budget": "Rs.300 to 700"}
    - action_search_restaurants
    - utter_send_mail
* send_email{"email": "dineshkumarjangid@gmail.com"}
    - slot{"email": "dineshkumarjangid@gmail.com"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_1
* restaurant_search{"location": "Delhi NCR"}
    - slot{"location": "Delhi NCR"}
    - action_check_location
    - slot{"valid_location": "true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "indonesian"}
    - slot{"cuisine": "indonesian"}
    - action_check_cuisine
    - slot{"valid_cuisine": "false"}
    - utter_Invalidcuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - slot{"location": "Delhi NCR"}
    - utter_send_mail
* affirm{"email": "dinesh@outlook.com"}
    - slot{"email": "dinesh@outlook.com"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian", "location": "Pune"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"valid_location": "true"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs.300 to 700"}
    - slot{"budget": "Rs.300 to 700"}
    - action_search_restaurants
    - utter_send_mail
* affirm
    - utter_ask_email
* send_email{"email": "mnit@ymail.com"}
    - slot{"email": "mnit@ymail.com"}
    - action_send_email
    - utter_sentmail
    - action_slotreset
    - reset_slots

## interactive_story_1
* restaurant_search{"cuisine": "thai", "location": "Bengaluru"}
    - slot{"cuisine": "thai"}
    - slot{"location": "Bengaluru"}
    - action_check_location
    - slot{"valid_location": "true"}
    - action_check_cuisine
    - slot{"valid_cuisine": "false"}
    - utter_Invalidcuisine
* restaurant_search{"cuisine": "continental"}
    - slot{"cuisine": "continental"}
    - action_check_cuisine
    - slot{"valid_cuisine": "false"}
    - utter_Invalidcuisine
* restaurant_search{"cuisine": "spanish"}
    - slot{"cuisine": "spanish"}
    - action_check_cuisine
    - slot{"valid_cuisine": "false"}
    - utter_Invalidcuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"valid_cuisine": "true"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs.300 to 700"}
    - slot{"budget": "Rs.300 to 700"}
    - action_search_restaurants
    - utter_send_mail
* deny
    - utter_goodbye
