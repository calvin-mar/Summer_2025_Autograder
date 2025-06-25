# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['lab_06 (Linux)/autograder.py'],
    pathex=[],
    binaries=[],
    datas=[('lab_06 (Linux)/lab_06 (Linux)_assistant.py', '.'), ('lab_06 (Linux)/check.png', '.'), ('lab_06 (Linux)/redX.png', '.')],
    hiddenimports=['lab_06 (Linux)_assistant', 'astor', 'trace', 'multiprocessing', 'PyQt6.QtWidgets', 'csc170_lists_data', 'input_override'],
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
    name='lab_06 (Linux)_Linux_Autograder',
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
