from datetime import datetime
import calendar
from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/", methods=['GET', 'POST'])
def aritmetica():
    if request.method == "POST":
        num1 = float(request.form.get('n1'))
        num2 = float(request.form.get('n2'))

        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2
        
        return render_template('index.html', total_suma = suma,
                                            total_resta = resta,
                                            total_multiplicacion = multiplicacion,
                                            total_division = division)
    
    return render_template('index.html')

@app.route('/longitudes', methods=['GET', 'POST'])
def longitudes():
    if request.method == 'POST':
        num1 = float(request.form.get('n1'))

        centimetros = num1 * 100000
        decimetros = num1 * 10000
        metros = num1 * 1000
        decametros = num1 * 100
        hectometros = num1 * 10

        return render_template('longitudes.html',total_centimetros = centimetros,
                                            total_decimetros = decimetros,
                                            total_metros = metros,
                                            total_decametros = decametros,
                                            total_hectometros = hectometros)
    
    return render_template('longitudes.html')

@app.route('/divisas', methods=['GET', 'POST'])
def divisas():
    if request.method == 'POST':
        num1 = int(request.form.get('n1'))

        pesosC = num1 * 4211
        euros = num1 * 0.90
        librasE = num1 * 0.75
        francoS = num1 * 0.85

        return render_template('divisas.html',total_pesosC = pesosC,
                                            total_euros = euros,
                                            total_librasE = librasE,
                                            total_francoS = francoS,)
    
    return render_template('divisas.html')

@app.route('/fechas', methods=['GET', 'POST'])
def fechas():
    if request.method == 'POST':
        
        fecha1_str = request.form.get('fecha1')
        fecha2_str = request.form.get('fecha2')

        fecha1 = datetime.strptime(fecha1_str, '%Y-%m-%d')
        fecha2 = datetime.strptime(fecha2_str, '%Y-%m-%d')

        diferencia_dias = abs((fecha2 - fecha1).days)

        diferencia_semanas = diferencia_dias // 7
        dias_restantes = diferencia_dias % 7

        diferencia_meses = abs((fecha2.year - fecha1.year) * 12 + (fecha2.month - fecha1.month))

        return render_template(
            'fechas.html',
            total_dias=diferencia_dias,
            total_semanas=diferencia_semanas,
            total_dias_restantes=dias_restantes,
            total_meses=diferencia_meses
        )

    return render_template('fechas.html')


if __name__ == '__main__':
    app.run(debug=True)