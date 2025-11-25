import requests
from bs4 import BeautifulSoup
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("saturn-docs")

BASE_URL = "https://docs.rocketbot.com"

@mcp.tool()
def search_docs(query: str) -> str:
    """
    Search the Rocketbot Saturn documentation.
    
    Args:
        query: The search query string.
        
    Returns:
        A formatted string containing search results with titles and URLs.
    """
    search_url = f"{BASE_URL}/?s={query}"
    try:
        response = requests.get(search_url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # This selector might need adjustment based on actual WP theme
        # Usually search results are in <article> tags or specific classes
        results = []
        
        # Look for articles in the search results
        articles = soup.find_all('article')
        
        if not articles:
            return "No results found."
            
        for article in articles:
            # Try different selectors for title
            title_tag = article.find('h2', class_='entry-title')
            if not title_tag:
                title_tag = article.find('h1', class_='entry-title')
            if not title_tag:
                title_tag = article.find('p', class_='title')
                
            if title_tag and title_tag.find('a'):
                link = title_tag.find('a')['href']
                title = title_tag.get_text(strip=True)
                
                # Try different selectors for excerpt
                excerpt_tag = article.find('div', class_='entry-summary')
                if not excerpt_tag:
                    excerpt_tag = article.find('div', class_='content')
                
                excerpt = excerpt_tag.get_text(strip=True) if excerpt_tag else "No excerpt available."
                
                results.append(f"### [{title}]({link})\n{excerpt}\n")
                
        return "\n".join(results) if results else "No results found."

    except Exception as e:
        return f"Error searching docs: {str(e)}"

@mcp.tool()
def read_doc(url: str) -> str:
    """
    Read a specific documentation page from Rocketbot docs.
    
    Args:
        url: The full URL of the documentation page.
        
    Returns:
        The content of the page in Markdown format (approximated).
    """
    if not url.startswith(BASE_URL):
        return f"Error: URL must start with {BASE_URL}"
        
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Main content usually in entry-content
        content_div = soup.find('div', class_='entry-content')
        
        if not content_div:
            return "Could not find content on this page."
            
        # Simple HTML to Markdown conversion
        # For a more robust solution, we could use markdownify, but let's keep it simple for now
        # or just return text. Let's try to preserve some structure.
        
        markdown_lines = []
        
        for element in content_div.descendants:
            if element.name == 'h1':
                markdown_lines.append(f"\n# {element.get_text(strip=True)}\n")
            elif element.name == 'h2':
                markdown_lines.append(f"\n## {element.get_text(strip=True)}\n")
            elif element.name == 'h3':
                markdown_lines.append(f"\n### {element.get_text(strip=True)}\n")
            elif element.name == 'p':
                text = element.get_text(strip=True)
                if text:
                    markdown_lines.append(f"\n{text}\n")
            elif element.name == 'li':
                markdown_lines.append(f"- {element.get_text(strip=True)}")
            elif element.name == 'pre':
                code = element.get_text()
                markdown_lines.append(f"\n```\n{code}\n```\n")
                
        # Fallback if manual parsing is too messy, just get text
        if not markdown_lines:
             return content_div.get_text(separator='\n\n', strip=True)

        return "".join(markdown_lines)

    except Exception as e:
        return f"Error reading doc: {str(e)}"

if __name__ == "__main__":
    mcp.run()
