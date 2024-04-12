from langchain_community.tools.wikidata.tool import WikidataAPIWrapper, WikidataQueryRun
from langchain.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
print(wikipedia.run("Gainsville, Florida"))
wikidata = WikidataQueryRun(api_wrapper=WikidataAPIWrapper())
print(wikidata.run("Gainsville, Florida"))