import pyshorteners

# create a Shortener object
s = pyshorteners.Shortener()

# shorten a URL
short_url = s.tinyurl.short('https://chat.openai.com/?model=text-davinci-002-render')

# print the shortened URL
print(short_url)
