from unittest import TestCase
from API.Docker import Docker


class TestDocker(TestCase):
    def test_get_docker_images(self):
        Docker.get_docker_images()
