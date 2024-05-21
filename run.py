from core.build.create_app import create_app

def run():
    # app_name = input("app name: ")
    # description = input("description: ")
    # tech_stack = input("tech stack: ")

    app_name = "My Todo App"
    description = "Create app todo app with crud functionality"
    tech_stack = "Javascript"

    create_app(app_name, description, tech_stack)


run()