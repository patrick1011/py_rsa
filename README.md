# Toy RSA Implementation

**THIS IS A TOY PROJECT.  THIS IMPLEMENTATION OF THE RSA PROTOCOL IS NOT SECURE AND IS MISSING VITUAL SECURITY FEATURES.  FOR EDUCATIONAL PURPOSES ONLY.**

This project includes:
- An RSA key generator.
- A Flask server which listens for incoming encrypted messages.
- A client which sends encrypted messages to the above server.

The project is inspired by the exposition of the RSA cryptosystem in  *'Understanding Cryptography', A Textbook for Students and Practitioners by Christof Paar, Jan Pelzl, Bart Preneel (ISBN: 8601406549616)*.

## Generating RSA keys

Run the following to compute and print a set of RSA keys to the terminal:
```
python -m key_generator.main
```

## Lanching the server to listen for messages

Paste the `PRIVATE_EXPONENT` and `MODULUS` generated above into `server/settings.py` then run

```
python -m server.api.main
```

Incoming messages are listened to at `/`.  To be processed `POST` the following to `/`
```
{
  "ciphertext": CIPHERTEXT GOES HERE
}
```

Incoming messages will be logged to `server/message_log.txt`

## Using the client to send messages to the server

Paste the `PUBLIC_EXPONENT` and `MODULUS` generated above into `client/settings.py`.  Also specify a `URI` to send the encrypted message to.

Insert some plaintext into `client/plaintext_payload.txt` and run

```
python -m server.api.main
```
