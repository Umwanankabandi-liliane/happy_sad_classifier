from locust import HttpUser, task, between

class EmotionClassifierUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_prediction(self):
        """
        Sends a test request to the /predict endpoint.
        You must place a sample image named 'test.jpg' inside this folder.
        """
        with open("test.jpg", "rb") as f:
            files = {"file": ("test.jpg", f, "image/jpeg")}
            self.client.post("/predict", files=files)
