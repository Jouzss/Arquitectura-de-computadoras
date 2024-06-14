import asyncio
import httpx

urls = ["https://www.amazon.com", "https://www.google.com", "https://www.openai.com",
    "https://www.wikipedia.com", "https://www.python.org", "https://www.nvidia.com/en-us/",
    "https://www.microsoft.com/en-us/"]

async def async_fetch(url: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.text 

def sync_fetch(url:str) -> str:
    with httpx.Client() as client:
        response = client.get(url)
    return response.text

def sync_scraper(urls: list[str])-> list[str]:
    html_contents = []
    for url in urls:
        content = sync_fetch(url)
        html_contents.append(content)
    return html_contents

async def async_scraper(urls: list[str])-> list[str]:
    html_contents = []
    content = [async_fetch(url) for url in urls] #Crea una lista 
    html_contents = await asyncio.gather(*content)
    return html_contents

if __name__=="__main__":
    # Version sincrona
    print(sync_fetch(urls[0]))

    # Version asincrona
    print(asyncio.run(async_fetch(urls[0])))
    
    print(async_scraper(urls))
    #print("\n"*10)
    print(asyncio.run(sync_scraper(urls)))
    print(async_scraper(urls) == sync_scraper(urls))