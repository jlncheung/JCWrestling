#Julian Cheung
#301225474
#assignment 3

import cgi
form = cgi.FieldStorage()

#topline
print """Content-type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<style type="text/css"> #stylesheet for this particular order confirmation
body {
  background-color: #FAFAFA;
  color: #2A3B6E;
}
</style>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<title>Order form</title>
</head><body>
"""
#writing my own functions
def bctax():
        print "<p>You have a total of 12% sales tax</p>"
def bcship():
        print "<p>Your shipping and handling cost is $5</p>"

#values for the rest of the program
card=form.getvalue("cardBox") 
monthly= int(form["monthlyBox"].value)
monthlyp= monthly * 50
punch= int(form["punchBox"].value)
punchp= punch * 50
pads= int(form["padsBox"].value)
padsp = pads * 30
guards= int(form["guardsBox"].value)
guardsp= guards * 25
shoes= int(form["shoesBox"].value)
shoesp= shoes * 100
total= monthly + punch + pads + guards + shoes
totalp= monthlyp + punchp + padsp + guardsp + shoesp    #total price for everything

#start of program
print "<p> Name:", form.getvalue("nameBox"), "</p>"
print "<p> Email:", form.getvalue("emailBox"), "</p>"
print "<p> Address:", form.getvalue("streetBox"),",",form.getvalue("cityBox"),",", form.getvalue("provinceBox"),",", form.getvalue("postalBox"),"</p>"
print "<p> Credit Card information:", form.getvalue("typeSelect"), form.getvalue("Exp1Box"),"/" , form.getvalue("Exp2Box"),", xxxx-xxxx-xxxx-", card[11:15],"</p>"
print "<p>", monthly, "Monthly Training pass Gift Certificates at $50 a piece is $", monthlyp ,"</p>"
print "<p>", punch, "10-punch pass Gift Certificates at $50 a piece is $", punchp ,"</p>"
print "<p>", pads, "Knee pads at $30 a piece is $", padsp ,"</p>"
print "<p>", guards, "Ear guards at $25 a piece is $", guardsp ,"</p>"
print "<p>", shoes, "Wrestling shoes at $100 a piece is $", shoesp ,"</p>"

#giftwrapping yes/no
if form.getvalue("giftcheck"):
	print "<p>The total gift-wrapping cost is $", total, "</p>"
	totalp= totalp + total
else:
	print "<p>You did not want your items to be gift-wrapped</p>"
if totalp >= 150:
        print "<p>You have saved 15% from your total</p>"
        totalp = totalp * .85
if totalp == 200:
        print "<p>You have saved $30 from your total!</p>"
        totalp = totalp - 30

#sales tax
if form.getvalue("provinceBox") == "bc":
        bctax()
        totalp = totalp * 1.12
elif form.getvalue("provinceBox") == "Bc":
        bctax()
        totalp = totalp * 1.12
elif form.getvalue("provinceBox") == "bC":
        bctax()
        totalp = totalp * 1.12
elif form.getvalue("provinceBox") == "BC":
        bctax()
        totalp = totalp * 1.12
else:
        print "<p>You have a total of 6% sales tax</p>"
        totalp = totalp * 1.06

#shipping fee
if form.getvalue("provinceBox") == "bc":
        bcship()
        totalp = totalp + 5
elif form.getvalue("provinceBox") == "Bc":
        bcship()
        totalp = totalp + 5
elif form.getvalue("provinceBox") == "bC":
        bcship()
        totalp = totalp + 5
elif form.getvalue("provinceBox") == "BC":
        bcship()
        totalp = totalp + 5
else:
        print "<p>Your shipping and handling cost is $10</p>"
        totalp = totalp + 10
        
print "<p>Your total cost for this order is:$", totalp, "</p>"
if form.getvalue("shipcheck"):
        print "<p>You will be notified when the order has shipped via email</p>"
print """<p>Thank you for ordering with us.<br/>
If you have any questions, contact: Julian 123-321-3456.</p>

</body>
</html>
"""
