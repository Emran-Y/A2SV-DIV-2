class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.life = timeToLive
        self.store = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.store[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.store:
            if self.store[tokenId] + self.life > currentTime:
                self.store[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        c = 0
        for value in self.store.values():
            if value + self.life > currentTime:
                c+=1
        return c


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)