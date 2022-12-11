import errors


valid_domains = {".bg", ".com", ".org", ".net"}

while True:
    line = input()
    if line == "End":
        break
    email_parts = line.split("@")

    if len(email_parts) != 2:
        raise errors.MustContainAtSymbol("Email must contain @")
    name, domain_parts = email_parts[0], email_parts[1]

    if len(name) <= 4:
        raise errors.NameTooShort("Name must be more than 4 characters")
    domain = '.' + domain_parts.split('.')[-1]

    if domain not in valid_domains:
        raise errors.InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")
    print("Email is valid")