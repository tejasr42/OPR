from bs4 import BeautifulSoup
import requests
scores=[]
file=requests.get("https://www.thebluealliance.com/event/2017nysu").text.encode('utf-8')
soup=BeautifulSoup(file,"html.parser")

red = soup.findAll("td", { "class" : "red" })
reds = soup.findAll("td", { "class" : "redScore" })
blue = soup.findAll("td", { "class" : "blue" })
blues = soup.findAll("td", { "class" : "blueScore" })

for i in range(80):
	temp=[]
	temp.append(int(red[(6*i)+0].get_text("",strip=True)))
	temp.append(int(red[(6*i)+1].get_text("",strip=True)))
	temp.append(int(red[(6*i)+2].get_text("",strip=True)))
	temp.append(int(reds[2*i].get_text()))
	scores.append(temp)
	temp=[]
	temp.append(int(blue[(6*i)+0].get_text("",strip=True)))
	temp.append(int(blue[(6*i)+1].get_text("",strip=True)))
	temp.append(int(blue[(6*i)+2].get_text("",strip=True)))
	temp.append(int(blues[2*i].get_text()))
	scores.append(temp)
	#print str(i+1)+": "+red[(6*i)+0].get_text("",strip=True)+" | "+red[(6*i)+1].get_text("",strip=True)+" | "+red[(3*2)+0].get_text("",strip=True)+" || "+reds[2*i].get_text("",strip=True)+" ||||| "+blue[(6*i)+0].get_text("",strip=True)+" | "+blue[(6*i)+1].get_text("",strip=True)+" | "+blue[(6*i)+2].get_text("",strip=True)+" || "+blues[2*i].get_text("",strip=True)



teams=[20,250,303,353,369,395,527,639,810,1155,1156,1382,1600,1635,1665,1796,1880,1923,2265,2601,2869,2872,2875,3004,3044,3204,3314,3419,3950,4091,4122,4571,5016,5123,5202,5599,5781,5814,5943,5955,6024,6058,6300,6401,6593,6601,6636,6648]
opr=[0]*48
diff=[0]*48

costi=0
costf=0
grad=100
rate=0.33/len(scores)
for a in scores:
		costi+=(a[3]-(opr[teams.index(a[0])]+opr[teams.index(a[1])]+opr[teams.index(a[2])]))**2

while grad>0.001:
	for x in range(48):	
		for a in scores:
			if teams.index(a[0])==x or teams.index(a[1])==x or teams.index(a[2])==x:
				diff[x]+=rate*(a[3]-(opr[teams.index(a[0])]+opr[teams.index(a[1])]+opr[teams.index(a[2])]))	
	for i in range(48):
		opr[i]+=diff[i]
		diff[i]=0
	for a in scores:
		costf+=(a[3]-(opr[teams.index(a[0])]+opr[teams.index(a[1])]+opr[teams.index(a[2])]))**2
	grad=(costi-costf)
	#print grad
	costi=costf
	costf=0
oprdict={}
for i in range(48):
	oprdict[str(teams[i])]=opr[i]

#oprdict=sorted(oprdict.iteritems(), key=lambda (k,v): (v,k))

for key, value in sorted(oprdict.iteritems(), key=lambda (k,v): (v,k),reverse=True):
	print str(key)+": "+str(value)