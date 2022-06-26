# ClickJacker
## Full Automation Clickjacking Vulnerability Scanner

### Installation:
Copy the command and paste it on terminal

```javascript
git clone https://github.com/bughuntar/ClickJacker.git
```
```javascript
cd ClickJacker
```
```javascript
sudo chmod +x *
```

**Dependencies:**
```javascript
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```
```javascript
sudo pip3 install colorama
```
```javascript
sudo apt-get update figlet
```

### Usage:
```javascript
./exploit.sh
```
OR
```javascript
python file.py domains.txt
```

### How to use this tool?
>Go to your terminal and Install the tool. Then run the bash file `exploit.sh` and type your main domain or run the `file.py`. It will show you possible vulnerable subdomains with Verification link. Click on that link to verify the bug is valid or not.


### Automated:
```javascript
./exploit.sh
```

### Manual:
```javascript
python file.py domains.txt
```
