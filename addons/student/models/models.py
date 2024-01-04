# -*- coding: utf-8 -*-
import base64, datetime, requests

from odoo import models, fields, api


class Student(models.Model):
    _name = "wb.student"
    _description = "this is student profile"
    name=fields.Char("Name")
    name1=fields.Char("Name1")
    name2=fields.Char("Name2")
    file_to_sign = fields.Binary(string="File to sign")
    filename=fields.Char()

    def action_do_something(self):
        for record in self:
            record.name = "Something"
            eIDEasy_request ={
                "files": [
                    {
                        "fileContent": base64.b64encode(record.file_to_sign).decode('utf-8'),
                        "fileName": record.filename,
                        "mimeType": "application/pdf"
                    }
                    ],
                "client_id": "2IaeiZXbcKzlP1KvjZH9ghty2IJKM8Lg",
                "secret": "56RkLgZREDi1H0HZAvzOSAVlxu1Flx41",
                "container_type": "pdf",
                "signature_redirect": "google.com",
                "notification_state":
                    {
                    "time": str(datetime.datetime.now())
                    }
                }


            print("File name : " + record.filename)

            api_url = "https://test.eideasy.com/api/signatures/prepare-files-for-signing"

            # Set the Content-Type header to indicate JSON data
            headers = {"Content-Type": "application/json"}

            # Make the GET request
            response = requests.get(api_url,json=eIDEasy_request, headers=headers)


            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Process the API response (assuming it's in JSON format)
                api_data = response.json()
                # Now you can use `api_data` in your Odoo model logic
            else:
                # Handle the error appropriately
                print(response.reason)
                print(f"API request failed with status code: {response.status_code}")

        return True
