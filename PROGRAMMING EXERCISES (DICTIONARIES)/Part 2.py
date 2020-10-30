def accept_login(users, username, password):
    for x in sorted(users.keys()):
        if username == x:
            if password == users.get(x):
                return True
            else: return False
    return False
def main():
    mydict = { 'a' : 0, 'b': 1, 'c' : 2}
    print(accept_login(mydict,username='b',password=1))

main()