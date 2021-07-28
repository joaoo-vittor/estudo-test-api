from api_routes_for_test import BASE_URL
from json import loads
from locust import HttpUser, task, between


class SEFAZApiTest(HttpUser):
    """
    Class to Test SEFAZ-API
    """

    wait_time = between(0.5, 2.0)

    @task
    def test_route_test(self):
        with self.client.get(f"{BASE_URL}/test", catch_response=True) as response:
            data = loads(response.text)

            if not "msg" in data:
                response.failure("'msg' not existis in response")

    @task
    def test_route_not_exists(self):
        with self.client.get(
            f"{BASE_URL}/route_not_exists", catch_response=True
        ) as response:

            if response.status_code == 404:
                response.success()

    @task
    def test_route_home(self):
        mock_id = 1
        with self.client.get(
            f"{BASE_URL}/home?id={mock_id}", catch_response=True
        ) as response:
            data = loads(response.text)

            if not "id" in data.keys():
                response.failure("No response deve exitir a chave 'id'")

            if not (data["id"], int):
                response.failure(
                    "O valor referente a chave 'id' deve ser instancia de int"
                )

            if data["id"] != mock_id:
                response.failure(f"O valor de 'id' deve ser igual a {mock_id}")

            if response.status_code == 200:
                response.success()
