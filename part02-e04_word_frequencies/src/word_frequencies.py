#!/usr/bin/env python3

def word_frequencies(filename):
    aliceDict = {}

    with open(filename) as f:
        for word in f.read().split():
            wordStrip = word.strip("""!"#$%&'()*,-./:;?@[]_""")
            if wordStrip not in aliceDict:
                aliceDict[wordStrip] = 0
            aliceDict[wordStrip] += 1     

    return dict(sorted(aliceDict.items(), key=lambda item: item[1]))

def main():
    alice = word_frequencies("src/alice.txt")
    
    for word, count in alice.items():
        print(f"{word}\t{count}")
    

if __name__ == "__main__":
    main()
