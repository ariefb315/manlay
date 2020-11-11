from django.shortcuts import render, redirect
from .models import Ms_Pegawai, Tr_header_skp, Ms_tugas_skp
from .forms import SKP, detil_SKP
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PegawaiSerializer, KinerjaSerializer

# Create your views here.
def home(requests):
    if requests.method == 'POST':
        form_skp = SKP(data=requests.POST)
        if form_skp.is_valid():
            new_form_skp = form_skp.save(commit=False)
            new_form_skp.post = post
            new_form_skp.save()
            return redirect('home')
    
    pegawai = Ms_Pegawai.objects.get(id=2)
    add_skp = SKP()
    frm_det_skp = detil_SKP()
    lead_val = getattr(pegawai, 'nip')
    print(lead_val)   
    pimpinan = Ms_Pegawai.objects.get(id=1)

    print(pegawai)
    print(pimpinan)
    context = {
        'pegawai':pegawai,
        'pimpinan':pimpinan,
        'SKP':add_skp,
        'detil_skp': frm_det_skp,
    }

    return render(requests,'home.html', context)

def add_skp(requests):
    headers_skp = Tr_header_skp.objects.get(id=1)
    detil_skp = Ms_tugas_skp.objects.filter(id_header_skp=headers_skp.pk)
    print(detil_skp)
    pegawai=Ms_Pegawai.objects.get(nama=headers_skp.nip_pegawai)
    pimpinan=Ms_Pegawai.objects.get(nip=headers_skp.nip_pimpinan)
    context = {
        'headers_skp':headers_skp,
        'pegawai':pegawai,
        'pimpinan':pimpinan,
        'detil_skp':detil_skp,
    }
    return render(requests,'add_skp.html', context)

def test(requests):
    if request.method == 'POST':
        variable = requests.POST

    context = {

    }

    return render(requests, 'test.html', context)

@api_view(['GET', 'POST'])
def pegawai_list(requests):
    if requests.method == 'GET':
        pegawai = Ms_Pegawai.objects.all()
        pegawai_serializer = PegawaiSerializer(pegawai, many=True)
        return Response(pegawai_serializer.data)
    
    elif requests.method == 'POST':
        pegawai_serializer = PegawaiSerializer(data=requests.data)
        if pegawai_serializer.is_valid():
            pegawai_serializer.save()
            return Response(pegawai_serializer.data, status=status.HTTP_201_CREATED)
        return Response(pegawai_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def kinerja_list(requests):
    if requests.method == 'GET':
        kinerja = Ms_tugas_skp.objects.all()
        kinerja_serializer = KinerjaSerializer(kinerja, many=True)
        return Response(kinerja_serializer.data)
    
    elif requests.method == 'POST':
        kinerja_serializer = KinerjaSerializer(data=requests.data)
        if kinerja_serializer.is_valid():
            kinerja_serializer.save()
            return Response(kinerja_serializer.data, status=status.HTTP_201_CREATED)
        return Response(kinerja_serializer.errors, status=status.HTTP_400_BAD_REQUEST)