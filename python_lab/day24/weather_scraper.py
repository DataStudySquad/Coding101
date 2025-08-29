#!/usr/bin/env python3
"""
Day 24: Multi-Source Information Aggregator
A comprehensive web scraping tool that demonstrates ethical data extraction

This program showcases:
- Respectful web scraping with rate limiting
- Multiple data source integration
- Error handling and retry mechanisms
- Data cleaning and validation
- Multiple output formats (JSON, CSV)
- Professional scraping practices

Think of this as your personal data collection assistant!
"""

import requests
from bs4 import BeautifulSoup
import json
import csv
import time
import re
from datetime import datetime, timedelta
from pathlib import Path
from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin, urlparse


class RespectfulScraper:
    """
    A base class for ethical web scraping with built-in rate limiting
    Like having a polite assistant who always follows proper etiquette
    """
    
    def __init__(self, delay=1, max_requests_per_minute=30):
        """
        Initialize the scraper with rate limiting parameters
        """
        self.delay_between_requests = delay
        self.max_requests_per_minute = max_requests_per_minute
        self.request_times = []
        self.session = requests.Session()
        
        # Set a professional user agent
        self.session.headers.update({
            'User-Agent': 'Educational Web Scraper (Python/requests) - Learning Project'
        })
        
        print(f"🤖 Respectful Scraper initialized")
        print(f"   ⏰ Delay between requests: {delay} seconds")
        print(f"   📊 Max requests per minute: {max_requests_per_minute}")
    
    def check_robots_txt(self, url):
        """
        Check if scraping is allowed according to robots.txt
        """
        try:
            parsed_url = urlparse(url)
            base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
            robots_url = urljoin(base_url, '/robots.txt')
            
            rp = RobotFileParser()
            rp.set_url(robots_url)
            rp.read()
            
            can_fetch = rp.can_fetch('*', url)
            print(f"🤖 Robots.txt check: {'✅ Allowed' if can_fetch else '❌ Disallowed'}")
            
            return can_fetch
            
        except Exception as e:
            print(f"⚠️ Could not check robots.txt: {e}")
            return True  # Assume allowed if can't check
    
    def check_rate_limit(self):
        """
        Check if we're within rate limits
        """
        now = datetime.now()
        # Remove requests older than 1 minute
        self.request_times = [t for t in self.request_times if now - t < timedelta(minutes=1)]
        
        return len(self.request_times) < self.max_requests_per_minute
    
    def make_request(self, url, timeout=10):
        """
        Make a web request with rate limiting and error handling
        """
        # Check rate limiting
        if not self.check_rate_limit():
            print("⏰ Rate limit reached. Waiting 60 seconds...")
            time.sleep(60)
            self.request_times.clear()
        
        try:
            print(f"🌐 Requesting: {url}")
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()
            
            # Record request time
            self.request_times.append(datetime.now())
            
            # Respectful delay
            time.sleep(self.delay_between_requests)
            
            return response
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
            return None
    
    def make_request_with_retry(self, url, max_retries=3):
        """
        Make a request with retry logic
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


class WeatherScraper(RespectfulScraper):
    """
    Scrape weather information from multiple sources
    Like having a meteorologist who checks multiple weather stations
    """
    
    def __init__(self):
        super().__init__(delay=2)  # Be extra respectful to weather services
        self.weather_data = []
    
    def get_weather_from_wttr(self, location):
        """
        Get weather data from wttr.in (designed for programmatic access)
        """
        try:
            url = f"http://wttr.in/{location}?format=j1"
            response = self.make_request(url)
            
            if not response:
                return None
            
            data = response.json()
            current = data['current_condition'][0]
            
            weather_info = {
                'location': location,
                'temperature_c': int(current['temp_C']),
                'temperature_f': int(current['temp_F']),
                'description': current['weatherDesc'][0]['value'],
                'humidity': int(current['humidity']),
                'wind_speed_kmh': int(current['windspeedKmph']),
                'wind_direction': current['winddir16Point'],
                'feels_like_c': int(current['FeelsLikeC']),
                'feels_like_f': int(current['FeelsLikeF']),
                'visibility': int(current['visibility']),
                'pressure': int(current['pressure']),
                'cloud_cover': int(current['cloudcover']),
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'source': 'wttr.in'
            }
            
            # Add forecast data
            weather_info['forecast'] = []
            for day in data['weather'][:3]:  # Next 3 days
                forecast_day = {
                    'date': day['date'],
                    'max_temp_c': int(day['maxtempC']),
                    'min_temp_c': int(day['mintempC']),
                    'max_temp_f': int(day['maxtempF']),
                    'min_temp_f': int(day['mintempF']),
                    'description': day['hourly'][0]['weatherDesc'][0]['value']
                }
                weather_info['forecast'].append(forecast_day)
            
            return weather_info
            
        except Exception as e:
            print(f"❌ Error getting weather for {location}: {e}")
            return None
    
    def get_multiple_locations(self, locations):
        """
        Get weather for multiple locations
        """
        weather_reports = {}
        
        for location in locations:
            print(f"🌤️ Getting weather for {location}...")
            weather = self.get_weather_from_wttr(location)
            
            if weather:
                weather_reports[location] = weather
                self.weather_data.append(weather)
                print(f"✅ Success: {location} - {weather['temperature_c']}°C, {weather['description']}")
            else:
                print(f"❌ Failed to get weather for {location}")
        
        return weather_reports
    
    def format_weather_report(self, weather_data):
        """
        Create a formatted weather report
        """
        if not weather_data:
            return "No weather data available"
        
        report = f"""
🌤️ Weather Report for {weather_data['location']}
{'='*50}
📍 Location: {weather_data['location']}
🌡️ Temperature: {weather_data['temperature_c']}°C ({weather_data['temperature_f']}°F)
🌡️ Feels like: {weather_data['feels_like_c']}°C ({weather_data['feels_like_f']}°F)
☁️ Conditions: {weather_data['description']}
💧 Humidity: {weather_data['humidity']}%
💨 Wind: {weather_data['wind_speed_kmh']} km/h {weather_data['wind_direction']}
👁️ Visibility: {weather_data['visibility']} km
🌀 Pressure: {weather_data['pressure']} mb
☁️ Cloud Cover: {weather_data['cloud_cover']}%
📅 Updated: {weather_data['timestamp']}
"""
        
        if weather_data.get('forecast'):
            report += "\n📅 3-Day Forecast:\n"
            for day in weather_data['forecast']:
                report += f"   {day['date']}: {day['min_temp_c']}-{day['max_temp_c']}°C, {day['description']}\n"
        
        return report


class QuoteScraper(RespectfulScraper):
    """
    Scrape inspirational quotes from quotes.toscrape.com
    This site is specifically designed for scraping practice
    """
    
    def __init__(self):
        super().__init__(delay=1)
        self.quotes_data = []
    
    def scrape_all_quotes(self):
        """
        Scrape all quotes from the website
        """
        base_url = "https://quotes.toscrape.com"
        
        # Check robots.txt first
        if not self.check_robots_txt(base_url):
            print("❌ Scraping not allowed by robots.txt")
            return []
        
        quotes = []
        page = 1
        
        while True:
            url = f"{base_url}/page/{page}/"
            print(f"📖 Scraping quotes page {page}...")
            
            response = self.make_request(url)
            if not response:
                break
            
            soup = BeautifulSoup(response.content, 'html.parser')
            quote_divs = soup.find_all('div', class_='quote')
            
            if not quote_divs:
                print("📝 No more quotes found")
                break
            
            page_quotes = []
            for quote_div in quote_divs:
                try:
                    text = quote_div.find('span', class_='text').text.strip('"')
                    author = quote_div.find('small', class_='author').text
                    
                    # Get tags
                    tag_links = quote_div.find_all('a', class_='tag')
                    tags = [tag.text for tag in tag_links]
                    
                    quote_data = {
                        'text': text,
                        'author': author,
                        'tags': tags,
                        'length': len(text),
                        'word_count': len(text.split()),
                        'scraped_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'page': page
                    }
                    
                    quotes.append(quote_data)
                    page_quotes.append(quote_data)
                    
                except Exception as e:
                    print(f"⚠️ Error parsing quote: {e}")
                    continue
            
            print(f"✅ Found {len(page_quotes)} quotes on page {page}")
            page += 1
            
            # Safety limit to prevent infinite loops
            if page > 20:  # The site has about 10 pages
                break
        
        self.quotes_data = quotes
        print(f"🎯 Total quotes scraped: {len(quotes)}")
        return quotes
    
    def analyze_quotes(self):
        """
        Analyze the scraped quotes data
        """
        if not self.quotes_data:
            return "No quotes data to analyze"
        
        # Author analysis
        author_counts = {}
        tag_counts = {}
        total_words = 0
        total_chars = 0
        
        for quote in self.quotes_data:
            # Count authors
            author = quote['author']
            author_counts[author] = author_counts.get(author, 0) + 1
            
            # Count tags
            for tag in quote['tags']:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
            
            # Accumulate stats
            total_words += quote['word_count']
            total_chars += quote['length']
        
        # Calculate averages
        avg_words = total_words / len(self.quotes_data)
        avg_chars = total_chars / len(self.quotes_data)
        
        # Create analysis report
        report = f"""
📊 Quotes Analysis Report
{'='*40}
📖 Total quotes: {len(self.quotes_data)}
👥 Unique authors: {len(author_counts)}
🏷️ Unique tags: {len(tag_counts)}
📏 Average words per quote: {avg_words:.1f}
📏 Average characters per quote: {avg_chars:.1f}

👑 Top 10 Authors by Quote Count:
"""
        
        # Top authors
        top_authors = sorted(author_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        for i, (author, count) in enumerate(top_authors, 1):
            report += f"   {i:2d}. {author}: {count} quotes\n"
        
        report += "\n🏷️ Top 15 Most Popular Tags:\n"
        
        # Top tags
        top_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:15]
        for i, (tag, count) in enumerate(top_tags, 1):
            report += f"   {i:2d}. {tag}: {count} occurrences\n"
        
        return report
    
    def search_quotes(self, search_term, search_in=['text', 'author', 'tags']):
        """
        Search through quotes for specific terms
        """
        matching_quotes = []
        search_term = search_term.lower()
        
        for quote in self.quotes_data:
            match_found = False
            
            if 'text' in search_in and search_term in quote['text'].lower():
                match_found = True
            elif 'author' in search_in and search_term in quote['author'].lower():
                match_found = True
            elif 'tags' in search_in and any(search_term in tag.lower() for tag in quote['tags']):
                match_found = True
            
            if match_found:
                matching_quotes.append(quote)
        
        return matching_quotes


class DataExporter:
    """
    Export scraped data in various formats
    Like having a secretary who can prepare reports in any format you need
    """
    
    def __init__(self, output_dir="scraped_data"):
        """
        Initialize the exporter with an output directory
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        print(f"📁 Data exporter initialized. Output directory: {self.output_dir}")
    
    def export_to_json(self, data, filename, pretty=True):
        """
        Export data to JSON format
        """
        try:
            filepath = self.output_dir / f"{filename}.json"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                if pretty:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                else:
                    json.dump(data, f, ensure_ascii=False)
            
            print(f"💾 Data exported to JSON: {filepath}")
            return str(filepath)
            
        except Exception as e:
            print(f"❌ Error exporting to JSON: {e}")
            return None
    
    def export_quotes_to_csv(self, quotes_data, filename):
        """
        Export quotes to CSV format
        """
        try:
            filepath = self.output_dir / f"{filename}.csv"
            
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Write header
                writer.writerow(['Text', 'Author', 'Tags', 'Word Count', 'Character Count', 'Scraped At'])
                
                # Write data
                for quote in quotes_data:
                    writer.writerow([
                        quote['text'],
                        quote['author'],
                        ', '.join(quote['tags']),
                        quote['word_count'],
                        quote['length'],
                        quote['scraped_at']
                    ])
            
            print(f"💾 Quotes exported to CSV: {filepath}")
            return str(filepath)
            
        except Exception as e:
            print(f"❌ Error exporting quotes to CSV: {e}")
            return None
    
    def export_weather_to_csv(self, weather_data, filename):
        """
        Export weather data to CSV format
        """
        try:
            filepath = self.output_dir / f"{filename}.csv"
            
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Write header
                writer.writerow([
                    'Location', 'Temperature_C', 'Temperature_F', 'Feels_Like_C', 'Feels_Like_F',
                    'Description', 'Humidity', 'Wind_Speed_KMH', 'Wind_Direction',
                    'Visibility', 'Pressure', 'Cloud_Cover', 'Timestamp'
                ])
                
                # Write data
                for location, weather in weather_data.items():
                    writer.writerow([
                        weather['location'],
                        weather['temperature_c'],
                        weather['temperature_f'],
                        weather['feels_like_c'],
                        weather['feels_like_f'],
                        weather['description'],
                        weather['humidity'],
                        weather['wind_speed_kmh'],
                        weather['wind_direction'],
                        weather['visibility'],
                        weather['pressure'],
                        weather['cloud_cover'],
                        weather['timestamp']
                    ])
            
            print(f"💾 Weather data exported to CSV: {filepath}")
            return str(filepath)
            
        except Exception as e:
            print(f"❌ Error exporting weather to CSV: {e}")
            return None
    
    def create_summary_report(self, weather_data, quotes_data):
        """
        Create a comprehensive summary report
        """
        try:
            report_content = f"""
# Web Scraping Summary Report
Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Weather Data Summary
- **Total locations**: {len(weather_data) if weather_data else 0}
- **Data source**: wttr.in
- **Average temperature**: {sum(w['temperature_c'] for w in weather_data.values()) / len(weather_data) if weather_data else 0:.1f}°C

### Weather by Location:
"""
            
            if weather_data:
                for location, data in weather_data.items():
                    report_content += f"- **{location}**: {data['temperature_c']}°C, {data['description']}\n"
            
            report_content += f"""

## Quotes Data Summary
- **Total quotes**: {len(quotes_data) if quotes_data else 0}
- **Data source**: quotes.toscrape.com
- **Average words per quote**: {sum(q['word_count'] for q in quotes_data) / len(quotes_data) if quotes_data else 0:.1f}

### Top 5 Authors:
"""
            
            if quotes_data:
                author_counts = {}
                for quote in quotes_data:
                    author = quote['author']
                    author_counts[author] = author_counts.get(author, 0) + 1
                
                top_authors = sorted(author_counts.items(), key=lambda x: x[1], reverse=True)[:5]
                for author, count in top_authors:
                    report_content += f"- **{author}**: {count} quotes\n"
            
            # Save report
            report_path = self.output_dir / "scraping_summary_report.md"
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
            
            print(f"📊 Summary report created: {report_path}")
            return str(report_path)
            
        except Exception as e:
            print(f"❌ Error creating summary report: {e}")
            return None


def main():
    """
    Main function demonstrating the multi-source information aggregator
    """
    print("🌐" * 20)
    print("    MULTI-SOURCE INFORMATION AGGREGATOR")
    print("🌐" * 20)
    print("Ethical web scraping demonstration with multiple data sources")
    print()
    
    # Initialize components
    weather_scraper = WeatherScraper()
    quote_scraper = QuoteScraper()
    exporter = DataExporter()
    
    while True:
        print("\n" + "=" * 50)
        print("🛠️ WEB SCRAPING MENU")
        print("=" * 50)
        print("1. Scrape weather data")
        print("2. Scrape quotes")
        print("3. Export data (JSON/CSV)")
        print("4. Generate summary report")
        print("5. Search scraped quotes")
        print("6. View weather reports")
        print("7. Analyze quotes data")
        print("8. Demo - scrape everything")
        print("9. Exit")
        
        try:
            choice = input("\nSelect option (1-9): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 Happy scraping! Remember to always scrape ethically!")
            break
        
        if choice == "1":
            # Scrape weather data
            print("\n🌤️ Weather Data Scraping")
            print("-" * 30)
            
            cities_input = input("Enter cities (comma-separated, e.g., London,Tokyo,NewYork): ").strip()
            if cities_input:
                cities = [city.strip() for city in cities_input.split(',')]
                weather_data = weather_scraper.get_multiple_locations(cities)
                
                if weather_data:
                    print(f"\n✅ Successfully scraped weather for {len(weather_data)} cities")
                    for city in weather_data:
                        print(f"   📍 {city}: {weather_data[city]['temperature_c']}°C")
                else:
                    print("❌ No weather data collected")
            else:
                print("❌ Please enter at least one city")
        
        elif choice == "2":
            # Scrape quotes
            print("\n📖 Quotes Scraping")
            print("-" * 20)
            print("🚀 Starting to scrape quotes from quotes.toscrape.com...")
            print("   (This site is designed for scraping practice)")
            
            quotes = quote_scraper.scrape_all_quotes()
            
            if quotes:
                print(f"\n✅ Successfully scraped {len(quotes)} quotes")
                
                # Show sample quotes
                print(f"\n📝 Sample quotes:")
                for i, quote in enumerate(quotes[:3], 1):
                    print(f"\n{i}. \"{quote['text'][:100]}{'...' if len(quote['text']) > 100 else ''}\"")
                    print(f"   — {quote['author']} ({', '.join(quote['tags'][:3])})")
            else:
                print("❌ No quotes scraped")
        
        elif choice == "3":
            # Export data
            print("\n💾 Data Export")
            print("-" * 15)
            
            # Check what data is available
            has_weather = bool(weather_scraper.weather_data)
            has_quotes = bool(quote_scraper.quotes_data)
            
            if not has_weather and not has_quotes:
                print("❌ No data to export. Please scrape some data first.")
                continue
            
            print("Available data to export:")
            if has_weather:
                print(f"   🌤️ Weather data: {len(weather_scraper.weather_data)} locations")
            if has_quotes:
                print(f"   📖 Quotes data: {len(quote_scraper.quotes_data)} quotes")
            
            print("\nExport options:")
            print("1. Export all to JSON")
            print("2. Export weather to CSV")
            print("3. Export quotes to CSV")
            print("4. Export everything")
            
            export_choice = input("Choose export option (1-4): ").strip()
            
            if export_choice == "1":
                if has_weather:
                    weather_dict = {w['location']: w for w in weather_scraper.weather_data}
                    exporter.export_to_json(weather_dict, "weather_data")
                if has_quotes:
                    exporter.export_to_json(quote_scraper.quotes_data, "quotes_data")
            
            elif export_choice == "2" and has_weather:
                weather_dict = {w['location']: w for w in weather_scraper.weather_data}
                exporter.export_weather_to_csv(weather_dict, "weather_data")
            
            elif export_choice == "3" and has_quotes:
                exporter.export_quotes_to_csv(quote_scraper.quotes_data, "quotes_data")
            
            elif export_choice == "4":
                # Export everything
                if has_weather:
                    weather_dict = {w['location']: w for w in weather_scraper.weather_data}
                    exporter.export_to_json(weather_dict, "weather_data")
                    exporter.export_weather_to_csv(weather_dict, "weather_data")
                if has_quotes:
                    exporter.export_to_json(quote_scraper.quotes_data, "quotes_data")
                    exporter.export_quotes_to_csv(quote_scraper.quotes_data, "quotes_data")
        
        elif choice == "4":
            # Generate summary report
            print("\n📊 Generating Summary Report")
            print("-" * 30)
            
            weather_dict = {w['location']: w for w in weather_scraper.weather_data} if weather_scraper.weather_data else {}
            report_path = exporter.create_summary_report(weather_dict, quote_scraper.quotes_data)
            
            if report_path:
                print("✅ Summary report generated successfully!")
        
        elif choice == "5":
            # Search quotes
            if not quote_scraper.quotes_data:
                print("❌ No quotes data available. Please scrape quotes first.")
                continue
            
            print("\n🔍 Search Quotes")
            print("-" * 15)
            
            search_term = input("Enter search term: ").strip()
            if search_term:
                matches = quote_scraper.search_quotes(search_term)
                
                print(f"\n📖 Found {len(matches)} quotes matching '{search_term}':")
                
                for i, quote in enumerate(matches[:5], 1):  # Show first 5
                    print(f"\n{i}. \"{quote['text']}\"")
                    print(f"   — {quote['author']} (Tags: {', '.join(quote['tags'])})")
                
                if len(matches) > 5:
                    print(f"\n... and {len(matches) - 5} more matches")
        
        elif choice == "6":
            # View weather reports
            if not weather_scraper.weather_data:
                print("❌ No weather data available. Please scrape weather data first.")
                continue
            
            print("\n🌤️ Weather Reports")
            print("-" * 20)
            
            for weather in weather_scraper.weather_data:
                print(weather_scraper.format_weather_report(weather))
                print("-" * 50)
        
        elif choice == "7":
            # Analyze quotes
            if not quote_scraper.quotes_data:
                print("❌ No quotes data available. Please scrape quotes first.")
                continue
            
            analysis = quote_scraper.analyze_quotes()
            print(analysis)
        
        elif choice == "8":
            # Demo - scrape everything
            print("\n🎯 COMPREHENSIVE SCRAPING DEMO")
            print("-" * 35)
            
            # Scrape weather for major cities
            major_cities = ["London", "NewYork", "Tokyo", "Sydney", "Berlin"]
            print(f"🌍 Scraping weather for major cities: {', '.join(major_cities)}")
            
            weather_data = weather_scraper.get_multiple_locations(major_cities)
            
            # Scrape quotes
            print(f"\n📚 Scraping inspirational quotes...")
            quotes = quote_scraper.scrape_all_quotes()
            
            # Generate reports and exports
            if weather_data or quotes:
                print(f"\n📊 Generating exports and reports...")
                
                # Export everything
                if weather_data:
                    exporter.export_to_json(weather_data, "demo_weather_data")
                    exporter.export_weather_to_csv(weather_data, "demo_weather_data")
                
                if quotes:
                    exporter.export_to_json(quotes, "demo_quotes_data")
                    exporter.export_quotes_to_csv(quotes, "demo_quotes_data")
                
                # Create summary report
                exporter.create_summary_report(weather_data, quotes)
                
                print(f"\n🎉 Demo complete!")
                print(f"   🌤️ Weather data: {len(weather_data)} cities")
                print(f"   📖 Quotes: {len(quotes)} quotes")
                print(f"   📁 All data saved to 'scraped_data' directory")
            else:
                print("❌ Demo failed - no data collected")
        
        elif choice == "9":
            print("\n🎉 Thank you for using the Multi-Source Information Aggregator!")
            print("🌟 Remember the golden rules of web scraping:")
            print("   • Always check robots.txt")
            print("   • Respect rate limits")
            print("   • Don't overload servers")
            print("   • Use APIs when available")
            print("   • Scrape ethically and legally")
            break
        
        else:
            print("❌ Invalid option. Please select 1-9.")


if __name__ == "__main__":
    main()