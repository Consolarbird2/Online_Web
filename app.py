from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)




@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
            req = request.form
            web_num = ["num"]
    return render_template("/index.html")

@app.route("/option1", methods=["GET", "POST"])
def option1():
    
   
    if request.method == "POST":
        req = request.form
        title= req["title"]
        image1= req["image1"]
        image2= req["image2"]
        image3= req["image3"]
        image4= req["image4"]
        image5= req["image5"]
        image6= req["image6"]
        image7= req["image7"]
        image8= req["image8"]
        image9= req["image9"]
        location1= req["location1"]
        location2= req["location2"]
        location3= req["location3"]
        location4= req["location4"]
        location5= req["location5"]
        location6= req["location6"]
        location7= req["location7"]
        location8= req["location8"]
        location9= req["location9"]
        image_of_you1= req["image_of_you1"]
        image_of_you2= req["image_of_you2"]
        about_you= req["about_you"]
        email= req["email"]
        home= req["home"]
        phone_no= req["phone_no"]
        bg_color= req["bg_color"]
        footer= req["footer"]
      

        return render_template("/index_test.html", footer=footer, bg_color=bg_color, title=title, image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6, image7=image7, image8=image8, image9=image9, location1=location1, location2=location2, location3=location3, location4=location4, location5=location5, location6=location6, location7=location7, location8=location8, location9=location9,  image_of_you1= image_of_you1, image_of_you2=image_of_you2, about_you= about_you, email=email, home=home, phone_no=phone_no)
    return render_template("/option1.html")

@app.route("/test", methods=["GET", "POST"])
def test():
    title = "webtest"
    heading = "test page"
    if request.method == "POST":
        req = request.form
        videourl = req["videourl"]
        background = req["background"]
        para1 = req["para1"]
        para2 = req["para2"]
        return render_template("/temp2.html", para1=para1, para2=para2, background=background, videourl=videourl)
    return render_template("/test.html")

@app.route("/index_test", methods=["GET", "POST"])
def index_test():
    return render_template("/index_test.html")





if __name__ == '__main__':
    app.run(debug=True)
