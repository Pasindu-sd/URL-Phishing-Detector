import re

def check_url(url):
   
   print(f"Analyzing: {url}")
   problem = []
   
   if len(url) > 75:
      problem.append("URL is too long - might be hiding something")
      
   if url.count('-') > 3:
      problem.append("Too many hyphens - common in fake sites")
      
   if re.search(r"\d+\.\d+\.\d+\.\d+", url):
      problem.append("Uses IP address instead of domain name")
      
   fake_brands = ['paypal', 'facebook', 'google', 'microsoft', 'bank']
   for brand in fake_brands:
      if brand in url.lower() and '-' in url:
         problem.append("Might be faking {brand} website")
         
   if problem:
      print("\n SUSPICIOUS FOUND:")
      for problem in problem:
         print(f" {problem}")     
   else:
      print("\nURL looks safe (basic check)")
      
   return problem


# Main function
if __name__ == "__main__":
   website = input("Enter URL to check: ")
   check_url(website)