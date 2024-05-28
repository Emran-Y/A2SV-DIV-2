# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_parent = defaultdict(str)
        email_to_name = defaultdict(str)
        
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_parent[email] = email
                email_to_name[email] = name
        
        def find_parent(email):
            if email_parent[email] != email:
                email_parent[email] = find_parent(email_parent[email])
            return email_parent[email]
        
        def union(email1, email2):
            root1 = find_parent(email1)
            root2 = find_parent(email2)
            
            if root1 != root2:
                email_parent[root2] = root1

        for account in accounts:
            first_email = account[1]
            for email in account[2:]:
                union(first_email, email)
        
        merged_emails = defaultdict(list)
        for email in email_parent:
            root_email = find_parent(email)
            merged_emails[root_email].append(email)
        
        result = []
        for root_email, emails in merged_emails.items():
            emails.sort()
            account = [email_to_name[root_email]] + emails
            result.append(account)
        
        return result
