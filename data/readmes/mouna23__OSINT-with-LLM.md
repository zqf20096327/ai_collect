# POC : OSINT with LLM

This repository demonstrates domain, IP, and email reconnaissance with **LLM-powered** security reporting..

---

##  Overview

The project is divided into **two main components**:

1. **Recon Modules** 
2. **LLM Analysis and reporting** 

---

##  Recon Modules

### **Purpose**
Gathering information about an ip, domain or email

### **Approach**
- **Domain OSINT:** 
    * WHOIS Lookup

    * Shodan Info Gathering

    * SSL Certificate Validation

    * VirusTotal "malicious/clean" status
- **IP Recon:** 
    * AbuseIPDB score & classification

- **Email Recon:** 
    * Breach/exposure lookup

### **LLM Analysis and reporting**

* Converts technical OSINT into human-readable summaries

* Extracts key findings & risk insights

* Generates reports

## **Required API keys for OSINT modules**

* VT_API_KEY=your_virustotal_api_key
* ABUSEIPDB_KEY=your_abuseipdb_api_key
* SHODAN_KEY=your_shodan_api_key

## **Usage**
### **Install dependencies**
```bash
pip3 install -r requirements.txt
```
### **Demo**
```bash
python3 main.py
```
When finished:

* OSINT recon runs

* LLM analyzes results

* A report is saved in /reports/

#### **Demo with domain**

![Project Logo](images/llm_domain_1.png)

![Project Logo](images/llm_domain_2.png)

#### **Demo with ip**

![Project Logo](images/llm_ip_1.png)

![Project Logo](images/llm_ip_2.png)

#### **Demo with email**

![Project Logo](images/ll_email_1.png)

![Project Logo](images/llm_email_2.png)

##  Notes 
* The scripts are designed to be run locally, in a Python 3.13+ environment with the listed dependencies.
* Install Ollama on your machine and add the MISTRAL model.
* This poc is only for education purpose.