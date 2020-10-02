import sys
import argparse
import cloudflare.cloudflare as cloudflare
import workbook.workbook as workbook


def main():
    # Define Argument Parser
    parser = argparse.ArgumentParser(description="The tool creates a list of DNS entries for all domains managed by Cloudflare")
    parser.add_argument("token", type=str, help="Cloudflare API Token with permission to read Zone and DNS entries")
    parser.add_argument("--xlsx-file", type=str, help="The name of the resulting file in XLSX format")

    # Parse provided arguments
    try:
        arguments = parser.parse_args()

        if arguments.token is not None:
            wbook = workbook.workbook()
            zones = cloudflare.zones(arguments.token)

            # Move every found Zone
            for zone in zones:
                print("Zone:\n%s\n\nDNS Records:" % zone)
                workbook.zone(wbook, zone)

                # Get DNS Records for current Zone
                zone.records = cloudflare.records(arguments.token, zone)

                # Move every found DNS Record
                for record in zone.records:
                    print(record)
                    workbook.record(wbook, zone, record)

                print()

            # Save workbook
            if arguments.xlsx_file is not None:
                workbook.save(wbook, arguments.xlsx_file)

    except argparse.ArgumentError:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
