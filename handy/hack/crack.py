from brute import brute

def demo():
    for trystr in brute(length=5, letters=False, numbers=True, symbols=False):
        print(trystr)
        
if __name__ == "__main__":
    demo()