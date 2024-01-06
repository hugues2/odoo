# controllers/controller.py


# -*- coding: utf-8 -*-
from odoo import http
class Test(http.Controller):
    @http.route('/afterSigning', auth='public')
    def index(self, **kwargs):
        print("Return from eID Easy")
        print("docId : " + kwargs.get('docId'))
        print("formId : " + kwargs.get('formId'))

        return http.request.render('wb_student_tree_view')
