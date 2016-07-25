import time

from skiplagged import Skiplagged


if __name__ == '__main__':
    client = Skiplagged()
    
    bounds = (
              (40.76356269219236, -73.98657795715332), # Lower left lat, lng
              (40.7854671345488, -73.95812508392333) # Upper right lat, lng
              ) # Central park, New York City
#     bounds = client.get_bounds_for_address('Central Park, NY')
    
    while 1:
        try:
            # Log in with a Google or Pokemon Trainer Club account
        #     print client.login_with_google('GOOGLE_EMAIL', 'PASSWORD')
            print client.login_with_pokemon_trainer('trenggalek', 'klik123kali')
            
            # Get specific Pokemon Go API endpoint
            print client.get_specific_api_endpoint()
            
            # Get profile
            print client.get_profile()
            
            # Find pokemon
            for pokemon in client.find_pokemon(bounds):
                print pokemon
        except Exception as e:
            print("Exception: {0} {1}".format(e.message, e.args))
            time.sleep(1)
            
