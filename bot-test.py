import subprocess

strWebURL = "http://colors.corp.local/"

while True: 
  print("********************\n\n")
  print("1)  Bot Signature Test:")
  print("2)  Bot Black List Test:")
  print("3)  Bot White List Test:")
  print("4)  Bot Rate Limit Test:")
  print("5)  Bot Device Fingerprint Test:")
  print("x)  Exit Bot Test  \n\n")
  selection=input("Please Select:") 
  if selection =='1': 
    print ("\nTesting Bot Management ....... \nUsing Signature to block User Agent detected of \"a.pr-cy.ru\" :\n")
    mytext = subprocess.call(["curl",
      "-H",
      "User-Agent: a.pr-cy.ru",
      "-H",
      "Demo: mycitrixdemo.net",
      strWebURL,
      "-m 2"
      ], shell=False)
    print (mytext)
  elif selection == '2':
    print ("\nTesting Bot Management using black list of url \"test.php\" :\n")
    mytext = subprocess.call(["curl", 
      "-H",
      "Demo: mycitrixdemo.net", 
      strWebURL + "test.php/",
      "-m 2"
      ], shell=False)
    print (mytext)
  elif selection == '3': 
    print ("\nTesting Bot Management using white list of url \"white.html\" :\n")
    mytext = subprocess.call(["curl", 
      "-H",
      "Demo: mycitrixdemo.net", 
       strWebURL + "white.html/",
      "-m 2"
      ], shell=False)
    print (mytext)
  elif selection == '4': 
    print ("\nTesting Bot Management using rate limiting :\n")
    mytext = subprocess.call(["curl", 
      "-H",
      "Demo: mycitrixdemo.net", 
      strWebURL + "login_rl.html/",
      "-m 2"
      ], shell=False)
    print (mytext)
  elif selection == '5': 
    print ("\nTesting Bot Management using fingerprinting :\n")
    mytext = subprocess.call(["curl", 
      "-H",
      "Demo: mycitrixdemo.net", 
      strWebURL + "abc/",
      "-m 2"
      ], shell=False)
    print (mytext)
  elif selection == 'x' or selection == 'q' or selection == 'X' or selection == 'Q': 
    break
  else: 
    print ("\n\n\n*************************\nUnknown Option Selected!\n*************************\n\n\n")



  
