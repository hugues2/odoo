# controllers/controller.py


# -*- coding: utf-8 -*-
from odoo import http
class Test(http.Controller):
    @http.route('/afterSigning', auth='public')
    def index(self, **kwargs):
        print("Return from eID Easy")
        id=kwargs.get('id')
        cid = kwargs.get('cid')
        menu_id = kwargs.get('menu_id')
        action_id = kwargs.get('action_id')



        print("docId : " + kwargs.get('docId'))
        print("cids : " + kwargs.get('cids'))
        print("menu_id : " + kwargs.get('menu_id'))
        print("return URL : " + kwargs.get('returnUrl'))

        host_url=http.request.httprequest.host_url

        returnUrl=host_url+"/web#id="+id+"&cid="+cid+"&menu="+menu_id+"&action="+action_id+"&model=web.student"+"&view_type=form"
        print(returnUrl)

        return http.request.redirect(returnUrl)
