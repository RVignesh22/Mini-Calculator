from flask import Flask,redirect,render_template,request
apk=Flask(__name__)

@apk.route("/",methods=["GET","POST"])
def calcul():
    if request.method=="POST":
        r=request.form["num1"]
        R=int(r)
        v=request.form["num2"]
        V=int(v)
        i=request.form["values"]

        if i=="ADD":
            add=R+V
            return render_template("cal1.html",TOTAL=add)
        elif i=="SUB":
            sub=R-V
            return render_template("cal1.html",TOTAL=sub)
        elif i=="MUL":
            mul=R*V
            return render_template("cal1.html",TOTAL=mul)
        elif i=="DIV":
            div=R/V
            return render_template("cal1.html",TOTAL=div)
        
        else:
            return "INVALID VALUE"
        
    else:
        return render_template("calu.html")


if __name__=="__main__":
    apk.run(debug=True)
    