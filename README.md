# RSA-CBC-Encrypted-FLASK

A Flask-based API for secure communication using RSA and AES-CBC encryption. This project demonstrates a hybrid encryption system, combining the speed of symmetric encryption (AES) with the security of asymmetric encryption (RSA) for secure message exchange.

## Features
- RSA key pair generation and management
- AES encryption in CBC mode for data confidentiality
- Secure key exchange using RSA
- RESTful API for encryption and decryption
- Simple Flask server for encrypted communication

## Prerequisites
- Python 3.10+
- Flask (`pip install flask`)
- PyCryptodome (`pip install pycryptodome`)

## Installation
```bash
# Clone the repository
git clone https://github.com/ghalibbajwa/RSA-CBC-Encryted-FLASK.git
cd RSA-CBC-Encryted-FLASK

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'

# Install the required dependencies
pip install -r requirements.txt
