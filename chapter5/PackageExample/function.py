
def my_any(S):
    for x in S:
        if x:
           return True
    return False

def my_all(S):
    for x in S:
        if not x:
           return False
    return True