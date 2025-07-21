# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['lab_15/autograder.py'],
    pathex=[],
    binaries=[],
    datas=[('lab_15/lab_15_assistant.py', '.'), ('lab_15/check.png', '.'), ('lab_15/redX.png', '.')],
    hiddenimports=['lab_15_assistant', 'astor', 'trace', 'multiprocessing', 'PyQt6.QtWidgets', 'csc170_lists_data', 'input_override'],
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
    name='lab_15_Linux_Autograder',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
