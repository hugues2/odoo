# controllers/controller.py

import requests
# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from ..constants import CLIENT_ID, SECRET
class Test(http.Controller):
    @http.route('/afterSigning', auth='public')
    def index(self, **kwargs):
        print("Return from eID Easy")
        id=kwargs.get('id')
        cids = kwargs.get('cids')
        menu_id = kwargs.get('menu_id')
        action_id = kwargs.get('action_id')

        record = request.env['wb.student'].browse(id)

        docId=record['docId']

        eIDEasy_request = {
                    "secret": SECRET,
                    "client_id" : CLIENT_ID,
                    "docId" : docId
                }

        json_payload = json.dumps(eIDEasy_request)
        api_url = "https://test.eideasy.com/api/signatures/download-signed-file"

        headers = {"Content-Type": "application/json"}

        # Make the GET request
        response = requests.post(api_url, data=json_payload, headers=headers)

        api_data = response.json()

        print ("response status" + api_data['status'])
        record['signed_file']=api_data['signed_file_content']





        record.write({'name1': 'UPDATED'})


        print ("id" + id)
        print ("cids"+cids)
        print("menu_id"+menu_id)
        print("action_id"+action_id)

        host_url=http.request.httprequest.host_url

        returnUrl=host_url+"/web#id="+id+"&cids="+cids+"&menu="+menu_id+"&action="+action_id+"&model=web.student"+"&view_type=form"
        print(returnUrl)

        return http.request.redirect(returnUrl)
