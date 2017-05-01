#!/usr/bin/python
# For use in extracting KDF information from Ethereum wallet.json files(Geth)

__authors__ = ['Chick3nman']


import json, sys

with open('list.txt') as wallet_file:
    wallet_data = json.load(wallet_file)
    kdf = wallet_data['crypto']['kdf']
    if kdf == 'pbkdf2':
        prf = wallet_data['crypto']['kdfparams']['prf']
        if prf == 'hmac-sha256':
            ciphertext = wallet_data['crypto']['ciphertext']
            mac = wallet_data['crypto']['mac']
            iter = wallet_data['crypto']['kdfparams']['c']
            salt = wallet_data['crypto']['kdfparams']['salt']
            print '$ethereum$p*%s*%s*%s*%s' % (iter, salt, mac, ciphertext)
        else:
            print "Wallet format unknown or unsupported!"
            sys.exit()

    elif kdf == 'scrypt':
        ciphertext = wallet_data['crypto']['ciphertext']
        mac = wallet_data['crypto']['mac']
        n = wallet_data['crypto']['kdfparams']['n']
        p = wallet_data['crypto']['kdfparams']['p']
        r = wallet_data['crypto']['kdfparams']['r']
        salt = wallet_data['crypto']['kdfparams']['salt']
        print '$ethereum$s*%s*%s*%s*%s*%s*%s' % (n, r, p, salt, mac, ciphertext)
    else:
        print "Wallet format unknown or unsupported!"
        sys.exit()
