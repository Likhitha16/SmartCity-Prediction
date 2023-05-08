# cs5293sp23-project3
Template repo for Project 3

`smartcity/`  - contains the pdf applications \
`project3.ipynb` - template notebook to follow for Project3

Please change this README.md as needed.
# Smart City Slicker

#### Project is implemented using python and Jupyter notebook and it can be run using the following command.
#### pipenv run python project3.py --document city.pdf 
## Different kinds of Packages used are:
### os
### pyPDF2
### nltk
### Spacy
### pandas
### re
### nltk.corpus
# Fuctions and features used are
## readPdf()
#### This function takes different kinds of documents and reads the data and puts all the data into a datastructure called lists. It stores the data from all the pdfs into a list.
## cityandrawtext()
#### This function extracts citynames from the filenames and adds them to the list, it also extracts the rawtext and adds the rawtext from each of the files and then puts them combined into a list

#### I have used contractions.py file which was provided from one of the lectures and textnormalisation.py file which also provided through git hub and tried to normalise the city names and the raw text from the documents and did the data cleaning based on that.

## Bugs and Assumptions
### Bugs 
#### Multiple city mentions: The raw text may mention multiple cities, and it may not always be clear which city name should be extracted.
#### Text formatting: The raw text may be formatted in different ways (e.g., all caps, mixed case), which could impact the accuracy of city name extraction.
### Assumptions
#### Prevalence of city mentions: Assuming that city names are mentioned frequently enough in the raw text to make their extraction worthwhile.
#### Language processing accuracy: Assuming that the language processing technology used to extract city names is accurate and robust enough to handle variations in text formatting and language usage.
#### Overall, it's important to carefully consider potential bugs and assumptions when extracting city names from raw text in a smart city project to ensure that the extracted data is accurate and useful for decision-making. It may also be necessary to test and refine the extraction process to ensure accuracy and to minimize errors.

#Test-Functions
## test_smartcity.py
### test_read()
#### This function tests if the files are read correctly from the readfile method which uses PyPdf package.
### test_cityraw()
#### This function tests if the citynames and rawtext are extracted properly and also if the preprocessing is done correctly or not.

#### These are the important test_functions that we have used in the testfiles.

