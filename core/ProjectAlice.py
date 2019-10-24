import subprocess

from core.base.SuperManager import SuperManager
from core.commons.model.Singleton import Singleton


class ProjectAlice(Singleton):

	NAME = 'ProjectAlice'

	def __init__(self, restartHandler: callable):
		Singleton.__init__(self, self.NAME)
		self.logInfo('Starting up project Alice core')
		self._restart = False
		self._restartHandler = restartHandler
		self._superManager = SuperManager(self)

		self._superManager.initManagers()
		self._superManager.onStart()

		if self._superManager.configManager.getAliceConfigByName('useSLC'):
			subprocess.run(['sudo', 'systemctl', 'start', 'snipsledcontrol'])

		self._superManager.onBooted()


	@property
	def name(self) -> str:
		return self.NAME


	@property
	def restart(self) -> bool:
		return self._restart


	@restart.setter
	def restart(self, value: bool):
		self._restart = value


	def doRestart(self):
		self._restart = True
		self._restartHandler()


	def onStop(self):
		self.logInfo('Shutting down Project Alice')
		self._superManager.onStop()
		if self._superManager.configManager.getAliceConfigByName('useSLC'):
			subprocess.run(['sudo', 'systemctl', 'stop', 'snipsledcontrol'])
