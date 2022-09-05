
# Command to refresh the data in scrapers every 64 hours
0 * * * * t=$(date +\%s); [ "$(( (t / 3600) \% 64 ))" -eq 0 ] && python scraper/scraper.py
