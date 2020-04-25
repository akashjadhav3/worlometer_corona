import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from worldometer.spiders.countries import CountriesSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(CountriesSpider)
process.start()




# add  this launch.json file in vs code
# // scrapy debugger
#         {
#             "name": "Crawl with scrapy",
#             "type": "python",
#             "request": "launch",
#             "module": "scrapy",
#             "cwd": "${fileDirname}",
#             "args": [
#                 "crawl",
#                 "countries"
#             ],
#             "console": "internalConsole"
#         }
