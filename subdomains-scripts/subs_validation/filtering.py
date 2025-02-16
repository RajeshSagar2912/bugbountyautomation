def filter_subdomains(all_subdomains_file='filtered_subdomains.txt', waste_subdomains_file='waste_subs.txt', output_file='final_subs.txt'):
    with open(waste_subdomains_file, 'r') as wastefile:
        waste_subdomains = set(wastefile.read().splitlines())
    
    with open(all_subdomains_file, 'r') as infile:
        subdomains = infile.read().splitlines()
    
    useful_subdomains = [subdomain for subdomain in subdomains if subdomain not in waste_subdomains]

    with open(output_file, 'w') as outfile:
        for subdomain in useful_subdomains:
            outfile.write(subdomain + '\n')

    print(f"Filtered subdomains have been saved to {output_file}")

# Directly calling the function with default file names
filter_subdomains()