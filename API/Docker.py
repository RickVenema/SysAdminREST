import docker

client = docker.from_env()


class Docker:
    @staticmethod
    def get_docker_images():
        output = [f"{item}" for item in client.images.list()]
        return output

    @staticmethod
    def pull_docker_image(image_name):
        pass

    @staticmethod
    def run_docker_image(image_name):
        pass
