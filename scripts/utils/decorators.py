from datetime import datetime
import time
import requests
def with_metadata(func):
    def wrapper(self, watermark) -> dict:
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timer_start = time.perf_counter()
        metadata = {
            "source_system": self.source_system,
            "status": None,
            "items_count": 0,
            "hash_value": str,
            "watermark": watermark,
            "start_time": start_time,
            "end_time": None,
            "execution_time": None,
            "error_message": None
        }
        try:
            raw_data: list[dict] = func(self, watermark)
            metadata['execution_time'] = time.perf_counter() - timer_start 
            metadata['end_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            metadata['status'] = "Success"
            return {"raw_data": raw_data,
                    "metadata": metadata
                    }
        except (ConnectionError, TimeoutError, KeyError, requests.HTTPError, Exception) as e:
            timer_end = time.perf_counter()
            metadata['end_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            metadata['error_message'] = str(e)
            metadata['status'] = "Fail"
            return {
                    "metadata": metadata
                    }
        
    return wrapper