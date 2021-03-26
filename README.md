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
<p>-From the Properties of XOR, the associative property best applies here that is: </p>
<p> <t><t>Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C </p>
<p>-In our case: </p>
<p>(i)   Convert the hex to bytes</p>
<p>(ii)  Import xor from pwntools</p>
<p>(iii) XOR key2^key3 with key1</p>
<p>(iv)  XOR results above with flag^key1^key3^key2 to get flag</p>
<p>(v)   Decode the bytes to ascii</p>
<p>- Script provided here: <a href="https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/2.General/xor_properties.py">XOR Properties</a></p>

<h3>Favourite Byte</h3>
<img src="./screenshots/favourite_byte.png" alt="Favourite Byte">
<p>-In utf-8 an unsigned in ranges from 0-256, and each has 8bits(1byte) from which one of them has been used to XOR our flag</p>
<p>(i)  Convert the hex data to data bytes</p>
<p>(ii) Declare the starting bytes at 0x00</p>
<p>(iii)Loop through range 0-256 xoring each data bytes with bytes in step(i)</p>
<p>(iv) Since we know our flag format, print out only when the string has part of the flag else go back to step3</p>
<p>- Script provide here: <a href="https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/2.General/favourite_byte.py">Favourite Byte</a></p>

<h3>You either know, XOR you dont</h3>
<img src="./screenshots/eitherKnowXor.png" alt="Know XOR or Not">
<p></p>

<h3>Lemur XOR</h3>
<img src="./screenshots/LemurXor.png" alt="lemurXor">
<p>- The two images are XORed with the same key</p>
<p>- From XOR Properties, if we XOR the two images with each other, they are bound to give the key used in xoring them</p>
<p>- Script provided here: <a href="https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/2.General/lemurXor.sh">LemurXor</a></p>


<h2>Mathematics<h2>
<h3>Greatest Common Divisor</h3>
<img src="./screenshots/gcd.png" alt="GCD">
<p>- For this task, i used <a href="https://en.wikipedia.org/wiki/Euclidean_algorithm#Description">Euclid's algorithm</a> as advised in the challenge. Found it pretty simple than expected btw...</p>
<p>- For easier understanging, please go through the following youtube video: <a href="https://youtu.be/cOwyHTiW4KE">The Trev Tutor- Euclidian algorithm</a></p>
<p>- Basically, for any values (a,b): a = bq+r  and gcd(a,b) = gcd(b,r)<br>
e.g (5,2) = 2.2+1<br>
b = 2 r =1<br>
(2,1) = 2.1 + 0<br>
when r = 0, gcd will be equal to the value of b <br>
- For bigger numbers, repeat this recursively till r=0 .i.e while loop
- With this in mind, we can now script it <a href="https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/2.General/Mathematics/gcd.py>Euclidean algorithm</a></p>

<h3>Extended GCD</h3>
