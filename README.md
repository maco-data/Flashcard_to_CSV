# Flash Cards to CSV Generator

### Description

This is a small script I came up in order to be able to convert the flash cards I found in **Quizlet.com** to a csv file for easy import into anki.

I'm not connected to the internet at all times so having my flashcards synced to my phone via the anki app is amazing. 

Unfortunately creating decks is not easy or fun task specially for decks with hundreds of cards or decks from different creators about the same topic.

Being able to create a deck via "import" is a big time saver. 

This script is a web-scraping scrip that uses:
+ Beautifulsoup 4.10.0
+ Requests 2.26.0
+ Pandas 1.3.4

I will take the deck from the website, scrape all the information from the front and back of the card and append it to a csv file for easy import into anki.

At the time I created this script I was on "python 3.10.0".

### Instructions

1. Answer the prompnt of how many links you will use (make sure to give a numerical value).

2. Paste the complete url of the deck i.e:
>https://quizlet.com/347387076/gcp-architect-certification-001-flash-cards/ 
If there is more than one link then add them one by one, you will be promted (I look forward to add a batch pasting option in a near future).

3. Be patient! Depending on your computer it may be a fast or slow process to collect the data from all the cards.

4. Name your file. After naming the csv file it will be created and as I previously mentioned, it may take some time for the same reasons as before plus the size of the csv file.

Done!

### Appreciation

At the moment of coming up with this Idea I was studying for my Google Cloud Platform certification, therefore I would like to thank these amazing people who took the time to create the decks and the article that took me too them:

Sam Lee [Medium Profile](https://medium.com/@samuel.lee753)

**Article** Free flash cards & practise exams for getting Google Cloud certified [Link](https://medium.com/@samuel.lee753/free-flash-cards-practise-exams-for-getting-google-cloud-certified-ec206c398b4a)

Bill Scott "WJScoot" [Quizlet Profile]("https://quizlet.com/WJScoot/sets")

"Charlie_Petitpas" [Quizlet Profile](https://quizlet.com/Charlie_Petitpas/sets)

"czesieks" [Quizlet Profile](https://quizlet.com/czesieks/sets)

"tzsteve" [Quizlet Profile](https://quizlet.com/tzsteve/sets)

"casey_o_kane" [Quizlet Profile](https://quizlet.com/casey_o_kane/sets)