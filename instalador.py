import PyInstaller.__main__

PyInstaller.__main__.run(
    [
        'main.py',
        '--windowed',
        '--noconsole',
        '--onefile',
        '--name=5N_PROC_SPED_ICMS_IPI',
        '--icon=5N_icone_padrao.ico'
    ]
)