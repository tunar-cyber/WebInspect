

def subdomain_bt(url, file_path, output_file=None):

    report = []

    parsed = urlparse(url)
    hostname = parsed.netloc
    scheme = parsed.scheme

    report.append("# Subdomain Enumeration Report")
    report.append("")
    report.append(f"Target: {url}")
    report.append("")
    
    response_code=requests.get(url);
    code=response_code.status_code;
    try:
     status = HTTPStatus(code).phrase
    except ValueError:
     status = "Unknown"
    
    report.append(f"Response: {code} ({status})");
    report.append("## Discovered Subdomains")
    report.append("")

    with open(file_path, "r") as f:
        for line in f:
            subdomain = line.strip()

            if not subdomain:
                continue

            target = f"{scheme}://{subdomain}.{hostname}"

            try:
                response = requests.get(target, timeout=3)

                print(f"[{response.status_code}] {target}")

                report.append(f"[{response.status_code}] {target}")

            except requests.RequestException:

                print(f"[ERR] {target}")

                report.append(f"[ERR] {target}")

    if output_file:

        with open(output_file, "w", encoding="utf-8") as f:

            f.write("\n".join(report))

        print(f"\n[+] Report saved to {output_file}")
               
