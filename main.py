from exa_py import Exa

exa = Exa('your_exa_api_key_here')

query = input('Search here: ')

response = exa.search(
  query,
  num_results=15,
  type='keyword',
  include_domains=['https://scholar.google.com/']
)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()