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
    nisab = 85 * harga_emas_per_gram
    nisab_formatted = f"{nisab:,.2f}".replace(",", ".")

    if request.method == 'POST':
        jumlah_emas = float(request.form['jumlah_emas'])

        total_nilai_emas = jumlah_emas
        total_nilai_zakat = 0

        if total_nilai_emas >= nisab:
            total_nilai_zakat = 0.025 * jumlah_emas
            wajib_zakat = True

        else:
            wajib_zakat = False

        total_nilai_zakat_formatted = f"{total_nilai_zakat:,.2f}".replace(",", ".")
        
        return render_template('zakat_emas.html', 
                               wajib_zakat=wajib_zakat, 
                               jumlah_zakat=total_nilai_zakat_formatted,
                               nisab=nisab_formatted,
                               harga_emas_per_gram=f"{harga_emas_per_gram:,.2f}".replace(",", "."))
    
    return render_template('zakat_emas.html', 
                           jumlah_zakat=None,
                           nisab=nisab_formatted,
                           harga_emas_per_gram=f"{harga_emas_per_gram:,.2f}".replace(",", "."))


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
                                   jumlah_zakat = total_nilai_zakat_formatted,
                                   nisab = nisab_formatted,
                                   harga_emas_per_gram=f"{int(harga_emas_per_gram):,}".replace(",", "."))
    
    return render_template('zakat-perdagangan.html', jumlah_zakat=None, harga_emas_per_gram=f"{harga_emas_per_gram:,.2f}".replace(",", "."))

# zakat pertanian
@app.route('/zakat-pertanian', methods=['GET', 'POST'])
def zakat_pertanian():
    if request.method == 'POST':
        hasil_panen_kg = float(request.form.get('hasil_panen_kg', 0))
        harga_per_kg = float(request.form.get('harga_per_kg', 0))
        sistem_pengairan = request.form.get('sistem_pengairan')

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
                           jumlah_zakat=total_nilai_zakat_formatted,
                           nilai_zakat_kg=nilai_zakat_kg,
                           harga_per_kg=harga_per_kg_formatted)

    return render_template('zakat_pertanian.html', 
                       jumlah_zakat=None, 
                       wajib_zakat=None, 
                       sistem_pengairan=None, 
                       nisab=None, 
                       harga_per_kg=0)

# zakat penghasilan
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
                               jumlah_zakat=total_nilai_zakat_formatted,
                               nisab=nisab_formatted,
                               harga_emas_per_gram=f"{harga_emas_per_gram:,.2f}".replace(",", "."))
    
    return render_template('zakat_penghasilan.html', jumlah_zakat=None, harga_emas_per_gram=f"{harga_emas_per_gram:,.2f}".replace(",", "."))

@app.route('/zakat-peternakan', methods=['GET', 'POST'])
def zakat_peternakan():
    if request.method == 'POST':
        # Ambil input dari pengguna
        jenis_ternak = request.form.get('jenis_ternak')
        jumlah_ternak = int(request.form.get('jumlah_ternak', 0))

        # Default nilai jika tidak memenuhi syarat
        wajib_zakat = False
        jumlah_zakat = 0
        deskripsi = "Tidak wajib zakat"

        # Aturan zakat untuk sapi
        if jenis_ternak == "sapi":
            if jumlah_ternak < 30:
                deskripsi = "Jumlah ternak kurang dari nisab (30 ekor)"
            elif jumlah_ternak <= 39:
                wajib_zakat = True
                jumlah_zakat = 1
                deskripsi = "1 ekor anak sapi jantan/betina umur 1 tahun"
            elif jumlah_ternak <= 59:
                wajib_zakat = True
                jumlah_zakat = 1
                deskripsi = "1 ekor anak sapi betina umur 1 tahun"
            elif jumlah_ternak <= 69:
                wajib_zakat = True
                jumlah_zakat = 3
                deskripsi = "3 ekor anak sapi jantan/betina umur 1 tahun"
            elif jumlah_ternak <= 79:
                wajib_zakat = True
                jumlah_zakat = 3
                deskripsi = "2 ekor anak sapi betina umur 2 tahun + 1 ekor anak sapi jantan umur 1 tahun"
            else:
                wajib_zakat = True
                kelipatan = (jumlah_ternak - 79) // 100
                jumlah_zakat = 3 + kelipatan
                deskripsi = "Jika LEBIH DARI 70, setiap bertambah 30 ekor zakatnya 1 ekor umur 1 tahun. setiap bertambah 40 ekor, zakatnya bertambah 1 ekor umur 2 tahun"

        # Aturan zakat untuk kambing
        elif jenis_ternak == "kambing":
            if jumlah_ternak < 40:
                deskripsi = "Jumlah ternak kurang dari nisab (40 ekor)"
            elif jumlah_ternak <= 120:
                wajib_zakat = True
                jumlah_zakat = 1
                deskripsi = "1 ekor kambing"
            elif jumlah_ternak <= 200:
                wajib_zakat = True
                jumlah_zakat = 2
                deskripsi = "2 ekor kambing"
            elif jumlah_ternak <= 300:
                wajib_zakat = True
                jumlah_zakat = 3
                deskripsi = "3 ekor kambing"
            else:
                wajib_zakat= True
                kelipatan = (jumlah_ternak - 300) // 100
                jumlah_zakat = 3 + kelipatan
                deskripsi='Jika lebih dari 300, setiap kelipatan 100 ekor maka kadar zakatnya ditambah 1 ekor lagi.'

        # Tampilkan hasil
        return render_template(
            'zakat_peternakan.html',
            wajib_zakat=wajib_zakat,
            jumlah_zakat=jumlah_zakat,
            deskripsi=deskripsi
        )

    # Halaman kosong untuk GET
    return render_template(
        'zakat_peternakan.html',
        jenis_ternak = None,
        wajib_zakat=None,
        jumlah_zakat=None,
        deskripsi=None,
        jumlah_ternak=0
    )

if __name__ == '__main__':
    app.run(debug=True)