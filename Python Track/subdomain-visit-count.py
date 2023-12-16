class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        store = {}
        for element in cpdomains:
            sp_cp = element.split()
            times, domain = int(sp_cp[0]), sp_cp[1]
            domain = domain.split(".")
            i = len(domain) -1
            j = i + 1
            while i >= 0:
                sub = '.'.join(domain[i:j])
                store[sub] = store.get(sub, 0) + times
                i -= 1
        return [str(value) + " " + key for key, value in store.items()]