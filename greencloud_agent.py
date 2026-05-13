from datetime import datetime
from colorama import Fore, Style, init

init()

TEMP_LIMIT = 75
CPU_LIMIT = 85
POWER_LIMIT = 550


def check_server(server_id, cpu, temperature, power):

    warnings = []
    suggestions = []

    if temperature > TEMP_LIMIT:
        warnings.append("High temperature")
        suggestions.append(
            "Improve cooling or move workload to another server."
        )

    if cpu > CPU_LIMIT:
        warnings.append("High CPU load")
        suggestions.append(
            "Shift some tasks to a less busy virtual server."
        )

    if power > POWER_LIMIT:
        warnings.append("High power usage")
        suggestions.append(
            "Review workload efficiency to reduce energy waste."
        )

    print("\n===================================")
    print(" GreenCloud AI Monitoring Agent")
    print("===================================")
    print(f"Scan Time: {datetime.now()}")
    print("-----------------------------------")

    print(f"Server ID: {server_id}")
    print(f"CPU Load: {cpu}%")
    print(f"Temperature: {temperature}°C")
    print(f"Power Usage: {power}W")

    if warnings:

        print(Fore.RED + "Status: WARNING" + Style.RESET_ALL)

        print("Issues Found:")

        for warning in warnings:
            print(Fore.RED + f"- {warning}" + Style.RESET_ALL)

        print(Fore.CYAN + "AI Recommendation:" + Style.RESET_ALL)

        for suggestion in suggestions:
            print(
                Fore.CYAN
                + f"AI Agent Suggestion: {suggestion}"
                + Style.RESET_ALL
            )

    else:

        print(Fore.GREEN + "Status: Healthy" + Style.RESET_ALL)

        print(Fore.CYAN + "AI Recommendation:" + Style.RESET_ALL)

        print(
            Fore.GREEN
            + "AI Agent Suggestion: No action needed. Server is running efficiently."
            + Style.RESET_ALL
        )


def main():

    print(Fore.CYAN + "System Admin AI Agent Started" + Style.RESET_ALL)

    while True:

        print("\nManual Server Health Check Mode")
        print("-----------------------------------")

        server_id = input("Enter Server ID: ")
        cpu = int(input("Enter CPU Load (%): "))
        temperature = int(input("Enter Temperature (°C): "))
        power = int(input("Enter Power Usage (W): "))

        check_server(server_id, cpu, temperature, power)

        again = input("\nCheck another server? (yes/no): ")

        if again.lower() != "yes":

            print(
                Fore.YELLOW
                + "\nSystem Admin AI Agent Stopped"
                + Style.RESET_ALL
            )

            break


main()