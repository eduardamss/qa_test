from locust import HttpUser, task, between # type: ignore

class JokesLoadTest(HttpUser):  
    wait_time = between(1, 3)

    @task
    def get_random_joke(self):  
        with self.client.get("/random_joke", catch_response=True) as response:  
            if response.status_code != 200:
                response.failure("Status code != 200")
            else:
                try:
                    data = response.json()
                    assert "type" in data
                    assert "setup" in data
                    assert "punchline" in data
                    assert "id" in data
                    response.success()
                except Exception as e:
                    response.failure(f"Erro na validação: {e}")
