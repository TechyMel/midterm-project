########################
# Logger Configuration #
########################

import logging #pragma: no cover

from app.calculator_config import CalculatorConfig

config = CalculatorConfig()

# Ensure log directory exists
config.log_dir.mkdir(parents=True, exist_ok=True)

logging.basicConfig(  # pragma: no cover
    filename=config.log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)  # pragma: no cover