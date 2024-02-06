

# def domain_hits(inputStr):
#     domains = ['app.atlantichealth.org', 'app.atlantichealth.org', 
#         'api.atlantichealth.org', 'myatlantic.atlantichealth.org', 
#         'myatlantic.atlantichealth.org', 'test.app.atlantichealth.org', 
#         'test.app.atlantichealth.org', 'myatlantic.atlantichealth.org', 
#         'marketing.atlantichealth.org', 'marketing.atlantichealth.org', 
#         'healthcare.org', 'app.healthcare.org', 'healthcare.org', 
#         'google.com', 'api.google.com', 'app.google.atlantichealth.org', 
#         'google.com'] 
#     count_dict = {}
#     component = inputStr.split('.')
#     for domain in domains:
#         cur_domain = domain.split('.')
#         current_domain = ''
#         for component in reversed(cur_domain):
#             current_domain = component + '.' + current_domain if current_domain else component
#             count_dict[current_domain] += 1
#     return count_dict

    
# res = domain_hits("app.atlantichealth.org")
# print(res)


from collections import defaultdict

def count_domain_hits(domains):
    domain_counts = defaultdict(int)

    for domain in domains:
        components = domain.split('.')
        current_domain = ''
        
        for component in reversed(components):
            print(component)
            current_domain = component + '.' + current_domain if current_domain else component
            domain_counts[current_domain] += 1

    return domain_counts

# Example usage:
domains = ['app.atlantichealth.org', 'app.atlantichealth.org', 'api.atlantichealth.org', 
           'myatlantic.atlantichealth.org', 'myatlantic.atlantichealth.org', 
           'test.app.atlantichealth.org', 'test.app.atlantichealth.org', 
           'myatlantic.atlantichealth.org', 'marketing.atlantichealth.org', 
           'marketing.atlantichealth.org', 'healthcare.org', 'app.healthcare.org', 
           'healthcare.org', 'google.com', 'api.google.com', 
           'app.google.atlantichealth.org', 'google.com']

result = count_domain_hits(domains)
for domain, count in result.items():
    print(f'{domain}: {count}')
