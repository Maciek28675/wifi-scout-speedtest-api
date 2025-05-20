import os
import secrets

def generate_file(size_mb: int, filename: str):
    """
        Generate a binary file of size_bytes with random bytes.

        Args:
            size_bytes: int
                size of generated file.
            filename: str
                name of the generated file.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "wb") as f:
        for _ in range(size_mb):
            f.write(secrets.token_bytes(1000 * 1000))

if __name__ == '__main__':
    for size_mb in [1, 10, 25]:
        generate_file(size_mb, f'./static/files/{size_mb}MB.bin')