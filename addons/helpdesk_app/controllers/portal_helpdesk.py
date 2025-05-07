# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class PortalHelpdesk(http.Controller):
    @http.route('/support', type='http', auth='public', website=True)
    def portal_support_form(self, **post):
        return request.render('helpdesk_app.portal_support_form_template', {})

    @http.route('/support/submit', type='http', auth='public', website=True)
    def portal_support_ticket_submit(self, **post):
        if post:
            external_type = request.env.ref('helpdesk_app.helpdesk_type_2')
            request.env['helpdesk_app.helpdesk_ticket'].create(
                {
                    'partner_email': post.get('email'),
                    'partner_phone': post.get('phone').strip(),
                    'title': post.get('subject').strip(),
                    'query': post.get('query').strip(),
                    'description': post.get('description').strip(),
                    'type_id': external_type.id,
                }
            )
            return request.render('helpdesk_app.portal_support_ticket_received_template', {})
        return request.redirect('/support')
