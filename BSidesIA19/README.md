# Crack Me Up
### 50

    Description:
    Crack the hash to get the flag.
    2a9d119df47ff993b662a8ef36f9ea20:p4ssw0rd
    Put the cracked hash in secdsm{} to get the flag.

This one was pretty easy, as it was only 50 points. 
https://hashes.org/search.php returns `2a9d119df47ff993b662a8ef36f9ea20:p4ssw0rd`.

Flag: `secdsm{p4ssw0rd}`

# 114
### 50

    Description:
    Find the flag in the pcap.
    https://drive.google.com/open?id=1P7tcXmKc0DqpBDRt1LyiWhRPfpld0MlB

This was an odd series. The same pcap was used across different challenges and the challenge name helped distinguish which challenge you solved for which flag.
We got the flags from the pcacps and then submitted them to each of the challenges to see which flag went where. For this one I chose a tcp stream to follow in Wireshark and then in the bottom right hand corner, I went through all of the streams until I got to a FTP login where the password was the flag.

```
220 (vsFTPd 3.0.3)
USER ctf3
331 Please specify the password.
PASS SecDSM{KPp6GHevN9}
230 Login successful.
SYST
215 UNIX Type: L8
FEAT
211-Features:
 EPRT
 EPSV
 MDTM
 PASV
 REST STREAM
 SIZE
 TVFS
211 End
PWD
257 "/home/ctf3" is the current directory
TYPE I
200 Switching to Binary mode.
PASV
227 Entering Passive Mode (45,79,131,116,47,68)
CWD /home/ctf3/
250 Directory successfully changed.
LIST
150 Here comes the directory listing.
226 Directory send OK.
```

Flag: `SecDSM{KPp6GHevN9}`

# Samuel
### 100

    Description:
    Find the flag in the pcap.
    https://drive.google.com/open?id=1WTLG1R_RDxwXoVhgkbi8x16BBWg4dde_

This one is also from the series of pcacps. I followed a TCP stream again and then tcp stream 0 is a suspiciously similar to morse code.

Using https://morsecode.scphillips.com/translator.html it is in fact morse code.

```
f
... 
. 
-.-. 
-.. 
... 
-- 
/ 
-.-. 
-.- 
...-- 
--- 
-... 
--.- 
--.. 
.--. 
--. 
-.-- 
/

```

Flag: `SECDSM{CK3OBQZPGY}`

# Why Are Ogres Like Onions?
### 150 

    Description:
    `R00zQ0FNWlFFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQ...`

The full copy-paste is below. I threw this into cyberchef and ran the magic command with a crib of `sec`. This gave Base64 > Base32 > From Hex > From Octal > From Binary to get the flag

Cyberchef: `https://gchq.github.io/CyberChef/#recipe=Magic(7,false,false,'se')&input=UjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGtKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsVkZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRSVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAweVEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVTVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGtKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsVkZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRSVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAweVEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVTVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGtKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsVkZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRSVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAweVEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVTVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGtKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsVkZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRSVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAweVEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVTVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGtKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsVkZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpRMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRSVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVUVWxDVkVkQlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAweVEwRk5XbEZGUVZwRVFVbENWRWRaVVVSSFRVSkJSMGxaUTBGTldsZEZRVnBVUTBsQ1UwZEJVVVJIVGxKQlIwMVpVMEZOVWxGRlFWcFVUVWxDVkVkRlVVUkZUVUpCUjAwelEwRk5XbEpGUVZwRVFVbENWRWRaVVVSSFRVcEJSMGxaUTBGTldsZEZRVnBVUVVsQ1UwZEJVVVJIVGxKQlIwMVpVVDA5UFQwPQo`

```
R00zQ0FNWlFFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZU0FNUlFFQVpUTUlCVEdBUURFTUJBR00zQ0FNWlFFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTkJBR01ZQ0FNUlFFQVpUTUlCVEdBUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQVpUQUlCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlFFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWlVFQVpUQUlCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQUlCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdRUURHTUJBR0lZQ0FNWldFQVpUQUlCU0dBUURHTlJBR01ZU0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlFFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdBUURFTUJBR00yQ0FNWlFFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZU0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlFFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZU0FNUlFFQVpUSUlCVEdBUURFTUJBR00zQ0FNWlFFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTkJBR01ZQ0FNUlFFQVpUTUlCVEdBUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZU0FNUlFFQVpUTUlCVEdBUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWlVFQVpUQUlCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQUlCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdRUURHTUJBR0lZQ0FNWldFQVpUQUlCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQUlCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdBUURFTUJBR00yQ0FNWlFFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZU0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlFFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZQ0FNUlFFQVpUSUlCVEdBUURFTUJBR00zQ0FNWlFFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZU0FNUlFFQVpUTUlCVEdBUURFTUJBR00zQ0FNWlFFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTkJBR01ZQ0FNUlFFQVpUTUlCVEdBUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdBUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWlVFQVpUQUlCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlFFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZU0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdRUURHTUJBR0lZQ0FNWldFQVpUQUlCU0dBUURHTlJBR01ZU0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQVpUQUlCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdFUURFTUJBR00yQ0FNWlFFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQUlCU0dBUURHTlJBR01ZU0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlFFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQUlCU0dBUURHTlJBR01ZQ0FNUlFFQVpUSUlCVEdBUURFTUJBR00zQ0FNWlFFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZU0FNUlFFQVpUTUlCVEdBUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTkJBR01ZQ0FNUlFFQVpUTUlCVEdBUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdBUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWlVFQVpUQUlCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlFFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZU0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdRUURHTUJBR0lZQ0FNWldFQVpUQUlCU0dBUURHTlJBR01ZU0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlFFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQUlCU0dBUURHTlJBR01ZU0FNUlFFQVpUTUlCVEdBUURFTUJBR00yQ0FNWlFFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdBUURFTUJBR00zQ0FNWlFFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQUlCU0dBUURHTlJBR01ZQ0FNUlFFQVpUSUlCVEdBUURFTUJBR00zQ0FNWlFFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdBUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQUlCU0dBUURHTkJBR01ZQ0FNUlFFQVpUTUlCVEdBUURFTUJBR00zQ0FNWlFFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdBUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWlVFQVpUQUlCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQVpUQUlCU0dBUURHTlJBR01ZQ0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdRUURHTUJBR0lZQ0FNWldFQVpUQUlCU0dBUURHTlJBR01ZU0FNUlFFQVpUTUlCVEdBUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZU0FNUlFFQVpUTUlCVEdFUURFTUJBR00yQ0FNWlFFQVpEQUlCVEdZUURHTUJBR0lZQ0FNWldFQVpUQ0lCU0dBUURHTlJBR01ZU0FNUlFFQVpUTUlCVEdFUURFTUJBR00zQ0FNWlJFQVpEQUlCVEdZUURHTUpBR0lZQ0FNWldFQVpUQUlCU0dBUURHTlJBR01ZUT09PT0
```

Flag: `secdsm{c0v3r_y0uR_b@$3s_}`

# Rockit
### 200

    Description:
    Unzip the file to get the flag. http://bit.ly/2PjgyT3

Downloading the given file gives an encrypted 7z file. Running `7z2john` gives this hash

```
flag.7z:$7z$0$19$0$$8$693e1bf4590948220000000000000000$2892548062$112$106$2f34d18fc4f774392ae128b5c47151fdf827343ba7ee6e7dba718778a012839f5cb48f9e6190adc1f7d0bdddcaeab2253398b15ed9863b75eb2bf9cc5df8202bf0e975acbea94be9a124a069c09459e667f28771037a13ad97de917d891dce4dd32906a5012993c3b225414048402392
```

Which can be cracked very quickly with rockyou as the challenge hints at it with `rock` in the name. 
```
[blurbdust@X1C]: ~/Documents/B.Sides.19/rockit>$ john hash.txt --wordlist=/home/blurbdust/Documents/Wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (7z, 7-Zip [SHA256 256/256 AVX2 8x AES])
Cost 1 (iteration count) is 524288 for all loaded hashes
Cost 2 (padding size) is 6 for all loaded hashes
Cost 3 (compression type) is 0 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
bobesponja       (flag.7z)
1g 0:00:01:11 DONE (2019-04-21 21:59) 0.01397g/s 41.57p/s 41.57c/s 41.57C/s kikay..14789632
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

Extracting the file with the password of `bobesponja` now gives flag.txt and cat'ing it give the flag.
Flag: `secdsm{RockYou_password_encryption_did_not_rock}`

# Lego
### 200

    Description:
    Find the flag in the pcap.
    https://drive.google.com/open?id=1VDkJjGTR13RVtiXXJ2NnN-hlGRoXKq82

Back to the pcaps, we open this one up and do the same tcp stream, following. This leads to noticing there is SMB traffic and a reference to SMB carving in Wireshark. I Exported the Objects for SMB traffic and there was `flog.txt` and a zip file! This was encrypted so using `zip2john` gives the hash of 
```
tmp.zip:$zip2$*0*3*0*7bbdccf5cd8e8ec98f1d8a5cd24b1a53*33cf*13*d97d95396f8894aa92917a0bad8e67d76276f1*924f9d21299d000492fb*$/zip2$:::::tmp.zip-wavy/flag.txt
```
Again using the rockyou wordlist I got the password of `dontcry`. I unzipped the flag file and cat'ed it. 

Flag: `SecDSM{ZftGfXOjxi}`

# Scripting 3
### 400

    Description:
    Do socat servers dream of python sheep?
    nc 206.189.224.72 5123

Ok this one was fun. I also only did this one of the series which was a continuation on Scripting 1 and Scripting 2. Using `nc` to connect to the server you get prompted to answer a math question. 

```
[blurbdust@X1C]: ~/Documents/B.Sides.19/lego>$ nc 206.189.224.72 5123
75 / 88 = ?: 
```

After solving it you get another, and another, and another. They keep going for 24 times. Scripting 1 ended here. Scripting 2 went for an additional 20ish but also changed the operator `+-/*%` to words. Spliting on spaces and checking for `mod`, `plus`, `times`, and `divided` was our solution. Scripting 3 took the numbers and also turned those into words so `42 + 42 = ?` went to `fourty two plus fourty two = ?`. We tracked down a python library called `word2number` which could handle this conversion easily for us. After adding this in, the script still broke! The evil makers of this challenge decided they will now randomly throw the previous Scripting 1 and 2 formats back in so we have to handle these after the initial 24 and 20ish. This worked and we finalyl got the flag. The full script is below. 
Script TL;DR: I split on spaces, try to use the library to check if it's the new stage or old stage. If old stage, check if the `len(split_data[1]) < 2` to check if it's single character (`+`,`-`,`*`,`/`,`%`), if so then eval. Else replace the word with the symbol and eval. 

```python
import socket
from word2number import w2n

TCP_IP = '206.189.224.72'
TCP_PORT = 5123
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#s.send(MESSAGE)

data = s.recv(BUFFER_SIZE)
#if not data: break
print data
#s.close()
data2 = data[0: 10: 1]
data2 = data2[:-3]

print data2
result = str(eval(data2))
s.send(result + "\n")
print result

wordnum = False

count = 0

i = 0

while 1:
	data = s.recv(BUFFER_SIZE)
	try:
		newdata = data.split(' ')
		num1 = newdata[0] + " " + newdata[1]
		int_num1 = w2n.word_to_num(num1)
		wordnum = True
	except ValueError:
		wordnum = False
		# do normal things
		pass

	newdata = data.split(" ")

	if (len(newdata[1]) < 2):
		
		if not data: break
		print(data)
		#s.close()
		data2 = data[0: 10: 1]
		data2 = data2[:-3]
		
		print(data2)
		result = str(eval(data2))
		s.send(result + "\n")
		print result
		print i
		i += 1
	elif ((len(newdata[1]) > 2) and (wordnum == False)):
		if not data: break
		print(data)
		newdata = data.split(' ')
		if newdata[1] == 'plus':
			result = int(newdata[0]) + int(newdata[2])
			print result
		elif newdata[1] == 'minus':
			result = int(newdata[0]) - int(newdata[2])
			print result
		elif newdata[1] == 'mod':
			result = int(newdata[0]) % int(newdata[2])
			print result
		elif newdata[1] == 'times':
			result = int(newdata[0]) * int(newdata[2])
			print result
		elif newdata[1] == 'divided':
			result = int(newdata[0]) / int(newdata[3])
			print result
		s.send(str(result) + '\n')
		i += 1
		print i

	elif (wordnum == True):
		if not data: break
		print(data)
		newdata = data.split(' ')
		num1 = newdata[0] + " " + newdata[1]
		op = newdata[2]
		num2 = newdata[3] + " " + newdata[4]

		print("num1: " + str(num1))
		print("num2: " + str(num2))

		int_num1 = w2n.word_to_num(num1)
		int_num2 = w2n.word_to_num(num2)

		print("int_num1: " + str(int_num1))
		print("int_num2: " + str(int_num2))

		if op == 'plus':
			result = int(int_num1) + int(int_num2)
			print result
		elif op == 'minus':
			result = int(int_num1) - int(int_num2)
			print result
		elif op == 'mod':
			result = int(int_num1) % int(int_num2)
			print result
		elif op == 'times':
			result = int(int_num1) * int(int_num2)
			print result
		elif op == 'divided':
			result = int(int_num1) / int(int_num2)
			print result
		s.send(str(result) + '\n')
		print(result)
```

I had to run this a few times however you eventually get the flag.

Flag: `You win! SecDSM{way_easier_to_go_the_other_way}`

# Rivest–Shamir–Adleman
### 400

    Description:
    Download file: http://bit.ly/2vk0ebb
    Decrypt the file to get the flag

This one is RSA as the title says. We get a public key and an encrypted file. 
Using RsaCtfTool from https://github.com/Ganapati/RsaCtfTool

We can use the factordb attack to check if the primes have been added to http://factordb.com/

```
blurbdust@X1C]: ~/Documents/B.Sides.19/rsa>$ python2.7 ~/tools/RsaCtfTool/RsaCtfTool.py --publickey public.key --uncipherfile flag.enc --attack factordb
[+] Clear text : b���h	1zsecdsm{beonyourps&qs}
```
Flag: `secdsm{beonyourps&qs}`

# Reconstruction
### 450

    Description:
    Files available at http://bit.ly/2UurWw3 modulus:
    00:da:79:57:de:37:d2:fb:1a:b7:c8:cf:cd:67:d6:
    b3:f5:f5:f4:b5:e3:94:48:66:87:76:6b:3b:db:c0:
    33:74:54:b0:f3:cd:9a:90:8b:60:23:13:c4:e3:bd:
    08:fe:47:c8:db:1f:ad:d1:2a:12:da:54:f6:8b:bc:
    e7:66:15:30:d7:94:5f:cf:b9:99:18:a0:3a:6f:27:
    79:9b:fe:a5:2b:8a:6a:41:b6:2c:0a:a7:85:0b:7b:
    d7:4a:57:c1:7b:8a:f5:78:a2:ec:38:4b:58:26:e9:
    5c:06:2b:e3:0a:03:d7:d8:7c:57:58:ff:2e:b9:a9:
    21:67:85:62:38:55:dd:53:73

    publicExponent: 65537 (0x10001)

    privateExponent:
    37:91:57:7d:08:db:db:cc:5e:e4:6f:9e:42:04:04:
    ff:d1:50:2d:97:35:d6:f8:65:0a:04:9a:53:f9:5d:
    dc:ff:d1:86:21:4c:67:e9:5b:49:70:b4:ca:6c:01:
    46:93:c1:8d:a2:50:16:7c:4a:11:48:3c:f1:2b:d9:
    fb:47:f6:84:d6:09:dd:46:c6:79:d9:46:f0:7e:9c:
    1e:24:4a:3f:db:fb:94:1a:ea:5b:03:6c:4b:74:d2:
    c4:2a:1e:02:98:a9:e3:25:1d:1a:72:02:1b:fe:f5:
    2b:6a:d0:5c:4e:23:82:42:5b:8e:57:18:d4:d4:09:
    a0:e8:43:45:20:0f:d8:d9

    prime1:
    00:fb:ad:b1:49:bf:db:a3:30:6d:8c:e9:17:85:34:
    52:aa:f7:ac:7a:b0:f2:8b:8d:bb:36:04:a9:c6:04:
    1f:a6:6c:f0:34:2d:61:f0:c4:54:cb:5e:56:f2:19:
    79:5d:ec:3b:74:ec:94:18:1f:24:e5:25:1c:1c:62:
    ec:9d:eb:27:c7

    prime2:
	00:de:39:b1:72:a1:d5:38:1f:bd:ba:9f:4f:97:4e:
	4a:2a:04:c1:f2:62:c0:c9:b4:66:b9:5f:2e:b5:3e:
	8d:b7:f5:19:bb:b3:28:21:f5:ba:1c:9f:1e:d4:db:
	e6:85:84:a5:f4:35:0d:51:f6:d7:3c:81:c5:3e:e2:
	20:11:01:ae:f5

So we are given primes, a modulus, and an exponent. It sounds like RSA again!
We are given two files, `enc_key.enc` and `flag.enc`. I'm guessing we need to decrypt the key first and then do something else to decrypt the flag. 

RsaCtfTool can recreate a RSA key from the numbers that make up the key. That sounds like exactly what we need to do. can either do hex or decimal for the recreation. I like to use decimal so I used python to convert them. Save the numbers as strings, remove the `:`, the new lines, and then `print(int(num, 16))`. Then take those numbers and use it with RsaCtfTool's `--createpub`.

```
[blurbdust@X1C]: ~/Documents/B.Sides.19/reconstruction>$ python2.7 ~/tools/RsaCtfTool/RsaCtfTool.py --createpub -n 153417658035385267201603663701555060309113239092246784524632389918822299006317847021185056350551962482372979892829792285582460538571341886594717300718316849082378528321848961256305260150340512082309069043621723469564598541882175214196623792955206212920692949684291862065750365144190626093259936448445115356019 -e 65537
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDaeVfeN9L7GrfIz81n1rP19fS1
45RIZod2azvbwDN0VLDzzZqQi2AjE8TjvQj+R8jbH63RKhLaVPaLvOdmFTDXlF/P
uZkYoDpvJ3mb/qUrimpBtiwKp4ULe9dKV8F7ivV4ouw4S1gm6VwGK+MKA9fYfFdY
/y65qSFnhWI4Vd1TcwIDAQAB
-----END PUBLIC KEY-----
```
Then we can take the primes and add them to the past ctf times textfile and run RsaCtfTool again to get the private key. Why not just make the private key in the first place? RsaCtfTool only supports unciphering from a public key. 

```
echo "# bsides secdsm" >> ~/tools/RsaCtfTool/pastctfprimes.txt
echo "11638886703810816263076022704355286643278693037539797353010834609502878323603237967342636495026800360033420902652344544587374562439769944929211472215650037" >> ~/tools/RsaCtfTool/pastctfprimes.txt
echo "13181471900156318190914974965447548572159496954345577743507716421099673351951718084554874363290930680176850459642703614378635197409277655797292113391724487" >> ~/tools/RsaCtfTool/pastctfprimes.txt
```
Then we run `--uncipher` and it will automatically build the private key for us and then decrypt the flag. 

```
[blurbdust@X1C]: ~/Documents/B.Sides.19/reconstruction>$ python2.7 ~/tools/RsaCtfTool/RsaCtfTool.py --uncipherfile enc_key.enc --publickey pub.key 
[+] Clear text : 9Y؟V8P��rD�H{vs3�=�t�Tsf*3"�T�`��ԁ|��>S��a�[u�%$L֪��G>��0��~�~O�X���Z6�H�Wx@�/�^Kcda09bddd5377b12c7a35b7169785124
```

Yes there is a lot of garbage in the output but the important part is `cda09bddd5377b12c7a35b7169785124`. I got stuck here for awhile. I used the free hint and saw `A mode has no IV` so I thought AES. I tried to decrypt the flag and failed so I asked the maker for help. I was correct with AES however I was pointed to use the python AES implementation as cyberchef's AES module uses an IV of all nullbytes which was wrong since there was no IV specified when this challenge was created. 

The solution script is below. Use `python2.7`.

```python
prime2 = "00de39b172a1d5381fbdba9f4f974e4a2a04c1f262c0c9b466b95f2eb53e8db7f519bbb32821f5ba1c9f1ed4dbe68584a5f4350d51f6d73c81c53ee2201101aef5"

prime1 = "00fbadb149bfdba3306d8ce917853452aaf7ac7ab0f28b8dbb3604a9c6041fa66cf0342d61f0c454cb5e56f219795dec3b74ec94181f24e5251c1c62ec9deb27c7"

privExp = "3791577d08dbdbcc5ee46f9e420404ffd1502d9735d6f8650a049a53f95ddcffd186214c67e95b4970b4ca6c014693c18da250167c4a11483cf12bd9fb47f684d609dd46c679d946f07e9c1e244a3fdbfb941aea5b036c4b74d2c42a1e0298a9e3251d1a72021bfef52b6ad05c4e2382425b8e5718d4d409a0e84345200fd8d9"

mod = "00da7957de37d2fb1ab7c8cfcd67d6b3f5f5f4b5e394486687766b3bdbc0337454b0f3cd9a908b602313c4e3bd08fe47c8db1fadd12a12da54f68bbce7661530d7945fcfb99918a03a6f27799bfea52b8a6a41b62c0aa7850b7bd74a57c17b8af578a2ec384b5826e95c062be30a03d7d87c5758ff2eb9a9216785623855dd5373"

print(int(prime2, 16))
print("")
print(int(prime1, 16))
print("")
print(int(privExp, 16))
print("")
print(int(mod, 16))
print("")

print("see below")


msg = "04915b2c959c73744cbf5f054097fe84f14ba56c16bb65abfd2b2b3727d3f5ce".decode("hex")
from Crypto.Cipher import AES

key = 'cda09bddd5377b12c7a35b7169785124'.decode("hex")

decipher = AES.new(key, AES.MODE_ECB)


print(decipher.decrypt(msg))

```

Flag: `secdsm{Y0uRpr1v@t3ExpI$Exp0sed!}`

Overall this was the most fair CTF I have ever played in. There were no Gotchyas. If you knew the path you should take to get the flag you would get the flag and not have to jump through an additional hoop that other CTFs have to keep everyone on their toes. 