import os
import json
from inference.exceptions import ModelNotFound, ApplicationError, InvalidModelConfiguration, InferenceEngineNotFound, \
	ModelNotLoaded


class InferenceEngineFactory:

	@staticmethod
	def get_engine(path_to_model):
		"""
		Reads the model's inference engine from the model's configuration and calls the right inference engine class.
		:param path_to_model: Model's path
		:return: The model's instance
		"""
		if not os.path.exists(path_to_model):
			raise ModelNotFound()
		try:
			configuration = json.loads(open(os.path.join(path_to_model, 'config.json')).read())
		except Exception:
			raise InvalidModelConfiguration('config.json not found or corrupted')
		try:
			inference_engine_name = configuration['inference_engine_name']
		except Exception:
			raise InvalidModelConfiguration('missing inference engine name in config.json')
		try:
			# import one of the available inference engine class (in this project there's only one), and return a
			# model instance
			if inference_engine_name=='yolov3_opencv_cpu_detection' or inference_engine_name=='yolov4_opencv_cpu_detection':
				print(getattr(__import__("yolo_opencv_cpu_detection"), 'InferenceEngine')(path_to_model))
				return getattr(__import__("yolo_opencv_cpu_detection"), 'InferenceEngine')(path_to_model)
		except ApplicationError as e:
			raise e
		except Exception as e:
			raise InferenceEngineNotFound(inference_engine_name)
