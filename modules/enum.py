import requests
from colorama import Fore, Style



def basic_info(addr, output_file=None):

    report = []

    print("------------------------")
    print(f"Enumerating {addr}\n")

    response = requests.get(addr)

    status_code = response.status_code
    response_time = response.elapsed.total_seconds() * 1000
    response_headers = response.headers

    print("-------------------------")
    print(f"Status : [{status_code}]")
    print(f"Response Time : {response_time:.2f} ms")

    report.append("# WebInspect Report")
    report.append("")
    report.append(f"Target: {addr}")
    report.append(f"Status Code: {status_code}")
    report.append(f"Response Time: {response_time:.2f} ms")
    report.append("")

    print("--------------------------")
    print("General Response Headers")
    print("--------------------------")

    report.append("## Response Headers")

    for k, v in response_headers.items():

        print(f"{k}: {v}")

        report.append(f"{k}: {v}")

    print("\n-----------------------------")
    print("Useful Server Information")
    print("-----------------------------")

    report.append("")
    report.append("## Server Fingerprint")

    interesting_headers = [
        "Server",
        "X-Powered-By",
        "Content-Type",
        "Set-Cookie",
        "Content-Encoding"
    ]

    for header in interesting_headers:

        value = response_headers.get(header, "Not Found")

        print(f"{header}: {value}")

        report.append(f"{header}: {value}")

    print("\n-----------------------------")
    print("Security Headers")
    print("-----------------------------")

    report.append("")
    report.append("## Security Headers")

    security_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
        "Permissions-Policy"
    ]

    for header in security_headers:

        if header in response_headers:

            print(f"{Fore.GREEN}[✓]{Style.RESET_ALL} {header}")

            report.append(f"[✓] {header}")

        else:

            print(f"{Fore.RED}[✗]{Style.RESET_ALL} {header}")

            report.append(f"[✗] {header}")

    if output_file:

        with open(output_file, "w", encoding="utf-8") as f:

            f.write("\n".join(report))

        print(f"\n[+] Report saved to {output_file}")
