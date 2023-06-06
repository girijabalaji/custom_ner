import spacy
nlp = spacy.load("output/model-last/") #load the model


job_post = """We are Looking for Python Developer who are willing to prove their skills and creativity.

The candidate should have:

- Knowledge of Python, Selenium, Scraping Modules, HTML, Web Services

- strong knowledge of Regular expression

- Familiarity with techniques and tools for crawling, extracting and processing data (e.g. Scrapy, NLTK, pandas, scikit-learn, NoSQL, etc)

- Familiarity with Machine Learning Algorithms (Supervised Learning)

- Experience in common data science toolkits

- Strong communication and analytical skills

- Excellent organization and prioritization skills

Responsibilities and Duties:-

- Developing highly reliable web crawlers and parsers across various websites

- Extracting structured/unstructured data and store them into SQL/No SQL database

- Processing, cleansing, and verifying the integrity of data scrapped

- Creating anomaly detection systems and constant tracking of its performance

- Python, Web scrapping, Machine Learning

Interested candidates #share the resume at jaya.mishra@sveltetech.com
"""

doc = nlp(job_post)

for ent in doc.ents:
    print(ent.text, ent.label_)