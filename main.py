import requests

api_base_url = "https://api.stack.truckit.com/"
api_sign_in_endpoint = "api/2/signin"
api_sign_in_url = f"{api_base_url}{api_sign_in_endpoint}"
simulate_movement_ep = "api/1/demo/simulate-movement"
api_simulate_movement_url = f"{api_base_url}{simulate_movement_ep}"
trucks_ep = "api/2/trucks"
api_trucks_url = f"{api_base_url}{trucks_ep}"

username = "jnebeker"
password = "welcome"

signin_payload = {"username": username, "password": password}
response = requests.post(api_sign_in_url, json=signin_payload)

