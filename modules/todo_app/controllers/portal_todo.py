# -*- coding: utf-8 -*-

import math
from odoo import http
from odoo.http import request


class PortalTodo(http.Controller):
    _items_per_page = 10

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        values['todos_count'] = 100
        return values
    
    @http.route(['/my/todo', '/my/todo/page/<int:page>'], type='http', auth='user', website=True)
    def portal_todo(self, page=1, **kwargs):
        values = self._prepare_todo_values(page)

        total = values['total']
        page_count = math.ceil(total / self._items_per_page)

        values.update(
            {
                'pager': {
                    'url': '/my/todo',
                    'total': total,
                    'page': page,
                    'step': self._items_per_page,
                    'page_count': page_count,
                }
            }
        )

        return request.render('todo_app.portal_my_todos', values)

    def _prepare_todo_values(self, page):
        Todo = request.env['todo_app.todo']
        user = request.env.user

        domain = [('user_id', '=', user.id)]
        
        total_todos = Todo.search_count(domain)

        todos = Todo.search(
            domain, order='create_date desc',
            limit=self._items_per_page,
            offset=(page - 1) * self._items_per_page
        )

        return {
            'todos': todos,
            'total': total_todos,
        }
    
    @http.route(['/my/todo/<int:todo_id>'], type='http', auth='user', website=True)
    def portal_todo_page(self, todo_id, **kwargs):
        Todo = request.env['todo_app.todo'].sudo()
        todo = Todo.browse(todo_id)
        
        return request.render('todo_app.portal_todo_page', {'todo': todo})
