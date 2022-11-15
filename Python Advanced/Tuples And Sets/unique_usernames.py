n = int(input())
usernames = set()
for _ in range(n):
    username = input()
    usernames.add(username)
for user in usernames:
    print(user)