import re

def replace_substr_in_url(url):
    # Define the pattern to match the substring to be replaced
    pattern = r'_SX\d+_SY\d+_CR,\d+,\d+,\d+,\d+_'

    # Use re.sub to replace the matched pattern with "_SX689_"
    modified_url = re.sub(pattern, '_SX689_', url)

    return modified_url

# Example usage:
url = "https://m.media-amazon.com/images/I/31ahZ5LVYoL._SX38_SY50_CR,0,0,38,50_.jpg"
modified_url = replace_substr_in_url(url)

print(modified_url)
