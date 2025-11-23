from locust import HttpUser, task, between

class MLLoadTest(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_prediction(self):
        # Read test image from SAME folder as locustfile.py
        with open("test_image.jpg", "rb") as f:
            img = f.read()

        self.client.post(
            "/predict",
            files={"file": ("test_image.jpg", img, "image/jpeg")}
        )
