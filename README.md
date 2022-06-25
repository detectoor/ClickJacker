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


### exploit.sh --> It will enumerate subdomains then start Scanning (Auto)
### file.py --> It will scan your provided domains.txt
