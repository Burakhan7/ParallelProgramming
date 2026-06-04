import threading
from functools import wraps

def eszamanli_calistir(thread_sayisi: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Thread nesnelerini tek satırda oluşturuyoruz
            is parçacıkları = [
                threading.Thread(target=func, args=args, kwargs=kwargs)
                for _ in range(thread_sayisi)
            ]
            
            # Tüm thread'leri başlat
            for t in is_parçacıkları:
                t.start()
                
            # Hepsinin bitmesini bekle
            for t in is_parçacıkları:
                t.join()
                
        return wrapper
    return decorator
