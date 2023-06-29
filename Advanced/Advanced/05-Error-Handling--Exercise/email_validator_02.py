import re


class NameTooShortError(Exception):
    """Raised when the name in the email is less than the minimum."""
    pass


class MustContainAtSymbolError(Exception):
    """Raised when the email does not have a @ in it."""
    pass


class InvalidDomainError(Exception):
    """Raised when the domain of the email is not in the listed."""
    pass


class InvalidStartOfEmailError(Exception):
    """Raised when the email starts with other than letter."""
    pass


MIN_LENGTH = 5
VALID_DOMAINS = [".com", ".bg", ".org", ".net"]
DOMAIN_PATTERN = r"\.[a-z]+\b"

while True:
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @.")
    if not email[0].isalpha():
        raise InvalidStartOfEmailError("Email must start with a letter.")
    if len(email.split('@')[0]) < MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters.")
    if re.search(DOMAIN_PATTERN, email).group() not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net.")
    print("Email is valid.")
