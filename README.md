# Phishing-Detector


that checks if a website is fake or dangerous - like those fake login pages that steal passwords.

That checks if a website is fake or dangerous - like those fake login pages that steal passwords.
The program is working! Now you have a basic phishing detector.

---

### Test with these examples:
```
facebook.com ← Should be safe

facebook-security-login.com ← Should be suspicious

192.168.1.1/login ← Should be suspicious

my-small-business.com ← Should be safe

http://login-facebook-security-update.com/login 

```

### Output (Example 1):
```
Enter URL: http://login-facebook-security-update.com/login       
Analyzing: http://login-facebook-security-update.com/login       

SUSPICIOUS FOUND:
 - Suspicious brand pattern: facebook
 - DNS resolution failed
 - No SSL certificate on port 443 or couldn't fetch it
```

### Output (Example 2):
```
Enter URL: https://www.google.com
Analyzing: https://www.google.com
Resolved IP: 142.250.77.36
SSL cert found, notAfter: Dec 24 14:35:28 2025 GMT

Looks okay (basic checks)
```

