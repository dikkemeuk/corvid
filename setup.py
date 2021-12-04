from cx_Freeze import setup, Executable

buildOptions = {
    "includes": ["numpy", "PIL", "vmf_tool", "vpk"],
    "include_files": ["res/"]
}

setup(
    name="Corvid",
    version="1.0",
    description="Source Engine to Call of Duty map converter",
    options={"build_exe": buildOptions},
    executables=[
        Executable(
            "app.py",
            target_name="Corvid.exe",
            icon="res/icon.ico",
            base=None
            )
    ]
)