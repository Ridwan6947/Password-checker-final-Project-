This Python script utilizes the "Have I Been Pwned" API and SHA-256 hashing to enhance password security. When a user enters a password, the script first checks its strength based on length and character types.
Subsequently, it computes the SHA-256 hasing to  hash of the password, which is then split into two parts: the first five characters (the prefix) and the remainder of the hash (the tail). 
The prefix is sent to the "Have I Been Pwned" API, which responds with a list of leaked password hashes sharing the same prefix. The script then searches this list for a match with the tail of the user's password hash.
If a match is found, it signals that the password has been compromised in previous breaches.
This approach allows users to assess the security of their passwords without transmitting the actual password, enhancing security and privacy.
for the development of this project i worked by Request Module - allows you to send HTTP requests using Python
and Hashlib module  - provides a helper function for efficient hashing of a file


Novalty

CipherGuard doesn't just evaluate length and character diversity; it also securely hashes passwords and checks them against a comprehensive database of known breaches, all while preserving user privacy Additionally,
CipherGuard fills a crucial gap by not only identifying weak passwords but also actively informing users if their password has been compromised, prompting them to take immediate action to safeguard their online accounts
