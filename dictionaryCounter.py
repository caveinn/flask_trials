from flask import Flask, redirect,url_for,request,render_template

app =Flask(__name__)

@app.route ("/")
def index():
	return render_template("sentance.html")
@app.route('/some',methods=['POST','GET'])
def some():
	sent=request.args.get("sent")
	sentanceCount={}
	for charatcter in sent:
		sentanceCount.setdefault(charatcter,0)
		sentanceCount[charatcter]+=1
	return render_template("Table.html",sentanceCount=sentanceCount)
if __name__=="__main__":
	app.run(debug=True)
