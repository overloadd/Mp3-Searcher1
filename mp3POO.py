#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      overloadfull
#
# Created:     30/06/2014
# Copyright:   (c) overloadfull 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import urllib,urllib2
import os



class Busqueda:
    def __init__(self, busq):
        self.busq = busq
        self.busq.replace(" ","_")
        try:
         self.openn = urllib2.urlopen("http://www.mp3skull.com/mp3/"+busq+".html")
        except ValueError,a:
         print a.reason
        print busq
        self.reaad = self.openn.read()

    def search(self, dep):

        if dep >= 1:
         lista = []
         try:
          var = 0

          for i in str(self.reaad): #I read all the characters from the downloaded page
           for i2 in range(dep): #dep is the number of links the user wants to see
            a1 = self.reaad.find('<div style="float:left;"><a href="',var)#locates the link
            a2 = self.reaad.find('http://',a1)#Marks the start of the link
            a3 = self.reaad.find('.mp3" ',a2)
            a4 = self.reaad[a2:a3+4].replace(" ","_")
            var = var+ a3
            lista.append(a4)
            if i2 >= dep:
                break
           if len(lista) == dep:
            break

          self.openn.close()
          return lista
         except ValueError:
          print "Not found, search another way"
          exit
    def download(self, url):
     busqmod = self.busq
     try:
      busq2 = urllib2.Request(url)
      baj = urllib2.urlopen(busq2)
      datos = baj.read()
      mp3nombre = busqmod+".mp3"
      cancion = open(mp3nombre, "wb")
      cancion.write(datos)
      cancion.close()
     except urllib2.HTTPError, e:
        print "Broken link", e
        main()



def main():
  print """
When trying to search try this format: song name + first artist's name
For example: wide awake katy  . Instead of : wide awake katy perry or katy perry
                                                                      wide awake
It's a problem of the page page not mine
Enjoy :D



  """
  busq = raw_input("Search>> ")
  results = input("How many results do you want to show>> ?")
  b = Busqueda(busq)
  res = b.search(results)
  for canc in range(results):
    print res[canc]+' ------> '+ str(canc)
  for canc2 in range(results):
    res[canc] = str(canc)+'a'
  option(res,b)


def option(res,b):
  opt1 = input("Choose an option>> ")
  try:
   b.download(res[opt1])
   print "The song is located in: "+ os.getcwd() #REMEMBER: add the option for changing the download folder
   print "Check that the actual version of the song is the one you wanted before answering if you want another version."
   opt2 = raw_input("Do you want another version?(y/n)>> ")
   if opt2 == "y":
          option(res,b)
   elif opt2 =="n":
    exxit()
   else:
         print "Type a valid option"
         option(res,b)
  except:
    print "Broken link"
    option(res,b)



def exxit():
    opt3 = raw_input("Exit?(y/n)>> ")
    if opt3 == "y":
            exit()

    elif opt3 == "n":
            main()
    else:
            print "Type a valid option"
            exxit()





main()
