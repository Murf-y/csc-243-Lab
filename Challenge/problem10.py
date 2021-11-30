"""Your grandma/grandpa is new to the internet, and there are some slang words 
that s/he does not
understand. Create a dictionary that contains the below slang words and 
create a program that will take
a slang from the user and give the explanation to this word."""

def main():
    slangs_to_words = {
        "BRB": "Be right Back",
        "DP": "Display Picture",
        "LMAO": "Laughing My A** Off",
        "LOL": "Laughing Out Loud",
        "OK": "Olla Kalla or Oll Korrect",
        "PFA":"Please Find Attachement, Predictive Failure Analusis",
        "ROFL": " Rolling on Floor laughing",
        "TBH": "To Be Honest",
        "TTYL": "Talk to you later",
        "ETA": "Estimated time of arrival",
        "FYI": "For Your Information"
    }
    slang = input("Enter a slang: ")
    print(slangs_to_words.get(slang.upper(), "Sorry, I don't know that slang"))

main()