from argon2 import PasswordHasher

def generate_hash(text, algorithm='argon2id'):
    """
    Generate a hash of the input text using the specified 
    
    Args:
        text (str): The text to hash
        algorithm (str): The hash algorithm to use (default: 'argon2id')
    
    Returns:
        str: Hash string
    """
    if algorithm == 'argon2id':
        hasher = PasswordHasher()
        return hasher.hash(text)
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")


if __name__ == "__main__":
    # Interactive hash generator
    text = input("Enter text to hash:" )
    algorithm = input("Enter algorithm (default: argon2id): ") or 'argon2id'
    
    try:
        print(f"Original text: {text}")
        hash_result = generate_hash(text, algorithm)
        print(f"{algorithm}: {hash_result}")
    except ValueError as e:
        print(f"Error: {e}")