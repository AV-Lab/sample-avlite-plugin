from avlite.c10_perception.c12_perception_strategy import PerceptionStrategy

import logging
log = logging.getLogger(__name__)

class TestPerceptionStrategy(PerceptionStrategy):
    def __init__(self, perception_model, setting=None):
        super().__init__(perception_model, setting)
    
    @property
    def requirements(self) -> set:
        return set()
    
    @property
    def capabilities(self) -> set:
        return set()

    def perceive(self, rgb_img=None, depth_img=None, lidar_data=None, perception_model=None):
        log.info("Perceive method called...")
