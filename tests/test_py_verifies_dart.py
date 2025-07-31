import subprocess
import json

def test_dart_keypair_generation():
    result = subprocess.run(
        ["dart", "scripts/dart/generate_key_pair.dart"],
        capture_output=True, text=True, check=True
    )

    output = result.stdout.strip()
    keypair_json, public_key_b64 = json.loads(output)

    print(output)
    print("-----")
    print(keypair_json)
    print("-----")
    print(public_key_b64)

    assert isinstance(keypair_json, str)
    assert isinstance(public_key_b64, str)
    assert len(public_key_b64) > 0

if __name__ == "__main__":
    test_dart_keypair_generation()
    print("All py verifies dart tests passed.")