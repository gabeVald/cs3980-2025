
from hash_pass import HashPassword

hash_password = HashPassword()

my_password = "abc123456!"

hashed_pass = hash_password.create_hash(my_password)
print(hashed_pass)