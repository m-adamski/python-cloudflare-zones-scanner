import sys
import argparse
import datetime


def main():
    # Define Argument Parser
    parser = argparse.ArgumentParser(description="The tool creates a list of DNS entries for all domains managed by Cloudflare")
    parser.add_argument("--auth-token", type=str, help="Cloudflare API Token with permission to read Zone and DNS entries")

    # Parse provided arguments
    try:
        print("Launch date: ", datetime.datetime.today())
        print("Reading the given arguments and generating the configuration")
        arguments = parser.parse_args()

    except argparse.ArgumentError:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
