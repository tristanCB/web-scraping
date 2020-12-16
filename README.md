# Web Scraping
Automation of data collection can make a project efficient and repeatable. Web scrapers are programs which extract information from web pages (which are encoded in HTML). Web crawling is a type of scraping which involves iterating the scraping process over a multitude of URLs (DeVito et. al., 2020). Web data scraping is generally defined as the systematic process of extracting and combining contents of interest from the Web (Glez-Peña D., 2014).

The basic methods of web scraping have been in use for a considerable amount of time. They are the basis of search engines. "The amount of information on the Web is finite, but the number of pages is infinite" (Baeza-Yates, 2005). Scraping quality data is an inherently subjective matter. Nevertheless, work on the objective relative importance of Web pages led to the development of the PageRank algorithm (Brin S. & Page L., 1998): the first algorithm that google used (Patent [US6285999B1](https://patents.google.com/patent/US6285999B1/en); which has reached it's expiry date).

Prior to starting your project you should consider if the data can be obtained in a easier way such as using an API (application programming interface) or downloading the data directly (if the website makes it available). When web scraping is still the best approach ensure that the website can be scraped. In some instances more advanced techniques are required to access the desired data such as cases where the targeted data is displayed as CSS image sprites or as an image (JonasCz, 2020).

Robots exclusion standard (often simply called robots.txt) is a standard used by websites to communicate with robots (https://www.robotstxt.org/). In theory, owners can disallow  non user agents from visiting their website. In practice, it is the program's choice wether it implements the standard or not (it is a non binding contract). For the United States, the Computer Fraud and Abuse Act (CFAA) makes unlawful certain computer-related activities involving unauthorized access of protected computers (mainly governmental computers or ones used by financial institutions). When it boils down, the legality of scraping involves two issues: Ownership of content and denial of service. Digital media such as videos, music, books, images and scientific articles are of obvious concern if the content is used to benefit your or other's gains. If you are considering scraping data that may be copyright protected, ensure that you have a license or permission and that you follow your granted rights or that you comply with the Fair Use doctrine. The other concern (denial of service type; "the most important self imposed restriction" (Baeza-Yates, 2005)) may arise when the automation of the process causes other legitimate users to access the content. The entity hosting the website may incur increased bandwidth or electrical costs for running the servers. Web scraping is associated with severals often determined by numerous factual variable such as the nature of the data being scraped, the technical methods used to scrape, and the applicability of the contractual terms (iCrowdNewswire LLC, 2020). Several prominent cases regarding digital property and copyright law specifically related to web scraping which have shaped the it's legal landscape are: [eBay vs. Bidder's Edge](https://en.wikipedia.org/wiki/EBay_v._Bidder%27s_Edge), [Ticket-master Corp., et al. vs. Tickets.com](https://en.wikipedia.org/wiki/Ticketmaster_Corp._v._Tickets.com,_Inc.), legal threats issued against Edward Felten by SDMI([*](https://en.wikipedia.org/wiki/Edward_Felten)), and the criminal charges faced by weev regarding an AT&T data breach ([*](https://en.wikipedia.org/wiki/Weev)). To minimize the negative exposure related to web scraping, common web scraping practices have been included in Table 2.

It is only more recently that some scientific communities have turned to it for hypothesis testing. With regards to psychology, Richard N. Landers (2017) proposed certain guidelines for conducting relevant research using data obtained from web scraping. These guidelines mainly revolve around a theory driven approach (considering research questions a-priori) as supposed to being influenced by the techniques more commonly employed by web-scrapers such as data-mining and exploratory data analysis (including the use of machine learning). Care is to be taken when correlational techniques are used on larger datasets. The sample size employed will result in loss of value and meaning, especially being the case when when null hypothesis significance testing is being employed (Landers R.N., et. al., 2017).

## Types of Web Scrapers and Common Practices

| Type | Characteristic | Description | 
|---|---|---|
| spiders or copiers | recursively follows links | Ex: [Googlebot](https://developers.google.com/search/docs/advanced/crawling/googlebot?visit_id=637436563101153153-1272068882&rd=1), [HTTrack](http://www.httrack.com/)
| Shell Scripts | Uses common unix tools | Combination use of [Curl](https://curl.se/) to download a page and [Grep](http://www.gnu.org/software/grep/) to extract the data |
| HTML parsers | Parsing based on HTML | Ex: [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [scrapy](scrapy.org), [Colly](http://go-colly.org/) |
| Screenscrapers | Use browser to render the page | [Selenium](https://www.selenium.dev/), [PhantomJS](https://phantomjs.org/). Can also involve the use of Optical Character Recognition (OCR, ex: [pytesseract](https://github.com/madmaze/pytesseract))|

**Table 1: Types of web scrapers**

<br/><br/>

| Method  | Details |
|---|---|
| Respecting what the site wants you to scrape | Follow the standard in the robot.txt file |
| Crawling with delays | Will minimize the chance you negatively impact a server's performance, and prevent your IP from being flagged/blocked. Anecdotal evidence from web crawlers of known search engines vary from ~ 20 seconds to 3-4 minutes (Baeza-Yates, 2005) |
| Limiting concurrent requests per domain | Concurrent requests can be flagged as suspicious activity. Alternatively one can use auto throttling to adapt to a website's ability to handle requests. |
| Using identifiable user agents | Adding contact information in the User-Agent header of the requests will provide a convenient way for site admins to contact you. If your IP is flagged, this might prevent you from being automatically blocked. |
| Using an HTTP cache for development | Designing a web scraper is often an iterative process. Using cached webpages for development will prevent you from having to resend a same request multiple times. |

**Table 2: Minimizing exposure**

### Web Scraping Using Python
The following instructions are used to configure your environment for running the scraping examples included in [webscpr.py](./webscpr.py)

#### Setting up the Environment
Install Miniconda from https://docs.conda.io/en/latest/miniconda.html
Launch the anaconda prompt.
Create and activate an environment (execute following command in anaconda prompt):

```conda create --name myEnv python=3.8```

```conda activate myEnv```

Install required python packages into the newly created environment:

```conda install scrapy```

```conda install -c anaconda beautifulsoup4```

```conda install -c anaconda urllib3```

```conda install -c conda-forge selenium```

...

Download and include required drivers in the drivers folder of this project:
1. https://phantomjs.org/
1. https://github.com/mozilla/geckodriver/releases

Download firefox: https://www.mozilla.org/en-CA/firefox/new/
*alternatively chrome (with the Chrome webdriver) can be used.

### Setting up a Proxy Service
Most efforts to stop scraping involve the website detecting the difference between a human and a bot. Nevertheless, blocking an IP address or group thereof is an extremely common method for server admins to stop the process (Mitchell, 2015). The following will address various ways of overcoming this limitation.

Tor is a free and open-source software which can be used as a free proxy. It is a network of volunteer servers set up to route and re-route traffic through many layers. To use Tor as a proxy in your Python script ensure to have it installed and running on your machine. And that your proxy is appropriately configured (refer to Section Using selenium, TOR (as a proxy), and firefox for web scraping in [webscpr.py](./webscpr.py)). For an easy connection interface with a proxy one can use PySocks (https://pypi.org/project/PySocks/). 

### Building a web crawler
In 2004, it was estimated that crawling all of the contents indexed by google carried a price tag of approximately 4 million dollars(Craswell, 2004). It is nor practical or realistic to hope for a crawler to completely download a finite data set due to limitations imposed by network bandwidth, disk space, the time dependent nature of the web and the fact that an infinite number of pages can exist (dynamic pages). Ricardo Baeza-Yates (2005) investigated various page ordering strategies with an without the use of historical information. Of the ones considered without the use of historical data (Breadth-first, Backlink-count, Batch-pagerank, Partial-pagerank, OPIC, Larger-sites-first), the "larger-sites-first" approached seemed to perform and scale well. The OPIC methods implemented in Python [(*)](https://crawl-frontier.readthedocs.io/en/opic/topics/opic-precision.html) should be considered.

## Ideas
1. ML Focused crawler: https://en.wikipedia.org/wiki/Focused_crawler.
1. Using mouse recorder to gather data on human link crawling behavior. The formatting of the data could be considered for further investigation for the development of human like web crawling programs.
1. AWS lambda scraper. Scrapping as a web micro-service.
1. Graph neural networks to visualize the www?

## Useful content
1. The [code repo](https://github.com/PacktPublishing/Python-Web Scraping-Second-Edition) for __Python Web Scraping - Second Edition__ (Jarmul, 2017). - Useful examples which some are included in scraperexamples.py
1. A [stack overflow question](https://stackoverflow.com/questions/3161548/how-do-i-prevent-site-scraping/34828465#34828465) on how to prevent web scraping - A useful post explaining common methods site admins use to prevent web scraping.
1. https://docs.conda.io/en/latest/miniconda.html - My preferred python package manager.
1. https://docs.anaconda.com/anaconda/user-guide/cheatsheet/ - Useful conda commands.
1. https://visualstudio.microsoft.com/visual-cpp-build-tools/ - requirement if scrapy is going to be used
1. https://devhints.io/xpath - Xpath cheat sheet.


## References
Baeza-Yates, Ricardo et. al. __Crawling a Country: Better Strategies than Breadth-First for Web Page Ordering.__ 14th International World Wide Web Conference, 2005.

Craswell, N., et. al. __Performance and cost tradeoffs in web search.__ Proceedings of the 15th Australasian
Database Conference, 2004.

DeVito, Nicholas J, et al. __“How We Learnt to Stop Worrying and Love Web Scraping.”__ Nature : International Weekly Journal of Science, vol. 585, no. 7826, 2020, pp. 621–622., doi:10.1038/d41586-020-02558-0.

Glez-Peña D., et al. __Web Scraping Technologies in an Api World.__ Briefings in Bioinformatics, vol. 15, no. 5, 2014, pp. 788–97., doi:10.1093/bib/bbt026.

Heydt, Michael. __Python Web Scraping Cookbook : Over 90 Proven Recipes to Get You Scraping with Python, Microservices, Docker, and Aws.__ Packt Publishing, 2018.

iCrowdNewswire LLC. __Web Scraper Software Market to See Booming Growth | Diggernaut, Phantom Buster, Mozenda.__ November 26, 2020. Retrieved from: Down Jones Factivia december 15, 2020.

Jarmul, Katharine, and Richard Lawson. __Python Web Scraping : Fetching Data from the Web. Second edition.__, Packt Publishing, 2017.

JonasCz. __A guide to preventing Webscraping.__ Github, 2018. Retrieved from: https://github.com/JonasCz/How-To-Prevent-Scraping on December 15, 2020.

Landers R.N., et al. __A Primer on Theory-Driven Web Scraping: Automatic Extraction of Big Data from the Internet for Use in Psychological Research.__ Psychological Methods, vol. 21, no. 4, 2016, pp. 475–492.

Mitchell, Ryan. __Web Scraping with Python : Collecting Data from the Modern Web. First edition.__ O'Reilly Media, 2015.

Brin, Sergey and Page, Larry. __The PageRank Citation Ranking: Bringing Order to the Web.__ http://google.stanford.edu, 1998. 