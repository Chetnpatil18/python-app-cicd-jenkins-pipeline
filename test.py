import app
import re

def test_hello():
    app.app.testing = True
    client = app.app.test_client()

    rv = client.get('/')
    assert rv.status_code == 200

    message = rv.data.decode()
    start = re.search("<h1>", message).start()
    end = re.search("</h1>", message).start()
    message = message[start + 4:end]

    assert message == "hello dear, Lets have some fun!!"


def test_name():
    app.app.testing = True
    client = app.app.test_client()

    name = "alice"
    rv = client.get(f'/{name}')
    assert rv.status_code == 200

    message = rv.data.decode()
    start = re.search("<h1>", message).start()
    end = re.search("</h1>", message).start()
    message = message[start + 4:end]

    assert message == "alice: A nerd"
