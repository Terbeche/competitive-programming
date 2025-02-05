from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        n = len(emails)
        unique_emails = set()

        for i in range(n):
            local = emails[i].split("@")[0].split("+")[0].replace(".","")
            doamin = emails[i].split("@")[1]

            email = local + "@" + doamin
            unique_emails.add(email)
        return len(unique_emails)