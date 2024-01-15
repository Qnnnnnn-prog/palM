#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template
import google.generativeai as palM


# In[ ]:


palM.configure(api_key = "AIzaSyB0OhFEkITMtkm03WTIIS42GAdz5-PNnsI")
model = {"model":"models/chat-bison-001"}
app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")
        print(q)
        r = palM.chat(
        **model,
            messages = q
        )

        return(render_template("index.html",result = r.last))
    else:
        return(render_template("index.html",result = "waiting for question........."))
if __name__  == "__main__":
    app.run()


# In[ ]:


if __name__  == "__main__":
    app.run()


# In[ ]:




