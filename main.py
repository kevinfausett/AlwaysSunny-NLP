import requests
from bs4 import BeautifulSoup
import time
import pathlib
import re
from random import choice

def main():
    transcript = pathlib.Path("transcriptClean.txt").read_text()
    transcriptRecleaned = transcript.replace("DENNIS: ", "").replace("MAC: ", "").replace("DEE: ", "").replace("Frank: ", "").replace("Charlie: ", "").replace("ALISON: ", "")

    # Not appropriate for this task. It would split "didn't" into "did" and "n't" or "gonna"
    # into "gon" and "na" because it's tokenizing contractions separately, because they hold their own meaning.
    # This is good for analysis, bad for word generation.
    # transcriptWords = nltk.word_tokenize(transcript)

    # Instead we'll just split on one or more spaces
    words = re.split(' +', transcriptRecleaned)

    transitionTable = {}

    for i in range(2, len(words)):
        key = words[i-2], words[i-1]
        if key in transitionTable:
            transitionTable[key].append(words[i])
        else:
            transitionTable[key] = [words[i]]

    # dictionary.keys is an iterator now in Python 3. Rude
    start = choice(list(transitionTable.keys()))
    word1, word2 = start[0], start[1]
    word3 = choice(transitionTable[start])
    cast = ['MAC: ', 'DENNIS: ', 'DEE: ', 'FRANK: ', "CHARLIE: "]
    firstSpeaker = choice(cast)
    res = firstSpeaker
    res += (word1 + ' ' + word2 + ' ')
    current = firstSpeaker
    for i in range(0, 1000):
        res += word3 + ' '
        if "\n" in word3:
            speaker = choice(cast)
            if speaker != current:
                res += speaker
                current = speaker

        nextWord = choice(transitionTable[word2, word3])
        word2 = word3
        word3 = nextWord
    pathlib.Path("myscript.txt").write_text(res, encoding="utf8")
    print(res)



def scrapeForeverDreaming():
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,*',}
    page = requests.get("http://transcripts.foreverdreaming.org/viewtopic.php?f=104&t=30647&view=print", headers=headers, proxies={'http': '71.13.140.128:21776'})
    megaTranscript = ""
    megaDirtyTranscript = ""
    allepisodes = []
    for episode in allepisodes:
        page = requests.get(episode, headers)
        prettypage = BeautifulSoup(page.content, 'html.parser')
        transcript = prettypage.find_all(class_="scrolling-script-container")
        if transcript:
            transcriptDirty = transcript[0].get_text()
            transcriptClean = transcriptDirty.replace("\n", "").replace("\t", "").replace("\r", "").replace(" -", "\n")
            megaDirtyTranscript += transcriptDirty
            megaTranscript += transcriptClean
            print(episode)
            print(transcriptClean)
        time.sleep(3)
    pathlib.Path("transcriptClean.txt").write_text(megaTranscript, encoding="utf8")
    pathlib.Path("transcriptDirty.txt").write_text(megaDirtyTranscript, encoding="utf8")


def scrapeSpringfieldSpringfield():
    #Use a proxy for forever dreaming

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,*',}
    # page = requests.get("https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=its-always-sunny-in-philadelphia&episode=s02e01", headers)
    # prettypage = BeautifulSoup(page.content, 'html.parser')
    # transcriptDirty = prettypage.find_all(class_="scrolling-script-container")[0].get_text()
    # transcriptClean = transcriptDirty.replace("\n", "").replace("\t", "").replace("\r", "").replace(" -", "")
    # print(transcriptClean)
    headers = {'User-Agent': user_agent}


    s1to9e1to9 = ["https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=its-always-sunny-in-philadelphia&episode=s0" + str(season) + "e0" + str(episode) for season in range(1, 10) for episode in range(1, 10)]
    s1to9e10plus = ["https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=its-always-sunny-in-philadelphia&episode=s0" + str(season) + "e" + str(episode) for season in range(1, 10) for episode in range(10, 16)]
    s10to12e1to9 = ["https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=its-always-sunny-in-philadelphia&episode=s1" + str(season) + "e0" + str(episode) for season in range(0, 3) for episode in range(1, 10)]
    s10to12e10 = ["https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=its-always-sunny-in-philadelphia&episode=s1" + str(season) + "e10" for season in range(0, 3)]

    allepisodes = s1to9e1to9 + s1to9e10plus + s10to12e1to9 + s10to12e10

    megaTranscript = ""
    megaDirtyTranscript = ""
    for episode in allepisodes:
        page = requests.get(episode, headers)
        prettypage = BeautifulSoup(page.content, 'html.parser')
        transcript = prettypage.find_all(class_="scrolling-script-container")
        if transcript:
            transcriptDirty = transcript[0].get_text()
            transcriptClean = transcriptDirty.replace("\n", "").replace("\t", "").replace("\r", "").replace(" -", "\n")
            megaDirtyTranscript += transcriptDirty
            megaTranscript += transcriptClean
            print(episode)
            print(transcriptClean)
        time.sleep(3)
    pathlib.Path("transcriptClean.txt").write_text(megaTranscript, encoding="utf8")
    pathlib.Path("transcriptDirty.txt").write_text(megaDirtyTranscript, encoding="utf8")

main()