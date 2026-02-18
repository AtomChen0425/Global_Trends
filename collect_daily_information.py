from src import start_work
from src.Generators.report_generator_md import generate_report_CN, save_report,generate_report_EN
import logging

logger = logging.getLogger(__name__)

def collect_daily_information():
    intel = start_work.fetch_all_sources(limit=5)
    save_report(generate_report_EN(intel), output_dir="reports", lang="EN")
    save_report(generate_report_CN(intel), output_dir="reports", lang="CN")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - [%(name)s] %(message)s',
        datefmt='%H:%M:%S'
    )
    collect_daily_information()