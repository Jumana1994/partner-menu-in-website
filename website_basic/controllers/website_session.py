# -*- coding: utf-8 -*-
from odoo.http import Controller, request, route


class Partner(Controller):
    @route('/partner', auth='public', type="http", website=True)
    def partner(self):
        print('helo', request.env.uid)
        country_ids = request.env['res.country'].search([],)
        print(country_ids)
        return request.render('website_basic.website_partner_template',
                              {'country_ids': country_ids})

    @route('/create/partner', auth="public", website=True)
    def create_partner(self,name,email,**kw):
        print('create', kw)
        partner_id = request.env['res.partner'].sudo().create({
            'name':name,
            'email':email,
            'phone':kw.get('phone'),
            'country_id': kw.get('country'),
            'street':kw.get('street')
        })
        partner_ids = request.env['res.partner'].sudo().search([],limit=4,
                                                               order='create_date asc')

        return request.render('website_basic.website_partner_details',
                              {'partner_id':partner_id,
                               'partner_ids':partner_ids})
    @route('/view/partner/<model("res.partner"):partner>',
           auth="public", website=True)
    def view_partner(self,partner):
        print(partner)
        return request.render('website_basic.website_partner_view',
                              {'partner':partner,})


# using this we can specify the user using request.env.uid
# if user we getbthe id only internal users can access the page
# if none all users can access but we wont get the visitor id
# if public all users can access  ang we get the id
#
