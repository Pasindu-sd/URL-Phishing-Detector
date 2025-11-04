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
Extracted Domain: login-facebook-security-update.com

Possible Problems Found:
 - Suspicious brand pattern: facebook
 - DNS resolution failed (invalid or dead domain)
 - No SSL certificate or failed to fetch it
 - Could not connect to website
```

### Output (Example 2):
```

```

