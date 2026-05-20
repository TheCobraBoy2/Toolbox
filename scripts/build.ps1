& "C:/Users/lando/PycharmProjects/Toolbox/.venv/Scripts/pyinstaller.exe" `
    "C:/Users/lando/PycharmProjects/Toolbox/main.py" `
    --name "Toolbox" `
    --onefile `
    -w `
    --hidden-import patchers `
    --hidden-import my_things `
    --hidden-import applications `
    --distpath "C:/Users/lando/PycharmProjects/Toolbox/dist" `
    --add-data "C:/Users/lando/PycharmProjects/Toolbox/resources/*;resources" `
    --log-level DEBUG