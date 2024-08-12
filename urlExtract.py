import re

def save_urls_to_file(urls, file_path):
    """
    Saves a list of URLs to a text file.
    
    Args:
        urls (list of str): List of URLs to save.
        file_path (str): Path to the output text file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        for url in urls:
            file.write(url + '\n')
    print(f'URLs have been saved to {file_path}')


def extract_facebook_urls(text):
    """
    Extracts all URLs from connect.facebook.net domain from the given text.
    
    Args:
        text (str): The input text containing URLs.
    
    Returns:
        list: A list of extracted URLs from connect.facebook.net.
    """
    # Regular expression to match URLs containing 'connect.facebook.net'
    facebook_url_pattern = r'https://connect\.facebook\.net/[^\s,]+'
    urls = re.findall(facebook_url_pattern, text)
    return urls

# Example text (replace this with your actual text)
text = """
URL	MIME Type	From	To	Captures	Duplicates	Uniques
https://connect.facebook.net/signals/config/1264059003707256?v=2.7.19	application/x-javascript	Aug 1, 2019	Aug 1, 2019	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.7.21	application/x-javascript	Sep 12, 2017	Sep 12, 2017	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.8.1	application/x-javascript	May 18, 2019	May 18, 2019	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.8.11&r=stable	application/x-javascript	Apr 23, 2020	Apr 23, 2020	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.8.12&r=c2	application/x-javascript	Apr 8, 2018	Apr 8, 2018	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.8.12&r=stable	application/x-javascript	Mar 23, 2018	Apr 13, 2018	2	0	2
https://connect.facebook.net/signals/config/1264059003707256?v=2.8.14&r=stable	application/x-javascript	May 7, 2018	May 7, 2018	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.8.30&r=stable	application/x-javascript	Oct 21, 2018	Oct 21, 2018	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.8.35&r=stable	application/x-javascript	Jan 6, 2019	Jan 8, 2019	2	1	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.8.37&r=stable	application/x-javascript	Jan 10, 2019	Jan 10, 2019	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.8.46&r=stable	application/x-javascript	Jul 10, 2020	Jul 10, 2020	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.8.47&r=stable	application/x-javascript	May 10, 2019	May 17, 2019	3	1	2
https://connect.facebook.net/signals/config/1264059003707256?v=2.8.51&r=c2	application/x-javascript	Jun 4, 2020	Jun 4, 2020	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.8.6&r=stable	application/x-javascript	May 4, 2020	May 4, 2020	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.8.8&r=stable	application/x-javascript	Feb 1, 2018	Feb 1, 2018	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.100&r=stable	application/x-javascript	Mar 28, 2023	Apr 5, 2023	6	5	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.102&r=stable	application/x-javascript	Apr 22, 2023	Apr 22, 2023	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.11&r=stable	application/x-javascript	Jun 18, 2020	Jun 18, 2020	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.13&r=stable	application/x-javascript	Jun 18, 2020	Jun 18, 2020	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.131&r=stable&domain=www.riteaid.com	application/x-javascript	Sep 30, 2023	Sep 30, 2023	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.14&r=stable	application/x-javascript	Dec 10, 2019	Dec 10, 2019	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.15&r=stable	application/x-javascript	Mar 12, 2020	Mar 12, 2020	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.18&r=stable	application/x-javascript	Jun 4, 2020	Jun 18, 2020	2	0	2
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.2&r=stable	application/x-javascript	Aug 11, 2019	Aug 11, 2019	6	5	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.21&r=stable	application/x-javascript	Jul 2, 2020	Jul 2, 2020	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.22&r=stable	application/x-javascript	Jul 9, 2020	Aug 5, 2020	2	0	2
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.23&r=stable	application/x-javascript	Aug 6, 2020	Aug 30, 2020	23	19	4
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.24&r=stable	warc/revisit	Aug 31, 2020	Sep 28, 2020	25	20	5
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.26&r=stable	application/x-javascript	Sep 29, 2020	Sep 30, 2020	2	0	2
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.27&r=stable	application/x-javascript	Oct 1, 2020	Nov 11, 2020	34	27	7
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.28&r=stable	application/x-javascript	Nov 13, 2020	Nov 20, 2020	5	3	2
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.29&r=stable	application/x-javascript	Nov 21, 2020	Dec 9, 2020	11	8	3
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.30&r=stable	warc/revisit	Dec 10, 2020	Dec 21, 2020	11	7	4
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.31&r=stable	application/x-javascript	Dec 22, 2020	Dec 31, 2020	10	6	4
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.33&r=stable	application/x-javascript	Apr 12, 2021	Apr 12, 2021	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.39&r=stable	application/x-javascript	Apr 14, 2021	May 13, 2021	11	0	11
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.4&r=stable	application/x-javascript	Jun 18, 2020	Jun 18, 2020	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.40&r=stable	application/x-javascript	May 23, 2021	Jun 8, 2021	14	1	13
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.41&r=stable	application/x-javascript	Jun 10, 2021	Jun 24, 2021	14	3	11
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.42&r=stable	application/x-javascript	Jun 25, 2021	Jul 1, 2021	7	1	6
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.43&r=stable	application/x-javascript	Jul 2, 2021	Jul 29, 2021	26	0	26
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.44&r=stable	application/x-javascript	Jul 30, 2021	Aug 25, 2021	27	1	26
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.45&r=stable	application/x-javascript	Aug 26, 2021	Sep 21, 2021	26	0	26
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.46&r=stable	application/x-javascript	Sep 22, 2021	Sep 28, 2021	7	0	7
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.47&r=stable	application/x-javascript	Sep 29, 2021	Oct 28, 2021	28	1	27
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.48&r=stable	application/x-javascript	Oct 29, 2021	Jan 18, 2022	75	3	72
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.49&r=stable	application/x-javascript	Jan 19, 2022	Jan 24, 2022	6	0	6
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.5&r=c2	application/x-javascript	Oct 28, 2020	Jan 30, 2023	6	2	4
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.5&r=stable	application/x-javascript	Oct 14, 2019	Oct 29, 2019	3	1	2
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.51&r=stable	application/x-javascript	Jan 25, 2022	Jan 31, 2022	8	0	8
URL	MIME Type	From	To	Captures	Duplicates	Uniques
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.52&r=stable	application/x-javascript	Feb 1, 2022	Mar 2, 2022	24	1	23
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.55&r=stable	application/x-javascript	Mar 4, 2022	Mar 12, 2022	3	0	3
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.57&r=stable	application/x-javascript	Mar 24, 2022	May 4, 2022	31	1	30
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.58&r=stable	application/x-javascript	May 5, 2022	May 10, 2022	6	0	6
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.59&r=stable	application/x-javascript	May 11, 2022	May 31, 2022	7	0	7
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.6&r=stable	application/x-javascript	Jun 18, 2020	Jun 18, 2020	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.60&r=stable	application/x-javascript	May 17, 2022	May 24, 2022	8	0	8
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.61&r=stable	application/x-javascript	May 25, 2022	Jun 8, 2022	15	0	15
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.62&r=stable	application/x-javascript	Jun 11, 2022	Jun 28, 2022	16	0	16
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.64&r=canary	application/x-javascript	Jun 29, 2022	Jun 29, 2022	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.64&r=stable	application/x-javascript	Jun 30, 2022	Jul 13, 2022	12	0	12
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.65&r=stable	application/x-javascript	Jul 14, 2022	Jul 18, 2022	5	0	5
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.77&r=stable	application/x-javascript	Aug 25, 2022	Aug 27, 2022	2	0	2
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.78&r=stable	application/x-javascript	Aug 28, 2022	Sep 1, 2022	4	0	4
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.79&r=stable	application/x-javascript	Sep 2, 2022	Sep 14, 2022	13	0	13
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.81&r=stable	application/x-javascript	Sep 15, 2022	Sep 16, 2022	2	0	2
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.83&r=stable	application/x-javascript	Sep 17, 2022	Sep 24, 2022	6	0	6
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.84&r=stable	application/x-javascript	Sep 25, 2022	Oct 14, 2022	18	1	17
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.85&r=stable	application/x-javascript	Oct 15, 2022	Oct 18, 2022	4	0	4
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.86&r=stable	application/x-javascript	Oct 19, 2022	Oct 19, 2022	1	0	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.87&r=stable	application/x-javascript	Oct 21, 2022	Oct 25, 2022	6	0	6
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.89&r=stable	application/x-javascript	Oct 29, 2022	Dec 14, 2022	37	4	33
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.90&r=stable	application/x-javascript	Dec 18, 2022	Jan 2, 2023	9	0	9
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.91&r=stable	application/x-javascript	Jan 5, 2023	Jan 11, 2023	7	0	7
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.92&r=stable	application/x-javascript	Jan 14, 2023	Jan 29, 2023	8	0	8
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.94&r=stable	application/x-javascript	Jan 20, 2023	Jan 26, 2023	6	0	6
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.95&r=stable	application/x-javascript	Feb 2, 2023	Feb 15, 2023	13	11	2
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.96&r=stable	warc/revisit	Feb 17, 2023	Feb 23, 2023	4	2	2
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.97&r=stable	warc/revisit	Feb 25, 2023	Feb 28, 2023	5	4	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.98&r=stable	warc/revisit	Mar 4, 2023	Mar 16, 2023	4	3	1
https://connect.facebook.net/signals/config/1264059003707256?v=2.9.99&r=stable	warc/revisit	Mar 18, 2023	Mar 19, 2023	2	1	1
https://connect.facebook.net/signals/config/1264059003707256?v=next&r=canary	application/x-javascript	Jul 26, 2021	Jun 18, 2022	3	0	3




"""

# Extract URLs
facebook_urls = extract_facebook_urls(text)
output_file_path = 'riteaid_pixel_js.txt'
save_urls_to_file(facebook_urls, output_file_path)

# Print the extracted URLs
for url in facebook_urls:
    print(url)

print(len(facebook_urls))