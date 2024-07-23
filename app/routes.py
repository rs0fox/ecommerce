from app import app, db
from app.models import Product

@app.route('/')
def index():
    products = Product.query.all()
    return 'Products: {}'.format(products)

@app.route('/product/<int:id>')
def product(id):
    product = Product.query.get(id)
    return 'Product: {}'.format(product.name)
