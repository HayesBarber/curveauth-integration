from curveauth.challenge import generate_challenge

def generate():
    challenge = generate_challenge()
    print(challenge)

if __name__ == "__main__":
    generate()
