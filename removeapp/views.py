from django.shortcuts import render
from django.http import FileResponse
from rembg import remove
from io import BytesIO

# Create your views here.
def removebackground(request):
    if request.method == 'POST':
        # Get the uploaded file from the form
        uploaded_file = request.FILES['remover']

        # Read the image into memory
        image_data = uploaded_file.read()

        # Use rembg to remove the background
        output = remove(image_data)

        # Create a response with the processed image
        response = FileResponse(BytesIO(output), content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="no_bg.png"'
        return response

    return render(request, 'removeapp/index.html')
