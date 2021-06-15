# CC-Item-Stock-Crawler

I wrote this (call it what you want) web scraping bot specifically tailored for Canada Computers. Since the pandemic has been quite merciless with scalpers and miners, I decided to write a solution that fits my needs to grab a GPU before anyone else does and sells it for 200% of the MSRP. 
I haven't really picked up a GPU yet but this has been tested on products in stock and out of stock and it works.

The way it works is simple, each scan (after the delay you chose in minutes) will scrape new data direct from the item's URL webpage. So even if the item goes in stock while the program is running and is missed by the ongoing scan, the scan right after will pick up the change and provide a loud beep along with a message that it's in stock even your neighbor will know.

Ctrl+C should close the program and open up the webpage in your chosen browser that takes you direct to the product's page.

I've only seen 1 reported glitch with an In-Stock product still being detected as out-of-stock, but seems to work just fine with everything else.

This is a personal solution that I wrote from scratch and I'm sharing with whoever sees this. I am in no circumstance responsible for any illegitimate activity you use this code for or if you get your IP blocked by spam scraping with low delay time.

In my experience, using 10 minutes delay time hasn't gotten my IP address blocked, whereas when I tested 5 minutes it got blocked. Feel free to find the sweet spot at your own risk/responsibility. 
