# Crypto
This repo will contain my learning journey as i learn and solve crypto day by day...
Feel free to comment, criticize and advise on my code....Thankyouuuu...😄😄😊😊
##### tags `Signup` `Introduction` `General`
### Writeups

<h1>Signup</h1>
<p>We are presented with a ROT cipher. Replace value of a in:<a href="https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/0.%20Signup/">signup;</a></p>
<p>with your cipher. The script makes 25 iterations. Pick the one which makes sense.</p>

<h1>Introduction<h1>
<h1>Network Attacks</h1>
<img src="./screenshots/network_attacks.png" alt="Network Attacks">
<p>- Send a json request {"buy":"flag"} over telnet connection to receive flag.</p>
<p>- Script provided here: <a href="https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/1.%20Introduction/">Network Attacks</a></p>

<h1>General</h1>
<h2>Encoding</h2>
<h3>ASCII</h3>
<img src="./screenshots/ascii.png" alt="Network Attacks">
<p>- Read Array and convert to ascii to get flag. Script provided here:<a href="https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/2.General/ASCII.py">Ascii</a> </p>

<h3>Hex</h3>
<img src="./screenshots/hex.png" alt="Network Attacks">
<p>- There are several options:
<p>- Use bytes.fromhex() to convert hex to bytes, then bytes.decode() to convert to Ascii to get the flag</p>
<p>- Use binascii library unhexlify to convert hex to bytes to get flag</p>
<p>Script provided here: <a href="https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/2.General/hex.py">Hex</a></p>

<h3>Base64</h3>
<img src="./screenshots/base64.png" alt="Network Attacks">
<p>- Decode hex to bytes, then encode to base64 and decode to ascii</p>
<p> - Script provided here: <a href"https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/2.General/encodebase.py">Base64</a></p>


<h3>Bytes and Big Intergers</h3>
<img src="./screenshots/bigbytesint.png" alt="Network Attacks">
<p>- Import Crypto.Util.number </p>
<p>- Use to_bytes() to convert to bytes</p>
<p>- Decode bytes to ascii to get flag</p>
<p> - Script provided here: <a href="https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/2.General/bytesbigint.py">Bytes and Big Intergers</a></p>

<h3>Encoding Challenge</h3>

<h2>XOR</h2>
<p>Before starting XOR, here are a few things you should know:</p>
<p>-By default, when you <b>XOR</b> in python, values are converted into binary,</p>
<p> then the bitwise operations are done</>
<h3>XOR Starter</h3>
<img src="./screenshots/xorstarter.png" alt="xorstarter">
<h4>Python</h4>
<p>- Loop through the string and convert each character to unicode(ascii)</p>
<p>- XOR each character with the interger provided</p>
<p>- Convert result back to character from unicode represntation you get after xor</p>
<p>- Script is provided here: <a href="https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/2.General/xorstarter.py">XOR starter</a></p>
<h4>Golang</h4>
<p>-Golang works with strings in utf-8 encoding so there will be no need for conversion</p>
<p>-Simply loop  through each character xoring it with the interger provided, convert the bytes back to string to get the flag</p>
<p>- Golang Script provided here: <a href="https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/2.General/xorstarter.go">XOR starter</a></p>

<h3>XOR Properties</h3>
<img src="./screenshots/xor_properties.png" alt="XOR Properties">
<p>-
