# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = "wb.student"
    _description = "this is student profile"
    name=fields.Char("Name")
    name1=fields.Char("Name1")
    name2=fields.Char("Name2")

    def action_greet(self):
        # Concatenate "Hello" with the value of the "name" field
        message = "Hello " + self.name


        # Display a prompt or print the message (you can customize this part based on your needs)
        self.env['base'].display_warning(title="Greeting", message=message)
