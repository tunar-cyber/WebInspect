import requests

from urllib.parse import urljoin

from http import HTTPStatus



def directory_enumeration(base_url, file_path, output_file=None):

    report = []

    print("-----------------------------")
    print("Directory Enumeration")
    print("-----------------------------")

    report.append("# Directory Enumeration Report")
    report.append("")
    report.append(f"Target: {base_url}")
    
    response_code=requests.get(base_url);
    code=response_code.status_code;
    try:
     status = HTTPStatus(code).phrase
    except ValueError:
     status = "Unknown"
    
    report.append(f"Response: {code} ({status})");
    report.append("## Discovered Directories")
    report.append("")

    with open(file_path, "r") as f_p:

        for line in f_p:

            directory = line.strip()

            if not directory:
                continue

            target = urljoin(base_url.rstrip("/") + "/", directory)

            try:

                response = requests.get(target, timeout=3)

                if response.status_code != 404:

                    size = len(response.content)

                    print(f"[{response.status_code}] {target} ({size} bytes)")

                    report.append(
                        f"[{response.status_code}] {target} ({size} bytes)"
                    )

            except requests.RequestException:

                pass

    if output_file:

        with open(output_file, "w", encoding="utf-8") as f:

            f.write("\n".join(report))

        print(f"\n[+] Report saved to {output_file}")
    
