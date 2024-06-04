
# 📡 Curl Command Cheat Sheet

Welcome to the Curl Command Cheat Sheet! This document provides a comprehensive list of commonly used `curl` commands, which can be used for various tasks such as fetching data, testing APIs, or automating web requests.

## 📄 Table of Contents

1. [Basic `curl` Commands](#basic-curl-commands)
2. [Authentication](#authentication)
3. [HTTP Methods](#http-methods)
4. [Headers and Data](#headers-and-data)
5. [SSL/TLS](#ssl-tls)
6. [Other Useful Commands](#other-useful-commands)

## Basic `curl` Commands

1. **Get a webpage content:**
   ```sh
   curl http://example.com
   ```

2. **Download a file:**
   ```sh
   curl -O http://example.com/file.zip
   ```

3. **Save output to a file:**
   ```sh
   curl http://example.com -o output.html
   ```

4. **Follow redirects:**
   ```sh
   curl -L http://example.com
   ```

5. **Limit download rate:**
   ```sh
   curl --limit-rate 100K http://example.com
   ```

6. **Include headers in the output:**
   ```sh
   curl -i http://example.com
   ```

## Authentication

1. **Basic authentication:**
   ```sh
   curl -u username:password http://example.com
   ```

2. **OAuth token:**
   ```sh
   curl -H "Authorization: Bearer your_token" http://example.com
   ```

## HTTP Methods

1. **POST request:**
   ```sh
   curl -X POST http://example.com
   ```

2. **POST request with data:**
   ```sh
   curl -X POST -d "param1=value1&param2=value2" http://example.com
   ```

3. **PUT request:**
   ```sh
   curl -X PUT -d "param1=value1" http://example.com
   ```

4. **DELETE request:**
   ```sh
   curl -X DELETE http://example.com
   ```

## Headers and Data

1. **Send custom headers:**
   ```sh
   curl -H "Content-Type: application/json" http://example.com
   ```

2. **Send multiple headers:**
   ```sh
   curl -H "Content-Type: application/json" -H "Authorization: Bearer your_token" http://example.com
   ```

3. **Send data with a request:**
   ```sh
   curl -d "param1=value1&param2=value2" http://example.com
   ```

4. **Send JSON data:**
   ```sh
   curl -H "Content-Type: application/json" -d '{"key1":"value1", "key2":"value2"}' http://example.com
   ```

## SSL/TLS

1. **Ignore SSL certificate errors:**
   ```sh
   curl -k https://self-signed.badssl.com/
   ```

2. **Specify SSL certificate:**
   ```sh
   curl --cert /path/to/cert.pem https://example.com
   ```

3. **Use a client certificate:**
   ```sh
   curl --cert client.pem --key key.pem https://example.com
   ```

## Other Useful Commands

1. **Download a file in chunks:**
   ```sh
   curl -C - -O http://example.com/largefile.zip
   ```

2. **Show request/response details:**
   ```sh
   curl -v http://example.com
   ```

3. **Show only response headers:**
   ```sh
   curl -I http://example.com
   ```

4. **Set a user agent:**
   ```sh
   curl -A "Mozilla/5.0" http://example.com
   ```

5. **Proxy support:**
   ```sh
   curl -x http://proxyserver:port http://example.com
   ```

6. **FTP upload:**
   ```sh
   curl -T file.txt ftp://ftpserver/upload/
   ```
