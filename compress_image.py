from sklearn.cluster import KMeans
import numpy as np
from PIL import Image

def compress_image(image_path, n_colors=8, download=False):
    img = Image.open(image_path)
    img = img.convert('RGB')
    img = img.resize((300, 300))
    pixels = np.array(img).reshape(-1, 3)
    
    kmeans = KMeans(n_clusters=n_colors, random_state=42)
    kmeans.fit(pixels)
    
    
    compressed_pixels = kmeans.cluster_centers_[kmeans.labels_]
    compressed_img = compressed_pixels.reshape(img.size[1], img.size[0], 3).astype(np.uint8)

    compressed_image_path = 'static/compressed_image.jpg'
    Image.fromarray(compressed_img).save(compressed_image_path)
    
    if download:
        return compressed_image_path
