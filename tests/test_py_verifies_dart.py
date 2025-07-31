import subprocess
import json

def test_dart_keypair_generation():
    result = subprocess.run(
        ["dart", "scripts/dart/generate_key_pair.dart"],
        capture_output=True, text=True, check=True
    )

    output = result.stdout.strip()
    keypair_json, public_key_b64 = json.loads(output)

    print(f"Key pair json: {keypair_json}")
    print(f"Public key b64: {public_key_b64}")

    assert isinstance(keypair_json, str)
    assert isinstance(public_key_b64, str)
    assert len(public_key_b64) > 0

    result = subprocess.run(
        ["python3", "scripts/py/generate_challenge.py"],
        capture_output=True, text=True, check=True
    )

    challenge = result.stdout.strip()

    print(f"Challenge: {challenge}")

    assert isinstance(challenge, str)
    assert len(challenge) > 0

    result = subprocess.run(
        ["dart", "scripts/dart/sign_challenge.dart", keypair_json, challenge],
        capture_output=True, text=True, check=True
    )

    signature = result.stdout.strip()
    print(f"Signature: {signature}")
    assert isinstance(signature, str)
    assert len(signature) > 0

    result = subprocess.run(
        ["python3", "scripts/py/verify_signature.py", public_key_b64, signature, challenge],
        capture_output=True, text=True
    )

    assert result.returncode == 0

if __name__ == "__main__":
    test_dart_keypair_generation()
    print("All py verifies dart tests passed.")