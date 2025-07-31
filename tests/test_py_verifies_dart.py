import subprocess
import json

def test_dart_keypair_generation():
    keygen_proc = subprocess.run(
        ["dart", "scripts/dart/generate_key_pair.dart"],
        capture_output=True, text=True, check=True
    )
    keypair_json, public_key_b64 = json.loads(keygen_proc.stdout.strip())
    assert len(public_key_b64) > 0

    challenge_proc = subprocess.run(
        ["python3", "scripts/py/generate_challenge.py"],
        capture_output=True, text=True, check=True
    )
    challenge = challenge_proc.stdout.strip()
    assert len(challenge) > 0

    sign_proc = subprocess.run(
        ["dart", "scripts/dart/sign_challenge.dart", keypair_json, challenge],
        capture_output=True, text=True, check=True
    )
    signature = sign_proc.stdout.strip()
    assert len(signature) > 0

    subprocess.run(
        ["python3", "scripts/py/verify_signature.py", public_key_b64, signature, challenge],
        capture_output=True, text=True, check=True
    )


def test_dart_invalid_signature():
    keygen_proc = subprocess.run(
        ["dart", "scripts/dart/generate_key_pair.dart"],
        capture_output=True, text=True, check=True
    )
    keypair_json, public_key_b64 = json.loads(keygen_proc.stdout.strip())

    challenge_proc = subprocess.run(
        ["python3", "scripts/py/generate_challenge.py"],
        capture_output=True, text=True, check=True
    )
    challenge = challenge_proc.stdout.strip()

    sign_proc = subprocess.run(
        ["dart", "scripts/dart/sign_challenge.dart", keypair_json, challenge],
        capture_output=True, text=True, check=True
    )
    signature = sign_proc.stdout.strip()

    tampered_signature = signature[:-1] + ("A" if signature[-1] != "A" else "B")

    verify_proc = subprocess.run(
        ["python3", "scripts/py/verify_signature.py", public_key_b64, tampered_signature, challenge],
        capture_output=True, text=True
    )

    assert verify_proc.returncode != 0

if __name__ == "__main__":
    test_dart_keypair_generation()
    test_dart_invalid_signature()
    print("All py verifies dart tests passed.")