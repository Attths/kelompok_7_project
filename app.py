from flask import Flask, request,  render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about-project.html')

# zakat emas
@app.route('/zakat-emas', methods=['GET', 'POST'])
def zakat_emas():
    harga_emas_per_gram = 1439700
    if request.method == 'POST':
        jumlah_emas = float(request.form['jumlah_emas'])

        nisab = 85 * harga_emas_per_gram
        total_nilai_emas = jumlah_emas
        total_nilai_zakat = 0

        if total_nilai_emas >= nisab:
            total_nilai_zakat = 0.025 * jumlah_emas
            wajib_zakat = True

        else:
            wajib_zakat = False

        total_nilai_zakat_formatted = f"{total_nilai_zakat:,.2f}".replace(",", ".")
        nisab_formatted = f"{nisab:,.2f}".replace(",", ".")

        return render_template('zakat_emas.html', 
                               wajib_zakat=wajib_zakat, 
                               nilai_zakat=total_nilai_zakat_formatted,
                               nisab=nisab_formatted,
                               harga_emas_per_gram=f"{harga_emas_per_gram:,.2f}".replace(",", "."))
    
    return render_template('zakat_emas.html', nilai_zakat=None, harga_emas_per_gram=f"{harga_emas_per_gram:,.2f}".replace(",", "."))


# zakat perdagangan
@app.route('/zakat-perdagangan', methods=['GET', 'POST'])
def zakat_perdagangan():
    harga_emas_per_gram = 1439700

    if request.method == 'POST':
            modal = float(request.form['jumlah_modal'])
            keuntungan = float(request.form['jumlah_keuntungan'])
            piutang = float(request.form['jumlah_piutang'])
            hutang = float(request.form['jumlah_hutang'])
            kerugian = float(request.form['jumlah_kerugian'])

            nisab = 85 * harga_emas_per_gram
            nilai_dagang = (modal + keuntungan + piutang) - (kerugian + hutang)
            total_nilai_zakat = 0

            if nilai_dagang >= nisab:
                total_nilai_zakat = 0.025 * nilai_dagang
                wajib_zakat = True

            else:
                wajib_zakat = False

            total_nilai_zakat_formatted = f"{int(total_nilai_zakat):,}".replace(",", ".")
            nisab_formatted = f"{int(nisab):,}".replace(",", ".")

            return render_template('zakat-perdagangan.html',
                                   wajib_zakat=wajib_zakat,
                                   nilai_zakat = total_nilai_zakat_formatted,
                                   nisab = nisab_formatted,
                                   harga_emas_per_gram=f"{int(harga_emas_per_gram):,}".replace(",", "."))
    
    return render_template('zakat-perdagangan.html', nilai_zakat=None, harga_emas_per_gram=f"{harga_emas_per_gram:,.2f}".replace(",", "."))

@app.route('/zakat-pertanian', methods=['GET', 'POST'])
def zakat_pertanian():
    if request.method == 'POST':
        hasil_panen_kg = float(request.form.get('hasil_panen_kg', 0))
        harga_per_kg = float(request.form.get('harga_per_kg', 0))
        sistem_pengairan = request.form.get('sistem_pengairan', 'irigasi')

        nisab = 635
        hasil_panen_rp = hasil_panen_kg * harga_per_kg

        if sistem_pengairan == 'irigasi':
            total_nilai_zakat = 0.05 * hasil_panen_rp
            nilai_zakat_kg = 0.05 * hasil_panen_kg 
        else:
            total_nilai_zakat = 0.1 * hasil_panen_rp
            nilai_zakat_kg = 0.1 * hasil_panen_kg 

        wajib_zakat = total_nilai_zakat >= nisab

        total_nilai_zakat_formatted = f"{total_nilai_zakat:,.2f}".replace(",", ".")
        nisab_formatted = f"{nisab:,.2f}".replace(",", ".")
        harga_per_kg_formatted = f"{harga_per_kg:,.2f}".replace(",", ".")
        nilai_zakat_kg = f"{nilai_zakat_kg:,.2f}".replace(",", ".")

        return render_template('zakat_pertanian.html',
                           wajib_zakat=wajib_zakat,
                           sistem_pengairan=sistem_pengairan,
                           nisab=nisab_formatted,
                           nilai_zakat=total_nilai_zakat_formatted,
                           nilai_zakat_kg=nilai_zakat_kg,
                           harga_per_kg=harga_per_kg_formatted)

    return render_template('zakat_pertanian.html', 
                       nilai_zakat=None, 
                       wajib_zakat=None, 
                       sistem_pengairan=None, 
                       nisab=None, 
                       harga_per_kg=0)


@app.route('/zakat-penghasilan', methods=['GET', 'POST']) 
def zakat_penghasilan(): 
    harga_emas_per_gram = 1439700
    if request.method == 'POST':
        jumlah_penghasilan = float(request.form['hasil_penghasilan'])
        
        nisab = 85 * harga_emas_per_gram / 12
        jumlah_penghasilan = jumlah_penghasilan
        total_nilai_zakat = 0

        if jumlah_penghasilan >= nisab:
            total_nilai_zakat = 0.025 * jumlah_penghasilan
            wajib_zakat = True

        else:
            wajib_zakat = False

        total_nilai_zakat_formatted = f"{total_nilai_zakat:,.2f}".replace(",", ".")
        nisab_formatted = f"{nisab:,.2f}".replace(",", ".")

        return render_template('zakat_penghasilan.html', 
                               wajib_zakat=wajib_zakat, 
                               nilai_zakat=total_nilai_zakat_formatted,
                               nisab=nisab_formatted,
                               harga_emas_per_gram=f"{harga_emas_per_gram:,.2f}".replace(",", "."))
    
    return render_template('zakat_penghasilan.html', nilai_zakat=None, harga_emas_per_gram=f"{harga_emas_per_gram:,.2f}".replace(",", "."))

if __name__ == '__main__':
    app.run(debug=True)