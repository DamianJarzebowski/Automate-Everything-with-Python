from pathlib import Path

root_dir = Path('.')
search_term = 'abc'

for path in root_dir.rglob("*"):
  if path.is_file():
    if search_term in path.stem:
      print(path.absolute())
