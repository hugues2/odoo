# controllers/controller.py


# -*- coding: utf-8 -*-
from odoo import http
class Test(http.Controller):
    @http.route('/afterSigning', auth='public')
    def index(self, **kwargs):
        print("Return from eID Easy")
        id=kwargs.get('id')
        cids = kwargs.get('cids')
        menu_id = kwargs.get('menu_id')
        action_id = kwargs.get('action_id')


        print ("id" + id)
        print ("cids"+cids)
        print("menu_id"+menu_id)
        print("action_id"+action_id)

        host_url=http.request.httprequest.host_url

        returnUrl=host_url+"/web#id="+id+"&cids="+cids+"&menu="+menu_id+"&action="+action_id+"&model=web.student"+"&view_type=form"
        print(returnUrl)

        return http.request.redirect(returnUrl)
