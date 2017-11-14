import urllib
import os,time

#this is the first part of the streetview, url up to the address, this url will return a 600x600px image
pre="https://maps.googleapis.com/maps/api/streetview?size=600x600&location="

#this is the second part of the streetview url, the text variable below, includes the path to a text file containing one address per line
#the addresses in this text file will complete the URL needed to return a streetview image and provide the filename of each streetview image

#this is the third part of the url, needed after the address
#this is my API key, please replace the one below with your own (google 'google streetview api key'), thanks!
suf="&key="

#this is the directory that will store the streetview images
#this directory will be created if not present
dir=r"/home/ajith/map3"

#checks if the dir variable (output path) above exists and creates it if it does not
if not os.path.exists(dir):
    os.makedirs(dir)

a=[
{1:'42.386196,-71.006075',2:'SARATOGA ST 02128'},
{1:'42.386148,-71.006036',2:'18 BARNES AV 02128'},
]


for a in a:

  ln = a[2].replace(" ","_")
  print "CLEANED UP ADDRESS LINE:\n"+ln
  # creates the url that will be passed to the url reader, this creates the full, valid, url that will return a google streetview image for each address in the address text file
  URL = pre+a[1]+suf
  print "URL FOR STREETVIEW IMAGE:\n"+URL
  #creates the filename needed to save each address's streetview image locally
  if os.path.exists(os.path.join(dir,ln+".jpg")):
    print "##################"
    filename = os.path.join(dir,ln+"_"+str(time.time())+".jpg")
  else:
    filename = os.path.join(dir,ln+".jpg")
  print "OUTPUT FILENAME:\n"+filename
  #you can run this up to this line in the python command line to see what each step does
  #final step, fetches and saves the streetview image for each address using the url created in the previous steps
  urllib.urlretrieve(URL, filename)