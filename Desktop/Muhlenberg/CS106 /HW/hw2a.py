def pickAndShow():
  file = pickAFile()
  file2 = pickAFile()
  pict = makePicture(file)
  pict2 = makePicture(file2)
  show(pict)
  show(pict2)

def printInvite():
  print "Come Celebrate Lucy's Birthday with us!"
  print "Sunday, November 2nd at 8PM" 
  print "222 Wonderland Ave, Lakeville, CT"

def printDisclaimer():
  print "Disclaimer: This invitation is not real!"
  print "At no point should anything written anywhere on this invitation be taken as factual or accurate"
  print "Please do not take anything seriously" 
  print "Also, we are not liable for anything that happens to you."
  
def printFullInvite():
  printInvite()
  printDisclaimer()
   
  