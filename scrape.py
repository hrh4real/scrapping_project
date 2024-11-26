from playwright.sync_api import sync_playwright


def scrape_quotes (playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto('https://quotes.toscrape.com')
    
    quotes = page.locator('.text').all_text_contents()
    for quote in quotes:
        print(quote)
    browser.close()
    
with sync_playwright() as playwright:
    scrape_quotes(playwright)


# from playwright.sync_api import sync_playwright

# def run(playwright):
#     # Launch the browser
#     browser = playwright.chromium.launch()
    
#     # Create a new page
#     page = browser.new_page()  # Corrected: Added parentheses
    
#     # Navigate to the URL
#     page.goto('https://example.com')
    
#     # Print the page title
#     print(page.title())
    
#     # Close the browser
#     browser.close()

# # Use the sync_playwright context manager
# with sync_playwright() as playwright:
#     run(playwright)