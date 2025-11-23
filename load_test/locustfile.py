from locust import HttpUser, task, between

class MLLoadTest(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_prediction(self):
        # Read test image
        with open("test_image.jpg", "rb") as f:
            img = f.read()

        # Send image to cloud API
        self.client.post(
            "/predict",
            files={"file": ("test_image.jpg", img, "image/jpeg")}
        )
