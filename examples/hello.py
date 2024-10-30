#!/usr/bin/env python3

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
