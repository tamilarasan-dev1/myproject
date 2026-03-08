import hashlib

def generate_hash(text, algorithm='sha256'):
    """
    Generate a hash of the input text using the specified algorithm.
    
    Args:
        text (str): The text to hash
        algorithm (str): The hash algorithm to use (default: 'sha256')
    
    Returns:
        str: Hexadecimal hash string
    """
    hash_obj = hashlib.new(algorithm)
    hash_obj.update(text.encode('utf-8'))
    return hash_obj.hexdigest()


if __name__ == "__main__":
    # Example usage
    text = "Hello, World!"
    
    print(f"Original text: {text}")
    print(f"SHA256: {generate_hash(text, 'sha256')}")
    print(f"SHA512: {generate_hash(text, 'sha512')}")
    print(f"MD5: {generate_hash(text, 'md5')}")
