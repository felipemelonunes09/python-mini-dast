
from scan import scan_controller
from run import app

app.register_blueprint(scan_controller.scan, url_prefix="/scan")
