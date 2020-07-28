from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset
import zomatopy
import json

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config={"user_key":"cc9611902ebc9b782618ec2adefba4c9"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('budget')

        if budget == 'Lesser than Rs.300':
            min_price = 0
            max_price = 299
        elif budget == 'Rs.300 to 700':
            min_price = 300
            max_price = 700
        elif budget == "More than 700":
            min_price = 701
            max_price = 10000000
        else:
            min_price = 0
            max_price = 0

        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'chinese':25,'mexican':73,'american':1,'italian':55,'north indian':50,'south indian':85}
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)))
        d = json.loads(results)

        global top_10
        response=""

        if d['results_found'] == 0:
            response= "no results found"
        else:
            restaurants_list = [{"name":restaurant['restaurant']['name'],
        	                    "address":restaurant['restaurant']['location']['address'],
                                "avg_cost":restaurant['restaurant']['average_cost_for_two'],
        	                    "rating":restaurant['restaurant']['user_rating']['aggregate_rating']}
                                for restaurant in d['restaurants'] if restaurant['restaurant']['average_cost_for_two'] >= min_price and restaurant['restaurant']['average_cost_for_two'] <= max_price]
            top_10 = sorted(restaurants_list, key = lambda x: x['rating'], reverse = True)[:10]
            top_5 = top_10[:5]

            serial_no = 1
            for restaurant in top_5:
                response += "{0}.{1} in {2} has been rated {3} \n\n".format(serial_no,restaurant['name'], restaurant['address'],restaurant["rating"])
                serial_no += 1
                
        dispatcher.utter_message(response)
        
class ActionCheckLocation(Action):
    def name(self):
        return "action_check_location"

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot("location")
        location_list = ['ahmedabad','bengaluru','chennai','delhi ncr','hyderabad','kolkata','mumbai','pune','agra','ajmer','aligarh',
			'amravati','amritsar','asansol','aurangabad','bareilly','belgaum','bhavnagar','bhiwandi','bhopal','bhubaneswar',
			'bikaner','bokaro','chandigarh','coimbatore','cuttack','dehradun','dhanbad','durg bhilai','durgapur','erode',
			'firozabad','gorakhpur','gulbarga','guntur','gwalior','guwahati','hamirpur','hubli','dharwad','indore','jablpur',
			'jaipur','jalandhar','jammu','jamnagar','jamshedpur','jhansi','jodhpur','kakinada','kannur','kanpur','lucknow',
			'kollam','kochi','kolhapur','kozhikode','kurnool','ludhiana','madurai','malappuram','mathura','goa','mangalore',
			'meerut','moradabad','mysore','nagpur','nanded','nashik','nellore','patna','puducherry','purulia','allahabad',
			'raipur','rajkot','rajahmundry','ranchi','rourkela','salem','sangli','shimla','siliguri','solapur','surat',
			'trivandrum','thrissur','trichy','tiruppur','ujjain','bijapur','vadodara','varanasi','vijayawada','visakhapatnam',
			'vellore','warangal']
        location_list=[x.lower() for x in location_list]
        if location.lower() in location_list:
            return [SlotSet('valid_location',"true")]
        else:
            return [SlotSet("valid_location", "false")]
            
class ActionCheckCuisine(Action):
    def name(self):
        return "action_check_cuisine"

    def run(self, dispatcher, tracker, domain):
        cuisine = tracker.get_slot("cuisine")
        cuisine_list = ["Chinese","Mexican","Italian","American","South Indian","North Indian"]
        cuisine_list=[x.lower() for x in cuisine_list]
        if cuisine.lower() in cuisine_list:
            return [SlotSet('valid_cuisine',"true")]
        else:
            return [SlotSet("valid_cuisine", "false")]
           
class ActionSendEmail(Action):
    def name(self):
        return "action_send_email"
    
    def run(self, dispatcher, tracker, domain):
        import smtplib 
        recipient = tracker.get_slot('email')

        email_data=top_10
        response=""
        if len(email_data)>0:
            for restaurant in email_data:
                response=response+"Restaurant name: "+restaurant['name']+"\n"+"Restaurant Address: "+restaurant['address']+"\n"+"Average cost for two people: "+f"{restaurant['avg_cost']}"+"\n"+"Average Zomato Rating: "+f"{restaurant['rating']}"+"\n \n"
        else:
            response=response+"I am sorry, your search had no results, please try again."
        
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("foodiebot0620", "oneaccount")

        body = "Hi there, \n\nPlease find below the details of all the restaurants you enquired about: \n\n"
        subject = "Foodie Bot- Your list of top 10 restaurants"

        body += response
        message = f"Subject: {subject}\n\n{body}"

        try:
            s.sendmail("TestingBotmail", str(recipient), message)
            s.quit()
        except:
            dispatcher.utter_message(recipient)
        
        
class ResetAllSlots(Action):
    '''Reset all slots'''
    def name(self):
        return 'action_slotreset'

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]