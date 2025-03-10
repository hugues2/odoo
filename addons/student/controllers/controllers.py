# controllers/controller.py

import requests, json
# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from ..constants import CLIENT_ID, SECRET
class Test(http.Controller):

    @http.route('/test', auth='public')
    def index(self, **kwargs):
        record=request.env['wb.student'].sudo().search([('id', '=', 5)])
        docId=record['docId']
        print(docId)

    @http.route('/afterSigning', auth='public')
    def index(self, **kwargs):
        print("Return from eID Easy")
        id=kwargs.get('id')
        cids = kwargs.get('cids')
        menu_id = kwargs.get('menu_id')
        action_id = kwargs.get('action_id')

        record=request.env['wb.student'].sudo().search([('id', '=', int(id))])

        #print(record)

        #record = request.env['wb.student'].browse(id)

        docId=record['docId']

        print("docId:" + docId)

        eIDEasy_request = {
                    "secret": SECRET,
                    "client_id": CLIENT_ID,
                    "doc_id": docId
                }

        json_payload = json.dumps(eIDEasy_request)
        print(json_payload)
        api_url = "https://test.eideasy.com/api/signatures/download-signed-file"

        headers = {"Content-Type": "application/json"}

        # Make the GET request
        response = requests.post(api_url, data=json_payload, headers=headers)
        print(response.reason)
        print(response.content)


        api_data = response.json()

        print ("response status" + api_data['status'])
        record['signed_file']=api_data['signed_file_contents']





        record.write({'name1': 'UPDATED'})


        print ("id" + id)
        print ("cids"+cids)
        print("menu_id"+menu_id)
        print("action_id"+action_id)

        host_url=http.request.httprequest.host_url

        returnUrl=host_url+"/web#id="+id+"&cids="+cids+"&menu="+menu_id+"&action="+action_id+"&model=web.student"+"&view_type=form"
        print(returnUrl)

        return http.request.redirect(returnUrl)
