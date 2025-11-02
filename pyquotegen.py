import pyquotegen

from Quotes_gen_api import author

# Get a random quote
quote = pyquotegen.get_quote()
print(quote)

# Get a quote by category (e.g., “inspirational”)
quote2 = pyquotegen.get_quote("inspirational")
print(quote2)

quote3 = pyquotegen.get_quote("coding")
print(quote3)
