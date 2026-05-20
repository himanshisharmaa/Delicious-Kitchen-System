# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files


extra_datas = collect_data_files('certifi') + collect_data_files('razorpay')


a = Analysis(
    ['run_app.py'],
    pathex=[],
    binaries=[],
    datas=[('.env', '.'), ('db.sqlite3', '.'), ('static', 'static'), ('staticfiles', 'staticfiles'), ('media', 'media'), ('account', 'account'), ('custom_admin', 'custom_admin'), ('deliciousKitchen', 'deliciousKitchen'), ('menu', 'menu'), ('manage.py', '.')] + extra_datas,
    hiddenimports=[],
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
    name='DeliciousKitchen',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
