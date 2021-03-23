import os

os.system("poetry install")
os.system("poetry add --dev {{ cookiecutter.dev_dependencies }}")


if "{{ cookiecutter.dependencies }}" != "":
    os.system("poetry add {{ cookiecutter.dependencies }}")

os.system("git init .")
os.system("poetry run pre-commit install")
os.system("git add .")
os.system("git commit -m 'Initial commit'")
