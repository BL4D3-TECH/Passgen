class encoder:
    def __init__(self):
        self.result = ""

    def swap(self, string):
        return "".join([f":{str(ord(char))[::-1]}:" for char in string])
    
    def unswap(self, code):
        return "".join([chr(int(char[::-1])) for char in code.split(":") if char != ""])

if __name__ == "__main__":
    obj = crypton()
    encrypt = obj.swap("hello world")
    unencrypt = obj.unswap(crpyted)

    print(unencrypt, "=", encrypt)