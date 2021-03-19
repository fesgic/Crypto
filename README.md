# Crypto
This repo will contain my learning journey as i learn and solve crypto day by day...
Feel free to comment, criticize and advise on my code....Thankyouuuu...😄😄😊😊
##### tags `Signup` `Introduction` `General`
### Writeups

<h1>Signup</h1>
<p>We are presented with a ROT cipher. Replace value of a in:</p>
- [Shell Script](https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/0.%20Signup/)
<p>with your cipher. The script makes 25 iterations. Pick the one which makes sense.</p>

<h1>Introduction<h1>
<h1>Network Attacks</h1>
<![Network Attacks](/screenshots/network_attacks.png)
<p>- Send a json request {"buy":"flag"} over telnet connection to receive flag.</p>
<p>- Script provided here:</p>
- [Network Attacks](https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/1.%20Introduction/)

<h1>General</h1>
<h2>Encoding</h2>
<h3>ASCII</h3>
<p>- Read Array and convert to ascii to get flag</p>
- [Ascii](https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/2.General/ASCII.py)

<h3>Hex</h3>
<p>- There are several options:
<p>- Use bytes.fromhex() to convert hex to bytes, then bytes.decode() to convert to Ascii to get the flag</p>
<p>- Use binascii library unhexlify to convert hex to bytes to get flag</p>
- [Hex](https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/2.General/hex.py)

<h3>Base64</h3>
<p>- Decode hex to bytes, then encode to base64 and decode to ascii</p>
- [Base64](https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/2.General/encodebase.py)

<h3>Bytes and Big Intergers</h3>
<p>- Import cryto.util.number </p>
<p>- Use to_bytes() to convert to bytes</p>
<p>- Decode bytes to ascii to get flag</p>
- ![Bytes and Big Intergers](https://github.com/fesgic/Crypto/blob/main/Cryptohack.org/2.General/bytesbigint.py)

<h3>Encoding Challenge</h3>

<h2>XOR</h2>
<h3>XOR Starter</h3>
