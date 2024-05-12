from flask import Flask, render_template, request, redirect, url_for, send_file
from compress_image import compress_image

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        if 'image' not in request.files:
            return render_template('index.html', message='No image uploaded')
        
        image_file = request.files['image']
        if image_file.filename == '':
            return render_template('index.html', message='No image selected')
        
        image_path = 'static/uploaded_image.jpg'
        image_file.save(image_path)
        
        compress_image(image_path, n_colors=8, download=True)
        
        compressed_image_path = 'static/compressed_image.jpg'
        return render_template('index.html', compressed_image=compressed_image_path)
    
    return render_template('index.html')
    
@app.route('/download_compressed')
def download_compressed():
    compressed_image_path = 'static/compressed_image.jpg'
    return send_file(compressed_image_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
