from crpapi import CRP

import sys

import random

import environment
import politicians as pol

#SET YOUR OPEN POLITICS API KEY IN ENVIRONMENT.PY
crp = CRP(environment.API_KEY)


def createCand():
    global id
    global cand
    global contribs
    global candName
    global candParty
    id = random.choice(pol.pol)
    try:
        cand = crp.candidates.get(id)
    except:
        print(f"Error: {id}")
    contribs = crp.candidates.contrib(id)
    candName = cand['@attributes']['firstlast']
    candParty = cand['@attributes']['party']
    if candParty == "D":
        candParty = "Democrat"
    else:
        candParty = "Republican"

def game():
    print(f"The politician's top donor is {contribs[0]['@attributes']['org_name']} and they gave {contribs[0]['@attributes']['total']} dollars")
    print("Democrat or Republican? (end game with 'end')")
    answer = input()
    
    if answer == candParty:
        print(f"Yes! {candName} is a {candParty}")
    elif answer != candParty:
        if answer == "end":
            sys.exit()
        print(f"No! {candName} is a {candParty}!")


while True:

    createCand()
    game()