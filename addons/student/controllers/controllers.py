# controllers/controller.py


# -*- coding: utf-8 -*-
from odoo import http
class Test(http.Controller):
    @http.route('/afterSigning', auth='public')
    def index(self, **kwargs):
        print("Return from eID Easy")
        print("docId : " + kwargs.get('docId'))
        print("formId : " + kwargs.get('formId'))
        print ("actionId :" + http.request.env.ref('student.wb_student_action', raise_if_not_found=False))

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'wb.student',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'views': [(wb_student_tree_view[0].id, 'tree'), (False, 'form')],
            'view_id ref="student.wb_student_tree_view"': '',
            'target': 'current',
            'domain': domain,
        }
