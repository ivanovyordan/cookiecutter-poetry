import os


def remove_file(filepath):
    PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


os.system("poetry install")
os.system("poetry add --group dev {{ cookiecutter.dev_dependencies }}")

if "{{ cookiecutter.dependencies }}" != "":
    os.system("poetry add {{ cookiecutter.dependencies }}")

if "Not open source" == "{{ cookiecutter.open_source_license }}":
    remove_file("LICENSE")

os.system("touch .env")
os.system("git init .")
os.system("poetry run pre-commit install")
os.system("git add .")
os.system("git commit -m 'Initial commit'")
