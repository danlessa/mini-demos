import click
from pathlib import Path

@click.command()
@click.option("--input", default="data")
@click.option("--output", default="data")
def load_data(input, output) -> str:
    with open(Path(input) / 'some_data.txt', 'r') as fid:
        text = fid.read()
    with open(Path(output) / 'new_data.txt', 'w') as fid:
        fid.write(text)
    return text

if __name__ == '__main__':
    load_data()

