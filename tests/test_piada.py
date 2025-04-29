import requests # type: ignore

URL = "https://official-joke-api.appspot.com/random_joke"

def test_100_request_unique_id():
    ids = set()
    for _ in range(100):
        response = requests.get(URL)
        assert response.status_code == 200
        data = response.json()

        assert "type" in data and isinstance(data["type"],str) and data["type"].strip() != "", "campo 'type' inválido"
        assert "setup" in data and isinstance(data["setup"], str) and data["setup"].strip() !="", "Campo 'setup' inválido"
        assert "punchline" in data and isinstance(data["punchline"], str) and data["punchline"].strip() != "", "Campo 'punchline' inválido"
        assert "id" in data and isinstance (data["id"], int), "Campo 'id inválido"

        assert data["id"] not in ids, f"ID duplicado encontrado: {data['id']}"
        ids.add(data["id"])

        

