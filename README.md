# quickcli

Python module for defining multi-command cli programs

## Description

The `quickcli` module is a lightweight wrapper over `argparse` which aims to make it easier to write multi-command cli programs and utilities. It does so by providing convenience decorators that allow for quickly defining sub-commands.

## Usage

```python
import quickcli


@quickcli.command("hello", help="say hello")
def command_hello(options):
    print("Hello, World!")


def main():
    cli = quickcli.CommandParser(description="Simple quickcli example.")
    cli.use_logging(format="[%(levelname)s] %(message)s")
    cli.run()


if __name__ == "__main__":
    main()
```
