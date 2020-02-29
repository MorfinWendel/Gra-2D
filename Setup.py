import cx_Freeze

executables = [cx_Freeze.Executable('Main.py')]
cx_Freeze.setup(
    name="Kapitan Bomba: Zemsta Dupy",
    options={"build exe": {"packages": ["pygame"],
                           "include_files": ['orzel.png', "fail.wav", 'gra.wav', 'menu.mp3',
                                             'kosmos.png', 'planet.png']
                           }},
    executables=executables
)
