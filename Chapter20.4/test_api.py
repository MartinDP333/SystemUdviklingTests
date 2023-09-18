import requests

ENDPOINT = "https://rocky-gorge-77460-611a79604e3d.herokuapp.com"
"""
Tests will create a user (test will fail if user already exists)
Test then tests if it is possible to login (method can be called to retrieve CWT token)
Then it checks users and quotes
After that we post a quote while getting the Newest quote id
We then retrieve the newest quote
Then we test if we can change the quote
Lastly we delete the posted quote
This should result in 1 failed and 7 passed tests (8 passed if new user)
There are also 3 warnings which are about the fact i use a return statement(which it complains will not work in the future)
"""

login_payload = {
    "uid": "MartinD",
    "pwd": "123456"
}

def test_register_user():
    response = requests.post(ENDPOINT + "/register", json=login_payload)
    assert response.status_code == 201, "User either already exists or an error occured"

    data = response.json()
    print(data)

def test_login_user():
    response = requests.post(ENDPOINT + "/login", json=login_payload)
    assert response.status_code == 200, "Failed to login"
    data = response.json()
    print(data)
    return data

def test_get_user():
    response = requests.get(ENDPOINT + "/users")
    assert response.status_code == 200, "Failed to get users"
    data = response.json()
    print(data)
    return data
def test_get_quotes():
    response = requests.get(ENDPOINT + "/quotes")
    assert response.status_code == 200
    data = response.json()
    return data

quote_payload = {
    "quote": "Quote",
    "attribution": "Martin D"
}
def test_post_quote():
    global qid # Used to get new quotes id. Makes it easier to secure tests work (also reduces the need for manual input)
    myToken = test_login_user()
    head = {"Authorization": "{}".format(myToken)}
    headers = {"content-type": "application/json"}  
    response = requests.post(ENDPOINT + "/quote", json=quote_payload, headers=head)
    assert response.status_code == 201, "Failed to post quote"

    # The .get method is white but it still works... Might just be my code editor being weird?
    qid = test_get_quotes()["quotes"][-1].get("qid") 
    print(qid)

def test_get_quote():
    response = requests.get(f"{ENDPOINT}/quote/{qid}")
    data = response.json()
    print(data)
    assert response.status_code == 200, "Failed to get specified quote"

put_quote_payload = {
    "quote": "New quote",
    "attribution": "Martin D"
}

def test_put_quote():
    myToken = test_login_user()
    head = {"Authorization": "{}".format(myToken)}
    headers = {"content-type": "application/json"}
    response = requests.put(f"{ENDPOINT}/quote/{qid}", json=put_quote_payload, headers=head)
    print(response.status_code)
    assert response.status_code == 204, "Failed to put replacement quote"

def test_delete_quote():
    myToken = test_login_user()
    head = {"Authorization": "{}".format(myToken)}
    headers = {"content-type": "application/json"}
    response = requests.delete(f"{ENDPOINT}/quote/{qid}", headers=head)
    assert response.status_code == 204, "Failed to delete quote"
