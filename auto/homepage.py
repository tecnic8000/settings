import webbrowser

# List of URLs to open
urls = [
    "https://www.youtube.com",
    "https://www.reddit.com",
    "https://iboard.ssi.com.vn/",
    "https://docs.google.com/spreadsheets/d/10zk6n_zRKplUFY05JAN8Qt3Tk1kF_7a_SLRKUinmyiQ/edit?gid=0#gid=0"
]
# Open the first URL in a new window
webbrowser.open_new(urls[0])

# Open the remaining URLs in new tabs in the same window
for url in urls[1:]:
    webbrowser.open_new_tab(url)