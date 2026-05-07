class Codec:
    d={}

    #Encodes a URL to a shortened URL.
    def encode(self, longUrl: str) -> str:
        self.d[(key:=str(hash(longUrl)))]=longUrl
        return key
        

        
    #Decodes a shortened URL to its original URL.
    def decode(self, shortUrl: str) -> str:
        return self.d[shortUrl]



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))