# ReconCrawler
Automating OSINT and Web Enumeration.

## Description:
Recon Crawler is a tool that automates the process of OSINT and Web Enumeration and provides proper report generation. It is currently under development and has 10 features at the moment, which several more coming as the project continues.

## Requirements:
 ```bash
 1. Shodan
 2. Python-Whois
 3. bs4
 4. requests
 5. re
 ```

## Installation:
 Clone the Repository in local environment.
 ```bash
 $> git clone https://github.com/samsepi0x0/ReconCrawler.git
 ```
 
 Install the requirements:
 ```bash
 $> cd ReconCrawler
 $> pip install -r requirements.txt
 ```
 
## Usage:
 To execute the code, run the following command:
 ```bash
 $> python main.py
 ```
 
## Modules Description:
 ### SHODAN SCANS:
   <b>API_Info</b>: Returns the information about the Shodan API like monitored IP, plan, scan credits etc.
   
   <b>Host_Scanner</b>: Returns information about the host to be scanned (a domain), returns information like name servers, IP, open ports, etc.
   
   <b>Search_Query</b>: Most powerful module in the tool. Returns results of shodan searches, with properly formatted output.
 
 ### WEB_ENUMERATION:
  <b>Web_Crawler</b>: Crawls the website and searches for hyperlinks inside the webpages leading to discovery of internal site structure.
  
  <b>Dirbuster</b>: Directory Buster that bruteforces website directories in order to get the structure of the website.
  
  <b>Subdomain Lookup</b>: Searches for third level subdomains of a website by bruteforcing.

 ### DNS ENUMERATION:
  <b>Check_Domain_Registration</b>: Checks if a domain is registered or not.
  
  <b>WHOIS_Information_Retrieval</b>: Retrieves the WHOIS query for a domain to find information like nameservers, parent organization and many more.
    
 ### OSINT:
  <b>User Recon</b>: Searches for a given username across famous social media platforms.
  
  <b>Port Scanner</b>: Lists open ports found in an organization's domain.
 
## Output:
 Here is the output of a sample module:
 
 ![USERNAME_RECONNAISSANCE](https://raw.githubusercontent.com/samsepi0x0/ReconCrawler/main/Screenshot%20from%202022-09-27%2012-14-05.png)

## Contributions:
Feel free to fork and create a pull request to contribute to this repository. You know the rules and so do I.
