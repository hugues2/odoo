# -*- coding: utf-8 -*-
import base64, datetime, requests, json

from odoo import models, fields, api

from odoo.http import request
from odoo import http



class Student(models.Model):
    _name = "wb.student"
    _description = "this is student profile"
    name=fields.Char("Name")
    name1=fields.Char("Name1")
    name2=fields.Char("Name2")
    file_to_sign = fields.Binary(string="File to sign")
    signed_file = fields.Binary(string="Signed file")
    filename=fields.Char()
    docId=fields.Char()

    def prepare_for_signing(self):
        for record in self:

            # Specify the file path where you want to save the PDF file
            file_path = '/tmp/file.pdf'

            # Open the file in binary write mode and write the bytes data
            #with open(file_path, 'wb') as file:
            #    file.write(record.file_to_sign)

            print("host_url"+ request.httprequest.host_url)
            id=(str(record.id))
            cids=str(1)
            menu_id = str(self.env.ref('student.wb_student_root_menu').id)

            action_id=str(self.env.ref('student.wb_student_action').id)
            print(action_id)


            record.name = "Something 2"
            base64_encoded_file = record.file_to_sign.decode('utf-8')
            eIDEasy_request ={
                "files": [
                    {
                        "fileContent": base64_encoded_file,
                        "fileName": record.filename,
                        "mimeType": "application/pdf"
                    }
                    ],
                "client_id": "2IaeiZXbcKzlP1KvjZH9ghty2IJKM8Lg",
                "secret": "56RkLgZREDi1H0HZAvzOSAVlxu1Flx41",
                "container_type": "pdf",
                "signature_redirect": request.httprequest.host_url+'afterSigning'+'?id='+id+'&action_id='+action_id+'&cids='+cids+'&menu_id='+menu_id,
                "notification_state":
                    {
                    "time": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z')
                    }
                }

            json_payload = json.dumps(eIDEasy_request)

            # print (eIDEasy_request["files"])
            print("File name : " + record.filename)
            print("Timestamp : " + datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z'))

            api_url = "https://test.eideasy.com/api/signatures/prepare-files-for-signing"

            # Set the Content-Type header to indicate JSON data
            headers = {"Content-Type": "application/json"}

            # Make the GET request
            response = requests.post(api_url,data=json_payload, headers=headers)


            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                print("API call was ok")
                # Process the API response (assuming it's in JSON format)
                api_data = response.json()
                # Now you can use `api_data` in your Odoo model logic
                record.docId=api_data['doc_id']
                print("Doc Id : "+record.docId)
            else:
                # Handle the error appropriately
                print(response.reason)
                print(response.content)
                print(f"API request failed with status code: {response.status_code}")

        return True

    def send_for_signing(self):
        for record in self:
            docId=record.docId
        return {
            'type': 'ir.actions.act_url',

            'url' : 'https://test.eideasy.com/sign_contract_external?client_id=2IaeiZXbcKzlP1KvjZH9ghty2IJKM8Lg&doc_id='+docId+'&country=BE&lang=en'
        }

    def get_url(self):
        print ("Base URL " + request.httprequest.base_url)
        print ("Host URL" + request.httprequest.host_url)
