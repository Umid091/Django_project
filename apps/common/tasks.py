from celery import shared_task
from apps.common.models import Phone
import logging

logger = logging.getLogger(__name__)


@shared_task
def check_phones_task():
    print("--=====================TASK ISHLADI ===================================--------------------")

    phones = Phone.objects.prefetch_related('images').all()

    print(f"=========== Celery Tekshiruvi Boshlandi (Jami telefonlar: {phones.count()}) ============")

    for phone in phones:
        images_count = phone.images.count()
        print(f"=====Telefon ID: {phone.id} | Nomi: {phone.title} | Rasmlar soni: {images_count}======")

    print("--- Celery Tekshiruvi Yakunlandi ---")
    return f"{phones.count()} ta telefon muvaffaqiyatli tekshirildi."