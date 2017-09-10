# -*- mode: python -*-

block_cipher = None


a = Analysis(['visualizeresults.py'],
             pathex=['/Users/devansh20la/Documents/ML lab/Melanoma/Visualization stuff/Visualization UI'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='visualizeresults',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='ndowed')
app = BUNDLE(exe,
             name='visualizeresults.app',
             icon='ndowed',
             bundle_identifier=None)
