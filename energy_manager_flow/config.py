TESTING_BACK = True
MOCK_SENSORS = True

if TESTING_BACK:
    base_backend_url = "http://6d9c4fab.ngrok.io" # "http://localhost:8000"
else:
    base_backend_url = "https://back.comunitaria.com"


community_token = "c78760cf-7716-4045-8d30-186821d9c8f5"