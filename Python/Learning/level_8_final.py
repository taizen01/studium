import os

os.system("cls")

chat_logs = [
    "My order is delayed wrong driver", 
    "I want to return my purchase", 
    "The app is crashing frequently", 
    "Payment failed wrong", 
    "Need help with account delayed recovery", 
    "Delivery was incomplete", 
    "Can't login to my login", 
    "Having trouble with checkout account",
    "Could't find a driver",
    "Help me with my Order payment"
]

keywords = {
    "Order": ["delayed", "items", "wrong", "return"], 
    "App": ["app", "crashing"],
    "Payment": ["failed", "Payment", "checkout"],
    "Account": ["recovery", "account", "login"],
    "Delivery": ["delivery", "driver"],
    }

categories = {"Order": 0, "App": 0, "Payment":0, "Account":0, "Delivery":0}


def categorize_issues(n,k):
    for i in (range(len(n))):
        categorized = False  # Flag zum Stoppen der weiteren Prüfung
        for key, words in k.items():
            if categorized:  # Wenn schon zugeordnet, keine weitere Prüfung, wird bei der ersten Prüfung nicht beachtet.
                break
            for j in range(len(words)):
                if words[j].upper() in n[i].upper():
                    categories[key]+=1
                    categorized = True # Wenn ein passendes Wort gefunden aus Satz, gehe zum nächsten
                    break
    print("\nIssue Categories: ")
    for key, value in categories.items():
        print(f'{key}: {value}\n')





def keyword_search(n, l):
        newlist = [x for x in l if n.upper() in x.upper()]
        print("Chat logs containing the keyword: ")

        for i in newlist:
             print(f'-> {i}')


                
                  

eingabe = input("Enter a keyword to search in chat logs: ")

categorize_issues(chat_logs,keywords)   
keyword_search(eingabe, chat_logs)