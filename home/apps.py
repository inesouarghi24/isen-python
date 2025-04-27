from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

if __name__ == "__main__":
    from urls import register_routes
    app = Flask(__name__)
    register_routes(app)
    app.run(host="127.0.0.1", port=8000)



