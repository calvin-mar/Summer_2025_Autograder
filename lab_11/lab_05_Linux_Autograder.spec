# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['lab_05/lab_05_autograder.py'],
    pathex=[],
    binaries=[],
    datas=[('lab_05/autograder_assistant.py', '.')],
    hiddenimports=['autograder_assistant.py', 'trace', 'multiprocessing', 'PyQt6.QtWidgets'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='lab_05_Linux_Autograder',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
