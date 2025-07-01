from flask import Flask, render_template

app = Flask(__name__)

# Main Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

@app.route('/organizations')
def organizations():
    return render_template('organizations.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Portfolio Detail Routes
@app.route('/portfolio/octave')
def portfolio_octave():
    return render_template('portfolio_octave.html')

@app.route('/portfolio/ctf')
def portfolio_ctf():
    return render_template('portfolio_ctf.html')

@app.route('/portfolio/forensics')
def portfolio_forensics():
    return render_template('portfolio_forensics.html')

@app.route('/portfolio/pcap')
def portfolio_pcap():
    return render_template('portfolio_pcap-analysis.html')

@app.route('/portfolio/ethical-hacking')
def portfolio_ethical_hacking():
    return render_template('portfolio_ethical-hacking.html')

@app.route('/portfolio/osint')
def portfolio_osint():
    return render_template('portfolio_osint_hackers.html')

@app.route('/portfolio/srm')
def portfolio_srm():
    return render_template('portfolio_srm_website.html')

@app.route('/portfolio/wmp')
def portfolio_wmp():
    return render_template('portfolio_wmp.html')

@app.route('/portfolio/wmpse')
def portfolio_wmpse():
    return render_template('portfolio_wmpse.html')

@app.route('/portfolio/cepicafe')
def portfolio_cepicafe():
    return render_template('portfolio_cepicafe.html')

@app.route('/portfolio/ai')
def portfolio_ai():
    return render_template('portfolio_ai.html')

@app.route('/portfolio/forensic-cases')
def portfolio_forensic_cases():
    return render_template('forensic_cases.html')

# Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)