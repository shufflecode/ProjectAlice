from flask import jsonify

from core.interface.model.Api import Api
from core.util.Decorators import ApiAuthenticated


class TelemetryApi(Api):
	route_base = f'/api/{Api.version()}/telemetry/'


	def __init__(self):
		super().__init__()


	@ApiAuthenticated
	def post(self):
		try:
			return jsonify(message='Not implemented')
		except Exception as e:
			self.logError(f'Failed getting telemetry data: {e}')
			return jsonify(success=False)
