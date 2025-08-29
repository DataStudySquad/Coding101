# Day 24: Web Scraping - Extracting Data from the Internet

Welcome to Day 24! Today we're learning web scraping - the art of automatically extracting data from websites. Think of it as having a tireless research assistant who can visit thousands of websites and gather information for you in seconds.

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- Understand what web scraping is and when it's appropriate to use
- Use Python's `requests` library to fetch web pages
- Parse HTML content with `BeautifulSoup`
- Extract specific data from web pages programmatically
- Handle common web scraping challenges (headers, delays, errors)
- Build a weather information scraper
- Practice ethical web scraping principles

## 🌐 What is Web Scraping?

### The Research Assistant Analogy

Imagine you're a researcher who needs to collect information about prices from 100 different online stores:

- **Manual Method**: Visit each website, copy prices by hand into a spreadsheet (takes days)
- **Smart Method**: Write a program that visits each website automatically and extracts the prices (takes minutes)

Web scraping is the smart method - automating the process of extracting information from websites.

### Real-World Applications

```python
# Examples of web scraping uses:
applications = {
    "Price Monitoring": "Track product prices across different stores",
    "News Aggregation": "Collect articles from multiple news sites",  
    "Weather Data": "Gather weather information from meteorological sites",
    "Social Media": "Analyze posts and trends (within platform rules)",
    "Real Estate": "Monitor property listings and prices",
    "Job Searching": "Aggregate job postings from multiple sites",
    "Research": "Collect data for academic or business analysis",
    "SEO Monitoring": "Track website rankings and competitor analysis"
}
```

### When NOT to Scrape

**Important**: Always check a website's `robots.txt` file and terms of service before scraping!

```
❌ DON'T scrape if:
- The website explicitly prohibits it
- There's an official API available
- It could harm the website's performance
- You're scraping personal/private information
- The website has captcha protection

✅ DO scrape when:
- It's for educational/research purposes
- You respect rate limits
- The data is publicly available
- You're not harming the website
- You follow ethical guidelines
```

## 📦 Essential Libraries

### Installing Required Packages

```bash
pip install requests beautifulsoup4 lxml
```

### The requests Library - Your Web Client

```python
import requests

# Think of requests as your web browser, but for Python programs
response = requests.get('https://httpbin.org/json')

# Check if the request was successful
if response.status_code == 200:
    print("Success! Got the webpage")
    print(f"Content length: {len(response.text)} characters")
else:
    print(f"Failed to get webpage. Status code: {response.status_code}")

# Working with JSON responses
json_data = response.json()
print(f"JSON data: {json_data}")

# Working with HTML/text responses
html_content = response.text
print(f"First 100 characters: {html_content[:100]}")
```

### BeautifulSoup - Your HTML Parser

```python
from bs4 import BeautifulSoup
import requests

# Get a webpage
url = 'https://quotes.toscrape.com/'
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.content, 'html.parser')

# BeautifulSoup is like having a smart assistant who can understand HTML structure
print(f"Page title: {soup.title.text}")

# Find elements by tag
quotes = soup.find_all('span', class_='text')
print(f"Found {len(quotes)} quotes on the page")

# Extract text from elements
for i, quote in enumerate(quotes[:3], 1):
    print(f"Quote {i}: {quote.text}")
```

## 🔧 Basic Web Scraping Techniques

### Making HTTP Requests Properly

```python
import requests
import time
from urllib.parse import urljoin, urlparse

def make_request(url, headers=None, timeout=10):
    """
    Make a web request with proper error handling
    Like having a polite visitor who follows website etiquette
    """
    # Default headers to look like a real browser
    default_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    if headers:
        default_headers.update(headers)
    
    try:
        response = requests.get(url, headers=default_headers, timeout=timeout)
        response.raise_for_status()  # Raises an exception for bad status codes
        return response
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def respectful_request(url, delay=1):
    """
    Make requests with delays to be respectful to servers
    """
    response = make_request(url)
    time.sleep(delay)  # Be nice to the server
    return response

# Example usage
url = "https://httpbin.org/user-agent"
response = make_request(url)
if response:
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.json()}")
```

### Parsing HTML Structure

```python
from bs4 import BeautifulSoup
import requests

def parse_webpage_structure(url):
    """
    Analyze the structure of a webpage
    Like having an architect who can read building blueprints
    """
    response = make_request(url)
    if not response:
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    structure = {
        'title': soup.title.text if soup.title else "No title",
        'headings': {
            'h1': len(soup.find_all('h1')),
            'h2': len(soup.find_all('h2')),
            'h3': len(soup.find_all('h3'))
        },
        'paragraphs': len(soup.find_all('p')),
        'links': len(soup.find_all('a')),
        'images': len(soup.find_all('img')),
        'forms': len(soup.find_all('form'))
    }
    
    return structure

# Example: Analyze a webpage structure
url = "https://quotes.toscrape.com/"
structure = parse_webpage_structure(url)
if structure:
    print("📊 Webpage Structure Analysis:")
    print(f"Title: {structure['title']}")
    print(f"Headings: H1={structure['headings']['h1']}, H2={structure['headings']['h2']}, H3={structure['headings']['h3']}")
    print(f"Paragraphs: {structure['paragraphs']}")
    print(f"Links: {structure['links']}")
    print(f"Images: {structure['images']}")
    print(f"Forms: {structure['forms']}")
```

### Finding Elements by Different Methods

```python
from bs4 import BeautifulSoup

def demonstrate_element_selection(html_content):
    """
    Show different ways to find elements in HTML
    Like having different search strategies in a library
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find by tag name
    titles = soup.find_all('h1')
    print(f"H1 tags: {len(titles)}")
    
    # Find by class
    highlighted = soup.find_all(class_='highlight')
    print(f"Elements with 'highlight' class: {len(highlighted)}")
    
    # Find by ID
    main_content = soup.find(id='main-content')
    if main_content:
        print(f"Found element with ID 'main-content'")
    
    # Find by attribute
    external_links = soup.find_all('a', {'target': '_blank'})
    print(f"External links: {len(external_links)}")
    
    # Find using CSS selectors
    navigation_links = soup.select('nav a')
    print(f"Navigation links: {len(navigation_links)}")
    
    # Find with complex conditions
    important_paragraphs = soup.find_all('p', class_=['important', 'highlight'])
    print(f"Important paragraphs: {len(important_paragraphs)}")

# Sample HTML for demonstration
sample_html = """
<html>
<head><title>Sample Page</title></head>
<body>
    <nav>
        <a href="/home">Home</a>
        <a href="/about">About</a>
    </nav>
    <div id="main-content">
        <h1>Welcome</h1>
        <p class="highlight">This is important text.</p>
        <p class="important">This is also important.</p>
        <a href="https://example.com" target="_blank">External Link</a>
    </div>
</body>
</html>
"""

demonstrate_element_selection(sample_html)
```

## 🌤️ Building a Weather Scraper

### Weather Information Extractor

```python
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

class WeatherScraper:
    """
    A weather information scraper that gets data from weather websites
    Like having a personal meteorologist who checks multiple sources
    """
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def get_weather_from_wttr(self, location):
        """
        Get weather data from wttr.in (a terminal-friendly weather service)
        """
        try:
            # wttr.in provides a simple API
            url = f"http://wttr.in/{location}?format=j1"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract current weather
            current = data['current_condition'][0]
            weather_info = {
                'location': location,
                'temperature_c': current['temp_C'],
                'temperature_f': current['temp_F'],
                'description': current['weatherDesc'][0]['value'],
                'humidity': current['humidity'],
                'wind_speed': current['windspeedKmph'],
                'wind_direction': current['winddir16Point'],
                'feels_like_c': current['FeelsLikeC'],
                'feels_like_f': current['FeelsLikeF'],
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'source': 'wttr.in'
            }
            
            return weather_info
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather from wttr.in: {e}")
            return None
        except (KeyError, IndexError, json.JSONDecodeError) as e:
            print(f"Error parsing weather data: {e}")
            return None
    
    def format_weather_report(self, weather_data):
        """
        Format weather data into a readable report
        """
        if not weather_data:
            return "Weather data not available"
        
        report = f"""
🌤️ Weather Report for {weather_data['location']}
{'='*50}
🌡️ Temperature: {weather_data['temperature_c']}°C ({weather_data['temperature_f']}°F)
🌡️ Feels like: {weather_data['feels_like_c']}°C ({weather_data['feels_like_f']}°F)
☁️ Conditions: {weather_data['description']}
💧 Humidity: {weather_data['humidity']}%
💨 Wind: {weather_data['wind_speed']} km/h {weather_data['wind_direction']}
📅 Updated: {weather_data['timestamp']}
📡 Source: {weather_data['source']}
"""
        return report
    
    def get_multiple_locations(self, locations):
        """
        Get weather for multiple locations
        """
        weather_reports = {}
        
        for location in locations:
            print(f"🔍 Fetching weather for {location}...")
            weather_data = self.get_weather_from_wttr(location)
            if weather_data:
                weather_reports[location] = weather_data
                print(f"✅ Got weather data for {location}")
            else:
                print(f"❌ Failed to get weather for {location}")
            
            # Be respectful - add a small delay
            time.sleep(1)
        
        return weather_reports
    
    def save_weather_data(self, weather_data, filename="weather_data.json"):
        """
        Save weather data to a JSON file
        """
        try:
            with open(filename, 'w') as f:
                json.dump(weather_data, f, indent=2)
            print(f"💾 Weather data saved to {filename}")
            return True
        except Exception as e:
            print(f"❌ Error saving weather data: {e}")
            return False
    
    def load_weather_data(self, filename="weather_data.json"):
        """
        Load previously saved weather data
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            print(f"📂 Weather data loaded from {filename}")
            return data
        except FileNotFoundError:
            print(f"📂 No previous weather data found ({filename})")
            return {}
        except Exception as e:
            print(f"❌ Error loading weather data: {e}")
            return {}

# Example usage
def weather_demo():
    """
    Demonstrate the weather scraper
    """
    print("🌤️ Weather Scraping Demo")
    print("-" * 30)
    
    scraper = WeatherScraper()
    
    # Get weather for a single location
    location = "London"
    print(f"Getting weather for {location}...")
    weather = scraper.get_weather_from_wttr(location)
    
    if weather:
        print(scraper.format_weather_report(weather))
    else:
        print("Failed to get weather data")
    
    # Get weather for multiple locations
    cities = ["Tokyo", "New York", "Sydney", "Berlin"]
    print(f"\n🌍 Getting weather for multiple cities: {', '.join(cities)}")
    
    all_weather = scraper.get_multiple_locations(cities)
    
    print(f"\n📊 Weather Summary for {len(all_weather)} cities:")
    for city, data in all_weather.items():
        print(f"   {city}: {data['temperature_c']}°C, {data['description']}")
    
    # Save the data
    scraper.save_weather_data(all_weather)

# Run the demo
if __name__ == "__main__":
    weather_demo()
```

## 📰 News Headlines Scraper

```python
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

class NewsHeadlineScraper:
    """
    Scrape news headlines from publicly available news sites
    Like having a news assistant who reads multiple papers for you
    """
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def scrape_quotes_toscrape(self):
        """
        Scrape quotes from quotes.toscrape.com (a site designed for scraping practice)
        """
        quotes_data = []
        page = 1
        
        while True:
            url = f"https://quotes.toscrape.com/page/{page}/"
            print(f"📖 Scraping page {page}...")
            
            try:
                response = self.session.get(url, timeout=10)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Find all quote containers
                quotes = soup.find_all('div', class_='quote')
                
                if not quotes:
                    print("📝 No more quotes found. Finished scraping.")
                    break
                
                for quote in quotes:
                    # Extract quote text
                    quote_text = quote.find('span', class_='text').text
                    
                    # Extract author
                    author = quote.find('small', class_='author').text
                    
                    # Extract tags
                    tag_elements = quote.find_all('a', class_='tag')
                    tags = [tag.text for tag in tag_elements]
                    
                    quotes_data.append({
                        'text': quote_text,
                        'author': author,
                        'tags': tags,
                        'scraped_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                
                print(f"✅ Found {len(quotes)} quotes on page {page}")
                page += 1
                
                # Be respectful - add a delay between requests
                time.sleep(1)
                
            except requests.exceptions.RequestException as e:
                print(f"❌ Error scraping page {page}: {e}")
                break
        
        return quotes_data
    
    def analyze_quotes(self, quotes_data):
        """
        Analyze the scraped quotes data
        """
        if not quotes_data:
            return "No quotes data to analyze"
        
        # Count quotes by author
        author_counts = {}
        all_tags = []
        
        for quote in quotes_data:
            author = quote['author']
            author_counts[author] = author_counts.get(author, 0) + 1
            all_tags.extend(quote['tags'])
        
        # Count tags
        tag_counts = {}
        for tag in all_tags:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
        
        # Generate analysis report
        report = f"""
📊 Quotes Analysis Report
{'='*40}
📖 Total quotes scraped: {len(quotes_data)}
👥 Total unique authors: {len(author_counts)}
🏷️ Total unique tags: {len(tag_counts)}

📚 Top 5 Authors by Quote Count:
"""
        
        # Sort authors by quote count
        top_authors = sorted(author_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        for i, (author, count) in enumerate(top_authors, 1):
            report += f"   {i}. {author}: {count} quotes\n"
        
        report += "\n🏷️ Top 10 Most Common Tags:\n"
        
        # Sort tags by frequency
        top_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        for i, (tag, count) in enumerate(top_tags, 1):
            report += f"   {i}. {tag}: {count} occurrences\n"
        
        return report
    
    def save_quotes_data(self, quotes_data, filename="scraped_quotes.json"):
        """
        Save scraped quotes to a JSON file
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(quotes_data, f, indent=2, ensure_ascii=False)
            print(f"💾 Quotes data saved to {filename}")
            return True
        except Exception as e:
            print(f"❌ Error saving quotes: {e}")
            return False
    
    def search_quotes(self, quotes_data, search_term):
        """
        Search through scraped quotes
        """
        matching_quotes = []
        search_term = search_term.lower()
        
        for quote in quotes_data:
            # Search in quote text, author, and tags
            if (search_term in quote['text'].lower() or 
                search_term in quote['author'].lower() or 
                any(search_term in tag.lower() for tag in quote['tags'])):
                matching_quotes.append(quote)
        
        return matching_quotes

def quotes_scraping_demo():
    """
    Demonstrate the quotes scraper
    """
    print("📖" * 20)
    print("    QUOTES SCRAPING DEMO")
    print("📖" * 20)
    
    scraper = NewsHeadlineScraper()
    
    # Scrape quotes
    print("🚀 Starting quotes scraping...")
    quotes = scraper.scrape_quotes_toscrape()
    
    if quotes:
        print(f"\n✅ Successfully scraped {len(quotes)} quotes!")
        
        # Show some sample quotes
        print(f"\n📝 Sample quotes:")
        for i, quote in enumerate(quotes[:3], 1):
            print(f"\n{i}. \"{quote['text'][:100]}{'...' if len(quote['text']) > 100 else ''}\"")
            print(f"   — {quote['author']}")
            print(f"   Tags: {', '.join(quote['tags'][:5])}")
        
        # Analyze the data
        analysis = scraper.analyze_quotes(quotes)
        print(analysis)
        
        # Save the data
        scraper.save_quotes_data(quotes)
        
        # Demo search functionality
        search_term = "life"
        matching_quotes = scraper.search_quotes(quotes, search_term)
        print(f"\n🔍 Found {len(matching_quotes)} quotes containing '{search_term}'")
        
        if matching_quotes:
            print(f"\nFirst matching quote:")
            quote = matching_quotes[0]
            print(f"\"{quote['text']}\" — {quote['author']}")
    else:
        print("❌ Failed to scrape any quotes")

if __name__ == "__main__":
    quotes_scraping_demo()
```

## 🛡️ Ethical Web Scraping Best Practices

### Respecting robots.txt

```python
import requests
from urllib.robotparser import RobotFileParser

def check_robots_txt(url, user_agent='*'):
    """
    Check if scraping is allowed according to robots.txt
    Like checking if visitors are welcome before entering a building
    """
    try:
        # Parse the base URL to get the robots.txt location
        from urllib.parse import urljoin, urlparse
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        robots_url = urljoin(base_url, '/robots.txt')
        
        # Create and read robots.txt parser
        rp = RobotFileParser()
        rp.set_url(robots_url)
        rp.read()
        
        # Check if the URL can be fetched
        can_fetch = rp.can_fetch(user_agent, url)
        
        print(f"🤖 Robots.txt check for {url}")
        print(f"   Robots.txt URL: {robots_url}")
        print(f"   Can fetch: {'✅ Yes' if can_fetch else '❌ No'}")
        
        return can_fetch
        
    except Exception as e:
        print(f"⚠️ Could not check robots.txt: {e}")
        print("   Proceed with caution and respect rate limits")
        return None

# Example usage
urls_to_check = [
    "https://quotes.toscrape.com/",
    "https://httpbin.org/",
    "https://example.com/"
]

for url in urls_to_check:
    check_robots_txt(url)
    print()
```

### Rate Limiting and Respectful Scraping

```python
import time
import requests
from datetime import datetime, timedelta

class RespectfulScraper:
    """
    A scraper that follows best practices and is respectful to servers
    Like being a polite guest who doesn't overstay their welcome
    """
    
    def __init__(self, delay_between_requests=1, max_requests_per_minute=30):
        """
        Initialize with rate limiting parameters
        """
        self.delay_between_requests = delay_between_requests
        self.max_requests_per_minute = max_requests_per_minute
        self.request_times = []
        self.session = requests.Session()
        
        # Set a reasonable user agent
        self.session.headers.update({
            'User-Agent': 'Educational Web Scraper (Python/requests) - Contact: student@example.com'
        })
    
    def make_request(self, url):
        """
        Make a request with built-in rate limiting
        """
        # Check rate limiting
        if not self.check_rate_limit():
            print("⏰ Rate limit reached. Waiting...")
            time.sleep(60)  # Wait a minute
            self.request_times.clear()
        
        # Make the request
        try:
            print(f"🌐 Requesting: {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            # Record the request time
            self.request_times.append(datetime.now())
            
            # Respectful delay
            time.sleep(self.delay_between_requests)
            
            return response
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error: {e}")
            return None
    
    def check_rate_limit(self):
        """
        Check if we're within our rate limits
        """
        now = datetime.now()
        # Remove requests older than 1 minute
        self.request_times = [t for t in self.request_times if now - t < timedelta(minutes=1)]
        
        # Check if we're under the limit
        return len(self.request_times) < self.max_requests_per_minute
    
    def scrape_with_retries(self, url, max_retries=3):
        """
        Scrape with retry logic for failed requests
        """
        for attempt in range(max_retries):
            response = self.make_request(url)
            if response:
                return response
            
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"⏳ Retrying in {wait_time} seconds... (attempt {attempt + 1}/{max_retries})")
                time.sleep(wait_time)
        
        print(f"❌ Failed to fetch {url} after {max_retries} attempts")
        return None

# Example usage
scraper = RespectfulScraper(delay_between_requests=2, max_requests_per_minute=20)

urls_to_scrape = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/user-agent",
    "https://httpbin.org/headers"
]

for url in urls_to_scrape:
    response = scraper.scrape_with_retries(url)
    if response:
        print(f"✅ Success: {response.status_code}")
    print()
```

## 🏃‍♂️ Practice Exercises

### Exercise 1: Book Information Scraper
Create a scraper for book information:

```python
def scrape_book_info(book_url):
    """
    Scrape book information from a book listing page
    Extract: title, author, price, rating, description
    """
    # Your code here
    pass
```

### Exercise 2: Job Listings Aggregator
Build a job scraper (for practice sites only):

```python
def scrape_job_listings(search_term, location):
    """
    Scrape job listings based on search criteria
    Return: title, company, location, salary, description
    """
    # Your code here
    pass
```

### Exercise 3: Social Media Post Analyzer
Create a tool to analyze public posts:

```python
def analyze_public_posts(hashtag):
    """
    Analyze public posts for a specific hashtag
    Return: sentiment analysis, common themes, posting frequency
    """
    # Your code here
    pass
```

## 📝 Key Takeaways

1. **Always check robots.txt** - Respect website scraping policies
2. **Use appropriate delays** - Don't overwhelm servers with requests
3. **Handle errors gracefully** - Websites can be unreliable
4. **Check for APIs first** - Many sites offer official APIs
5. **Inspect HTML structure** - Use browser dev tools to understand the page
6. **Be respectful** - Your scraping shouldn't harm the website
7. **Stay legal and ethical** - Follow terms of service and applicable laws

## 🎯 Today's Project Preview

Today you'll build a **Multi-Source Information Aggregator** that demonstrates professional web scraping. It will:
- Scrape weather information from multiple sources
- Extract news headlines and summaries
- Collect quotes and inspirational content
- Implement respectful rate limiting
- Handle errors and retries gracefully
- Generate comprehensive reports from scraped data
- Save data in multiple formats (JSON, CSV)

The goal is to create a useful tool while following ethical scraping practices!

## 🔗 Connection to Previous Days

### Building on Previous Skills
- **Regular Expressions (Day 23)**: Clean and validate scraped data
- **File Handling (Day 19)**: Save scraped data to files
- **Error Handling (Day 20)**: Handle network errors gracefully
- **Functions (Day 15-16)**: Organize scraping logic into reusable functions

### Looking Forward
Web scraping skills will enhance:
- **Data Processing (Day 26)**: Scrape data for analysis
- **Final Projects**: Gather real-world data for applications

Web scraping opens up a world of data possibilities, but remember: with great power comes great responsibility. Always scrape ethically and respectfully!