#!/usr/bin/env python3

import fastcommand


@fastcommand.command("hello", help="say hello")
def command_hello(options):
    print("Hello, World!")


def main():
    cli = fastcommand.CommandParser(description="Simple fastcommand example.")
    cli.use_logging(format="[%(levelname)s] %(message)s")
    cli.run()


if __name__ == "__main__":
    main()
