#!/usr/bin/env python3

import fastcommand


@fastcommand.command("hello", help="say hello")
def command_hello(options):
    print("Hello, World!")


@fastcommand.command("goodbye", help="say goodbye", arguments=[
    fastcommand.Argument("name"),
    fastcommand.Argument("--wave", "-w", action="store_true", default=False)
])
def command_goodbye(options):
    print(f"Goodbye, {options.name}!")
    if options.wave:
        print("👋")


def main():
    cli = fastcommand.CommandParser(description="Simple fastcommand example.")
    cli.use_logging(format="[%(levelname)s] %(message)s")
    cli.run()


if __name__ == "__main__":
    main()
