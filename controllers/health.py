from odoo import http
from odoo.http import Response

class HealthController(http.Controller):

    @http.route('/web/health', type='http', auth='none', methods=['GET'], csrf=False)
    def health(self):
        try:
            # Query mínima para comprobar que la DB responde
            http.request.env.cr.execute("SELECT 1")
            return Response("OK", status=200)
        except Exception:
            return Response("DB ERROR", status=500)