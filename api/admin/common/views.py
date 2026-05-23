from rest_framework import generics,status
from apps.common.models import Phone,PhoneImage

from rest_framework.views import APIView
from rest_framework.response import Response



class PhoneListCreateAPIView(APIView):
    def get(self, request):
        phones = Phone.objects.prefetch_related('images').all()

        data = []
        for phone in phones:
            rasmlar = []
            for img in phone.images.all():
                rasmlar.append(request.build_absolute_uri(img.image.url))

            data.append({
                "id": phone.id,
                "title": phone.title,
                "created_at": phone.created_at,
                "images": rasmlar
            })

        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)

    def post(self,  request):
        title = request.data.get('title')
        images = request.FILES.getlist('images')

        if not title:
            return Response({
                "status": "error",
                "message": "title kiritishingiz majburiy "
            }, status=status.HTTP_400_BAD_REQUEST)

        phone = Phone.objects.create(title=title)

        for image in images:
            PhoneImage.objects.create(phone=phone, image=image)

        return Response({
            "status": "success",
            "message": "Telefon saqlandi",
            "data": {
                "id": phone.id,
                "title": phone.title,
                "created_at": phone.created_at,
            }
        }, status=status.HTTP_201_CREATED)


class PhoneRetrieveDestroyAPIView(APIView):

    def get_object(self, pk):
        # slug = self.request.GET.get('slug')
        try:
            return Phone.objects.prefetch_related('images').get(pk=pk)
        except Phone.DoesNotExist:
            return None


    def get(self, request, pk):
        phone = self.get_object(pk)

        if not phone:
            return Response({
                "status": "error",
                "message": "Telefon topilmadi!"
            }, status=status.HTTP_404_NOT_FOUND)

        rasmlar = []
        for img in phone.images.all():
            rasmlar.append(request.build_absolute_uri(img.image.url))

        data = {
            "id": phone.id,
            "title": phone.title,
            "created_at": phone.created_at,
            "images": rasmlar
        }

        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)


    def delete(self, request, pk):
        phone = self.get_object(pk)

        if not phone:
            return Response({
                "status": "error",
                "message": "Telefon topilmadi!"
            }, status=status.HTTP_404_NOT_FOUND)

        phone.delete()

        return Response({
            "status": "success",
            "message": f"ID: {pk} telefon o'chirildi."
        }, status=status.HTTP_200_OK)






