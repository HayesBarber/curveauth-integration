import subprocess
import json

def test_dart_keypair_generation():
    keygen_proc = subprocess.run(
        ["dart", "scripts/dart/generate_key_pair.dart"],
        capture_output=True, text=True, check=True
    )
    keypair_json, public_key_b64 = json.loads(keygen_proc.stdout.strip())
    print(f"Key pair json: {keypair_json}")
    print(f"Public key b64: {public_key_b64}")
    assert len(public_key_b64) > 0

    challenge_proc = subprocess.run(
        ["python3", "scripts/py/generate_challenge.py"],
        capture_output=True, text=True, check=True
    )
    challenge = challenge_proc.stdout.strip()
    print(f"Challenge: {challenge}")
    assert len(challenge) > 0

    sign_proc = subprocess.run(
        ["dart", "scripts/dart/sign_challenge.dart", keypair_json, challenge],
        capture_output=True, text=True, check=True
    )
    signature = sign_proc.stdout.strip()
    print(f"Signature: {signature}")
    assert len(signature) > 0

    subprocess.run(
        ["python3", "scripts/py/verify_signature.py", public_key_b64, signature, challenge],
        capture_output=True, text=True, check=True
    )

if __name__ == "__main__":
    test_dart_keypair_generation()
    print("All py verifies dart tests passed.")