# AlwaysSunny-NLP
practicing NLP stuff with always sunny transcripts


*Discontinued this project.* SpringfieldSpringfield has no labels for who is speaking, and ForeverDreaming's are very sparse. 
Features of the final version pushed: 
* successfully generates a randomized transcript using 2-grams, randomly assigns speakers without regard to who is most likely to actually say it.
* succcessfully scrapes every episode from SpringfieldSpringfield, parses them cleanly into a single text file with only words, newlines, and punctuation.
* random scraps of code I didn't finish for scraping and parsing ForeverDreaming.

In the process of looking more closely at ForeverDreaming, I realized there wasn't a viable transcript for the things I wanted to do.
Please see the spiritual successor to this project, FB-NLP, generating randomized quotes for every member of a facebook messenger chat/groupchat.
Improvements of that version over this repo:
* Divides quotes by person with a separate markov chain for every participant
* Supports n-grams of any n
* Much faster parsing into n-grams
* More NLP shenanigans to come.
