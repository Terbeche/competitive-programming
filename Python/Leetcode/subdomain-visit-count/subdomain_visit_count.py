class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = {}
        result = []

        for cpdomain in cpdomains:
            number_of_visits = cpdomain.split(" ")[0]
            domain = cpdomain.split(" ")[1]

            domain_list = domain.split(".")
            final_domain_list = []

            if len(domain_list) == 2:
                final_domain_list.append(domain_list[0] + "." + domain_list[1])
                final_domain_list.append(domain_list[1] )
            
            if len(domain_list) == 3:
                final_domain_list.append(domain_list[0] + "." + domain_list[1] + "." + domain_list[2])
                final_domain_list.append(domain_list[1] + "." + domain_list[2])
                final_domain_list.append(domain_list[2] )

            print(final_domain_list)
            for domain in final_domain_list:
                if domain in visits:
                    visits[domain] += int(number_of_visits)
                else:
                    visits[domain] = int(number_of_visits)

        print(visits)
        for key,value in visits.items():
            result.append(str(value) + " " + key)
        
        print(result)
        return result
