import imp
from flask import Flask
from routes.usuario import usuario
from routes.productos import producto
from routes.orden import orden
from routes.detalle_orden import dl_orden
from routes.compatibildiad_producto import cmp_prodcuto
from routes.categoria_producto import ca_producto
from routes.buildpc import build


app = Flask(__name__)


app.register_blueprint(usuario)
app.register_blueprint(orden)
app.register_blueprint(producto)
app.register_blueprint(dl_orden)
app.register_blueprint(cmp_prodcuto)
app.register_blueprint(ca_producto)
app.register_blueprint(build)
