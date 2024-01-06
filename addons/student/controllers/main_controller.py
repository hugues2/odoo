# controllers/main_controller.py

from odoo import http
from odoo.http import request

class MainController(http.Controller):
    @http.route('/afterSigning', auth='public', website=True)
    def main_method(self, **kw):
        param_value = request.params.get('param_name')
        print("Return from eID Easy")
        #return True
        return http.request.render('your_module.template_name', {'param_value': param_value})
