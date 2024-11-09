from locust import HttpUser, between, task

class APIUser(HttpUser):
    # Correctly defining wait_time as a class attribute
    wait_time = between(1, 2)
    host = 'http://localhost:5001'

    def on_start(self):
        """This method is called when a simulated user starts. We will use it to login and get the token."""
        login_data = {
            "username": "admin",
            "password": "admin"
        }
        # Send POST request to log in and obtain the JWT token
        response = self.client.post("/login", json=login_data)
        if response.status_code == 200:
            # Store the token for later use in the Authorization header
            self.token = response.json()["token"]
        else:
            print("Failed to log in and get the token")

    @task
    def get_root(self):
        """Access the root endpoint with authentication"""
        headers = {"Authorization": f"Bearer {self.token}"}
        self.client.get("/", headers=headers)

    @task
    def get_resource1(self):
        """Access the /resource1 endpoint with authentication"""
        headers = {"Authorization": f"Bearer {self.token}"}
        self.client.get("/resource1", headers=headers)

    @task
    def get_heavy_resource(self):
        """Access the /heavy-resource endpoint with authentication"""
        headers = {"Authorization": f"Bearer {self.token}"}
        self.client.get("/heavy-resource", headers=headers)