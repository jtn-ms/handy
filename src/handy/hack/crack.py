from brute import brute

def demo():
    for trystr in brute(start_length=3,length=5, letters=False, numbers=True, symbols=True, spaces=True):
        print(trystr)
        
if __name__ == "__main__":
    demo()