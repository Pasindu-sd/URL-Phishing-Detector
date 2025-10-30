# simple_phish_check.py
import re
import socket
import ssl

def get_domain(url):
    url = url.lower().strip()
    url = re.sub(r"^https?://", "", url)
    domain = url.split('/')[0].split(':')[0]
    return domain

def has_ssl_cert(domain, timeout=5):
    """Try to fetch SSL certificate from port 443.
       Returns certificate 'notAfter' string if found, else None."""
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.settimeout(timeout)
            s.connect((domain, 443))
            cert = s.getpeercert()
        return cert.get("notAfter")
    except Exception:
        return None

def simple_check(url):
    print(f"Analyzing: {url}")
    issues = []

    # basic pattern checks
    if len(url) > 75:
        issues.append("URL too long")
    if url.count('-') > 3:
        issues.append("Many hyphens")
    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        issues.append("Contains raw IP address")
    fake_brands = ['paypal','facebook','google','microsoft','bank']
    for b in fake_brands:
        if b in url.lower() and '-' in url:
            issues.append(f"Suspicious brand pattern: {b}")

    # domain + DNS
    domain = get_domain(url)
    try:
        ip = socket.gethostbyname(domain)
        print("Resolved IP:", ip)
        if ip.startswith(("10.","172.","192.168.")):
            issues.append("Resolves to private IP")
    except Exception as e:
        issues.append("DNS resolution failed")

    # SSL check
    cert_expiry = has_ssl_cert(domain)
    if cert_expiry:
        print("SSL cert found, notAfter:", cert_expiry)
    else:
        issues.append("No SSL certificate on port 443 or couldn't fetch it")

    if issues:
        print("\nSUSPICIOUS FOUND:")
        for it in issues:
            print(" -", it)
    else:
        print("\nLooks okay (basic checks)")

    return issues

if __name__ == "__main__":
    url = input("Enter URL: ").strip()
    simple_check(url)
