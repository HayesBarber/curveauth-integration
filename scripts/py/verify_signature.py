import argparse
import sys
from curveauth.signatures import verify_signature

parser = argparse.ArgumentParser(description="Verify a signature using curveauth.")
parser.add_argument("public_key_b64", help="Base64-encoded public key")
parser.add_argument("signature_b64", help="Base64-encoded signature")
parser.add_argument("message", help="Original message to verify")
args = parser.parse_args()

success = verify_signature(args.message, args.signature_b64, args.public_key_b64, True)

sys.exit(0 if success else 1)
