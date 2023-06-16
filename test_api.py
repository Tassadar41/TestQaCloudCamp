import requests

ENDPOINT = "https://jsonplaceholder.typicode.com/"

#CORRECT STATUS CODE RETUTN
def test_GET_posts_status_code():
    response = requests.get(ENDPOINT+'posts')
    assert response.status_code == 200
    pass

def test_GET_post_status_code():
    response = requests.get(ENDPOINT+'posts/1')
    assert response.status_code == 200
    pass

def test_POST_posts_status_code():
    response = requests.post(ENDPOINT+'posts')
    assert response.status_code == 201 or response.status_code == 200
    pass

def test_DELETE_posts_status_code():
    response = requests.delete(ENDPOINT+'posts/1')
    assert response.status_code == 200 or response.status_code == 202 or response.status_code == 204
    pass

#CORECT DATA MODEL

def test_GET_posts_data_structure():
    response = requests.get(ENDPOINT + 'posts')
    data_structure = ["userId", "id", "title", "body"]

    response_dict = response.json()
    list_obj = response_dict[0]
    list_obj_keys = list(list_obj.keys())

    assert list_obj_keys == data_structure
    pass

def test_GET_post_data_structure():
    response = requests.get(ENDPOINT + 'posts/1')
    data_structure = ["userId", "id", "title", "body"]

    response_dict = response.json()
    keys = list(response_dict.keys())

    assert keys == data_structure
    pass



#CORECT HEADERS

def test_GET_posts_headers():
    response = requests.get(ENDPOINT + 'posts')

    assert response.headers.get('content-type') == "application/json; charset=utf-8"
    assert response.headers.get('connection') == "keep-alive"
    assert response.headers.get('cache-control') == "max-age=43200"
    assert response.headers.get('expires') == "-1"
    assert response.headers.get('access-control-allow-credentials') == "true"

    pass

def test_GET_post_headers():
    response = requests.get(ENDPOINT + 'posts/1')

    assert response.headers.get('content-type') == "application/json; charset=utf-8"
    assert response.headers.get('connection') == "keep-alive"
    assert response.headers.get('cache-control') == "max-age=43200"
    assert response.headers.get('expires') == "-1"
    assert response.headers.get('access-control-allow-credentials') == "true"

    pass

def test_POST_post_headers():
    response = requests.post(ENDPOINT + 'posts')

    assert response.headers.get('content-type') == "application/json; charset=utf-8"
    assert response.headers.get('connection') == "keep-alive"
    assert response.headers.get('cache-control') == "no-cache"
    assert response.headers.get('expires') == "-1"
    assert response.headers.get('access-control-allow-credentials') == "true"


    pass

def test_DELETE_post_headers():
    response = requests.delete(ENDPOINT + 'posts/1')

    assert response.headers.get('content-type') == "application/json; charset=utf-8"
    assert response.headers.get('connection') == "keep-alive"
    assert response.headers.get('cache-control') == "no-cache"
    assert response.headers.get('expires') == "-1"
    assert response.headers.get('access-control-allow-credentials') == "true"

    pass

#RESPONSE TAKE IN TIME

def test_GET_posts_timeout():
    response = requests.get(ENDPOINT + 'posts', timeout=1)
    assert response.status_code == 200
    pass

def test_GET_post_timeout():
    response = requests.get(ENDPOINT+'posts/1', timeout=1)
    assert response.status_code == 200
    pass

def test_POST_post_timeout():
    response = requests.post(ENDPOINT+'posts', timeout=1)
    assert response.status_code == 201 or response.status_code == 200
    pass

def test_DELETE_post_timeout():
    response = requests.delete(ENDPOINT+'posts/1', timeout=1)
    assert response.status_code == 200 or response.status_code == 202 or response.status_code == 204
    pass

#RESPONSE ERROR

def test_GET_post_response_error():
    response = requests.get(ENDPOINT+'posts/101')
    assert response.status_code == 404
    pass

def test_DELETE_post_response_error():
    response = requests.delete(ENDPOINT+'posts/101')
    assert response.status_code == 404
    pass


#RESPONSE ERROR IN TIME

def test_GET_post_response_error_timeout():
    response = requests.get(ENDPOINT+'posts/101', timeout=1)
    assert response.status_code == 404
    pass

def test_DELETE_post_response_error_timeout():
    response = requests.delete(ENDPOINT+'posts/101', timeout=1)
    assert response.status_code == 404
    pass



#CORRECT RESPONSE DATA

def test_GET_post_response_data():
    response = requests.get(ENDPOINT + 'posts/1')
    expected_data = {
                        "userId": 1,
                        "id": 1,
                        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
                    }
    response_data = response.json()
    assert expected_data == response_data
    pass

def test_POST_post_response_data():
    response = requests.post(ENDPOINT + 'posts')
    expected_data = {
                        "id": 101,
                    }
    response_data = response.json()
    assert expected_data == response_data
    pass

def test_DELETE_post_response_data():
    response = requests.post(ENDPOINT + 'posts/1')
    expected_data = {}
    response_data = response.json()
    assert expected_data == response_data
    pass
