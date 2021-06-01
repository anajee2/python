from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def basic():
    return render_template('proj3converter.html')


@app.route('/')
def name_site(name):
    return 'Hello'.format(name=name)


if __name__ == '__main__':
    app.run()


#HTML CODE
<html>
 <body>
   <fieldset> 
  <form name="literconverter">
  	<p><b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input(Liters)</b> <br>
	<p></p>
    A &nbsp;<input type="text" value = "" name="literdisp">
   <input type="button" value="Convert" onclick="pintform.pintdisp.value=eval((2.11338).toFixed(2)*literconverter.literdisp.value); quartsform.quartsdisp.value=eval((1.05669).toFixed(2)*literconverter.literdisp.value);
   gallonform.gallondisp.value=eval((0.264172).toFixed(2)*literconverter.literdisp.value)">
   
   
   <input type="button" name="clear" value="Clear" onclick="literconverter.literdisp.value=''; pintform.pintdisp.value=''; quartsform.quartsdisp.value=''; gallonform.gallondisp.value=''">
   
  </p>
  </form>
	
	
  <p><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output</b></p>
  
  
  <form name="pintform">
  <p align="left">
   <b> </b> <br>
   B &nbsp;<input type="text" name="pintdisp"> Pints<br><br>
  </p>
  </form>

  <form name="quartsform">
  <p align="left">
   <b> </b> <br>
   C &nbsp;<input type="text" name="quartsdisp"> Quarts<br><br>
  </p>
  </form>
  
  <form name="gallonform">
  <p align="left">
   <b> </b> <br>
   D &nbsp;<input type="text" name="gallondisp"> Gallons<br><br>
  </p>
  </form>

  
   
  </p>
</fieldset>
</body>
</html>