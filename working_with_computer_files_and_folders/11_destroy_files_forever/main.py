from pathlib import Path

root_dir = Path('files')

for path in root_dir.glob("*.csv"):
  with open(path, 'wb') as file:
    file.write(b'')
  path.unlink()