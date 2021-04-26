import flask
from API.AboutSystem import AboutSystem

app = flask.Flask(__name__)
app.config["DEBUG"] = True


class API:
    @staticmethod
    @app.route('/', methods=['GET'])
    def home():
        return "<h1>SysAdmin REST</h1><p>" \
               "This site is an API for distant reading of System information.</p>"

    @staticmethod
    @app.route('/api/hello_world', methods=['GET'])
    def api_hello_world():
        return {"Hallo": "world"}

    @staticmethod
    @app.route('/api/system_info', methods=['GET'])
    def api_system_info():
        return AboutSystem.get_total_info()

    @staticmethod
    @app.route('/api/cpu_usage', methods=['GET'])
    def api_cpu_usage():
        return {"cpu_usage": AboutSystem.get_cpu_usage()}

    @staticmethod
    @app.route('/api/mem_usage', methods=['GET'])
    def api_mem_usage():
        return {"cpu_usage": AboutSystem.get_mem_usage()}


app.run()
