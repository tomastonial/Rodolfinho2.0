import cx_Freeze

executaveis = [
        cx_Freeze.Executable(
            script="main.py",
            icon="bases/rodolfo.ico",
            target_name="Rodolfinho"
        )
]

cx_Freeze.setup(
    name = "Rodolfo",
    options = {
        "build_exe":{
            "packages":["pygame"],
            "include_files":["bases","recursos"]
        }
    }, executables = executaveis
)
