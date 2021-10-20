def contains_palindrome(words):
    for word in words:
        if word ==  ''.join(reversed(word)):
            return True

    return False


def contains_palindrome2(words):
    return any(word == ''.join(reversed(word)) for word in words)

print(contains_palindrome2('aba'))
print(contains_palindrome('aba'))
print(any(num == 10 for num in range(100_000_000)))
print(any([num == 10 for num in range(100_000_000)]))
