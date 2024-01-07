# controllers/controller.py


# -*- coding: utf-8 -*-
from odoo import http
class Test(http.Controller):
    @http.route('/afterSigning', auth='public')
    def index(self, **kwargs):
        print("Return from eID Easy")
        print("docId : " + kwargs.get('docId'))
        print("formId : " + kwargs.get('formId'))
        print("return URL : " + kwargs.get('returnUrl'))

        returnUrl=kwargs.get('return')

        return http.request.redirect(returnUrl)
