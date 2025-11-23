from locust import HttpUser, task, between
import os

class MLLoadTest(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_prediction(self):
        # Full correct path for Windows setup
        test_path = os.path.join("load_test", "test_image.jpg")

        with open(test_path, "rb") as f:
            img = f.read()

        self.client.post(
            "/predict",
            files={"file": ("test_image.jpg", img, "image/jpeg")}
        )
